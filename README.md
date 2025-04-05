# LanguageLearner

An interactive language learning application that uses AI to help users learn German vocabulary with contextual examples and speech.

## Overview

LanguageLearner is a tool designed to facilitate language learning by providing:

- Vocabulary words with translations and explanations
- Contextual example sentences
- Text-to-speech pronunciation in both the target language and English
- Spaced repetition learning algorithm

The application uses a language model to generate explanations and example sentences for German vocabulary words, helping users understand usage in context.

## Features

- AI-powered explanations and contextual examples
- Text-to-speech functionality for pronunciation practice
- Visual display of learning content
- Adaptive learning system that focuses on words needing more practice
- Support for A1, A2, and B1 level German vocabulary

## Project Structure

```
LanguageLearner/
│
├── data/               # Language vocabulary data
│   └── deutsch.py      # German vocabulary words
│
├── src/                # Source code
│   ├── prompts.py      # Prompt templates for the language model
│   └── tts.py          # Text-to-speech functionality
│
├── main.py             # Main application file
├── README.md           # Documentation
└── requirements.txt    # Dependencies
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/LanguageLearner.git
   cd LanguageLearner
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Add your language model path in `main.py`:
   ```python
   model_path_token = "path/to/your/model"
   ```

## Usage

Run the application from the root directory:

```
python main.py
```

The application will:
1. Select a German word based on the learning algorithm
2. Generate an explanation and example sentences
3. Display the content in a window
4. Read the content aloud
5. Wait for 2 minutes before showing the next word

## How It Works

1. **Word Selection**: Words are selected based on a weighting system. Initially, all words have equal weight. After a word is shown, its weight is reduced, making it less likely to appear soon.

2. **Content Generation**: The application sends the selected word to a language model, which generates an explanation and contextual examples.

3. **Visual Display**: The content is displayed in a window with the word, translation, explanation, and example sentences.

4. **Text-to-Speech**: The application reads the content aloud, alternating between German and English.

5. **Progress Tracking**: The application tracks progress through a weights file, ensuring focus on words that need more practice.

## Customization

- Add new vocabulary words in `data/deutsch.py`
- Adjust the delay between words by modifying the `time.sleep()` value in `main.py`
- Change the voice settings in `src/tts.py`

## License

This project is licensed under the Apache License, Version 2.0 - see the LICENSE file for details.

## Citation

```
@software{LanguageLearner,
  author = {Unsal Gokdag},
  title = {LanguageLearner: AI-Powered Language Learning Tool},
  year = {2025},
  url = {https://github.com/AutomaticHourglass/LanguageLearner}
}
```
