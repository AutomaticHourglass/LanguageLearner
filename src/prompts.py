"""
Prompt templates for language learning application.
Contains example data and functions to generate prompts for the language model.
"""

# Example data with word/phrase entries in XML format
# Each entry contains:
# - input: the German word/phrase to learn
# - konzept: the word and its translation
# - explanation: description of the word's meaning and usage
# - de: example sentence in German
# - en: example sentence in English
examples = """
<data>
    <entry>
        <input>abfahren</input>
        <output>
            <konzept>abfahren --- to depart</konzept>
            <explanation>A verb meaning to leave or depart from a place.</explanation>
            <de>Der letzte Bus fährt gleich ab, wir müssen uns beeilen!</de>
            <en>The last bus is leaving soon, we need to hurry!</en>
        </output>
    </entry>
    <entry>
        <input>der Vorschlag</input>
        <output>
            <konzept>der Vorschlag --- suggestion</konzept>
            <explanation>A noun meaning a proposal or suggestion for consideration.</explanation>
            <de>Dein Vorschlag für den Wochenendausflug klingt fantastisch!</de>
            <en>Your suggestion for the weekend trip sounds fantastic!</en>
        </output>
    </entry>
    <entry>
        <input>aufpassen</input>
        <output>
            <konzept>aufpassen --- to pay attention</konzept>
            <explanation>A verb meaning to be careful or watchful.</explanation>
            <de>Pass auf den heißen Kaffee auf, er ist gerade frisch gebrüht!</de>
            <en>Watch out for the hot coffee, it's freshly brewed!</en>
        </output>
    </entry>
    <entry>
        <input>die Entwicklung</input>
        <output>
            <konzept>die Entwicklung --- development</konzept>
            <explanation>A noun referring to progress or development process.</explanation>
            <de>Die Entwicklung künstlicher Intelligenz schreitet jeden Tag voran.</de>
            <en>The development of artificial intelligence advances every day.</en>
        </output>
    </entry>
    <entry>
        <input>ausgezeichnet</input>
        <output>
            <konzept>ausgezeichnet --- excellent</konzept>
            <explanation>An adjective meaning outstanding or excellent.</explanation>
            <de>Deine Präsentation war wirklich ausgezeichnet, alle waren beeindruckt!</de>
            <en>Your presentation was truly excellent, everyone was impressed!</en>
        </output>
    </entry>
    <entry>
        <input>die Gelegenheit</input>
        <output>
            <konzept>die Gelegenheit --- opportunity</konzept>
            <explanation>A noun meaning opportunity or occasion.</explanation>
            <de>Diese Gelegenheit kommt vielleicht nie wieder, du solltest sie nutzen.</de>
            <en>This opportunity might never come again, you should take it.</en>
        </output>
    </entry>
    <entry>
        <input>nachdenken</input>
        <output>
            <konzept>nachdenken --- to reflect</konzept>
            <explanation>A verb meaning to think deeply about something.</explanation>
            <de>Ich muss über dieses interessante Jobangebot nachdenken.</de>
            <en>I need to think about this interesting job offer.</en>
        </output>
    </entry>
    <entry>
        <input>die Unterstützung</input>
        <output>
            <konzept>die Unterstützung --- support</konzept>
            <explanation>A noun meaning help or support.</explanation>
            <de>Ohne deine Unterstützung hätte ich es nie geschafft.</de>
            <en>Without your support, I would have never made it.</en>
        </output>
    </entry>
    <entry>
        <input>einverstanden</input>
        <output>
            <konzept>einverstanden --- agreed</konzept>
            <explanation>An adjective meaning to be in agreement.</explanation>
            <de>Wenn alle einverstanden sind, können wir das Projekt starten.</de>
            <en>If everyone agrees, we can start the project.</en>
        </output>
    </entry>
    <entry>
        <input>die Bedeutung</input>
        <output>
            <konzept>die Bedeutung --- meaning</konzept>
            <explanation>A noun referring to the significance or meaning of something.</explanation>
            <de>Die Bedeutung dieses alten Symbols bleibt ein Mysterium.</de>
            <en>The meaning of this ancient symbol remains a mystery.</en>
        </output>
    </entry>
    <entry>
        <input>aufhören</input>
        <output>
            <konzept>aufhören --- to stop</konzept>
            <explanation>A verb meaning to cease or stop doing something.</explanation>
            <de>Kannst du bitte aufhören, mit dem Fuß zu wippen? Es macht mich nervös.</de>
            <en>Could you please stop tapping your foot? It's making me nervous.</en>
        </output>
    </entry>
    <entry>
        <input>die Möglichkeit</input>
        <output>
            <konzept>die Möglichkeit --- possibility</konzept>
            <explanation>A noun meaning possibility or opportunity.</explanation>
            <de>Besteht die Möglichkeit, das Meeting zu verschieben?</de>
            <en>Is there a possibility to reschedule the meeting?</en>
        </output>
    </entry>
    <entry>
        <input>zufrieden</input>
        <output>
            <konzept>zufrieden --- satisfied</konzept>
            <explanation>An adjective meaning content or satisfied.</explanation>
            <de>Die Kunden sind mit dem neuen Design sehr zufrieden.</de>
            <en>The customers are very satisfied with the new design.</en>
        </output>
    </entry>
    <entry>
        <input>die Entscheidung</input>
        <output>
            <konzept>die Entscheidung --- decision</konzept>
            <explanation>A noun referring to a choice or decision made.</explanation>
            <de>Diese Entscheidung wird mein ganzes Leben verändern.</de>
            <en>This decision will change my entire life.</en>
        </output>
    </entry>
    <entry>
        <input>vorbereiten</input>
        <output>
            <konzept>vorbereiten --- to prepare</konzept>
            <explanation>A verb meaning to prepare or get ready for something.</explanation>
            <de>Wir müssen uns gut auf die wichtige Präsentation vorbereiten.</de>
            <en>We need to prepare well for the important presentation.</en>
        </output>
    </entry>
</data>
"""


# Function to create a prompt for a given input phrase
# Inserts the input phrase into the XML template
create_example = lambda input_phrase: f"""{examples[:-8]}
    <entry>
        <input>{input_phrase}</input>"""

# System prompt for the language model
# Instructs the model on its role and expected output format
sys_prompt = """You are a helpful assistant in 2 languages, English and Deutsch. 
You give explanation and example sentences with respect to the format provided in entries. 
You only give the xml output, nothing else.
Make sure to only use the proper language in each field."""
