"""
Language Learning Application

This application helps users learn German vocabulary using AI-powered
explanations and examples with text-to-speech capabilities.

The program displays German words/phrases with their translations,
explanations, and example sentences, using a language model to generate
contextual examples for better learning.
"""

import ctypes
import re
import os
import pickle
import time
import random
import numpy as np
import cv2
import pyttsx3
from datetime import datetime
from tqdm import tqdm
from llama_cpp import Llama
from PIL import ImageFont, ImageDraw, Image

from src.tts import speak
from src.prompts import create_example, sys_prompt
from data.deutsch import *

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize language model
model_path_token = "path/to/your/model/tokenizer.model.gguf"  # Path to the tokenizer model GGUF format for now
ctx_length = 2048  # Context length for the language model

llm = Llama(
    model_path=model_path_token,
    n_gpu_layers=-1,  # Use all available GPU layers
    n_ctx=ctx_length,
    temperature=1,
    embedding=False,
    verbose=True,
)


def llm_call(sys_prompt, prompt, llm):
    """
    Call the language model with system and user prompts.
    
    Args:
        sys_prompt (str): System instructions for the language model
        prompt (str): User prompt/query
        llm: The language model instance
        
    Returns:
        str: The model's response
    """
    response = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1  # Low temperature for more deterministic output
    )
    return response['choices'][0]['message']['content']


def extract_elements(xml_string):
    """
    Extract elements from the XML response of the language model.
    
    Args:
        xml_string (str): XML string containing language learning data
        
    Returns:
        list: Extracted elements (concept, explanation, German example, English example)
    """
    # Define regex patterns for each element
    patterns = {
        'konzept': r'<konzept>(.*?)</konzept>',
        'explanation': r'<explanation>(.*?)</explanation>',
        'de': r'<de>(.*?)</de>',
        'en': r'<en>(.*?)</en>',
    }

    # Extract elements using regex
    elements = []
    for key in ['konzept', 'explanation', 'de', 'en', 'de']:
        match = re.search(patterns[key], xml_string, re.IGNORECASE)
        if match:
            if key == 'konzept':
                a, b = match.group(1).split('---')
                elements.append(a.strip())
                elements.append(b.strip())
            else:
                elements.append(match.group(1))

    return elements


def named_turn(phrase):
    """
    Process a single phrase by generating explanations and examples.
    
    Args:
        phrase (str): The German word or phrase to process
        
    Returns:
        list: Processed elements (word, translation, explanation, examples)
    """
    print(f'Konsept: {phrase}')
    metin = create_example(phrase)

    # Get response from language model
    res = llm_call(sys_prompt, metin, llm)
    print(res)
    
    # Extract elements from the response
    elements = extract_elements(res)
    print('\n'.join(elements))

    return elements


def draw_multiline_text(text_list, start_pos=(0,0), max_width=960, max_height=220, color=(255, 255, 255)):
    """
    Create an image with the learning content.
    
    Args:
        text_list (list): List of text elements to display
        start_pos (tuple): Starting position coordinates (x, y)
        max_width (int): Maximum width of the text area
        max_height (int): Maximum height of the text area
        color (tuple): RGB color for the text
        
    Returns:
        numpy.ndarray: Image with rendered text
    """
    # Format the text elements for display
    text_show = ([f"{text_list[0]} - {text_list[1][0].upper()}{text_list[1][1:]}"] +
                 [i for i in text_list[2].split('.') if len(i)>1] +
                 text_list[3:])

    # Initial coordinates
    x, y = start_pos

    # Create a black background image
    img = np.zeros((max_height, max_width, 3), dtype=np.uint8)

    # Calculate text height for each line
    text_height = max_height / (len(text_show)+1)
    current_y = y + text_height/2
    
    # Add each line of text to the image
    for i, line in enumerate(text_show):
        # Check if we've exceeded the height limit
        if current_y + text_height > y + max_height:
            break

        # Center the text horizontally
        text_x = x + max_width // 20

        # Convert to PIL Image for text rendering
        pil_image = Image.fromarray(img)

        # Use different font sizes based on line number
        if i == 1:
            font = ImageFont.truetype('Verdana.ttf', 20)
        else:
            font = ImageFont.truetype('Verdana.ttf', 25)
            
        # Draw the text
        draw = ImageDraw.Draw(pil_image)
        draw.text((text_x, current_y), line, font=font)

        # Convert back to numpy array and BGR color space for OpenCV
        img = np.asarray(pil_image)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        # Update y coordinate for next line
        current_y += text_height

    return img


# Add a main function that can be imported
def main():
    """
    Main function to run the language learning application.
    Can be called from an external script.
    """
    # Initialize random seed
    random.seed(datetime.now().timestamp())
    
    # Load or initialize word weights
    # Words with higher weights are more likely to be selected
    if os.path.exists('weights.pkl'):
        with open('weights.pkl', 'rb') as f:
            weights = pickle.load(f)
            dataset = weights.keys()
    else:
        max_repetitions = 3
        dataset = list(set(a2_german_words + b1_german_words))
        weights = {phrase: 2**max_repetitions for phrase in dataset}
    
    # Initialize progress bar
    pbar = tqdm()
    
    # Main learning loop - continues until all words reach weight 0
    while sum(weights.values()) > 0:
        try:
            # Select a word based on weights (higher weight = higher probability)
            keys, values = list(zip(*weights.items()))
            values = [i / sum(values) for i in values]
            
            phrase = random.choices(keys, weights=values, k=1)[0]
            weights[phrase] //= 2  # Reduce the weight after selection
            
            # Get language learning elements for the selected phrase
            elements = named_turn(phrase)
            
            # Create and display the visual representation
            img = draw_multiline_text(elements)
            cv2.imshow('Learn', img)
            
            # Read aloud the examples in alternating languages
            languages = ['de', 'en', 'en', 'de', 'en', 'de']
            for s, l in zip(elements, languages):
                speak(s, l)
            
            # Save the updated weights
            with open('weights.pkl', 'wb') as f:
                pickle.dump(weights, f)
            
            # Wait before showing the next word
            time.sleep(120)  # 2 minutes per word
            
        except Exception as e:
            print(f"Error: {e}")
            pass
        
        # Update progress bar
        pbar.set_description(f'sum: {sum(weights.values())}')
        pbar.update(1)
    
    # Clean up
    cv2.destroyAllWindows()
    engine.stop()

# Main application loop
if __name__ == "__main__":
    main()
