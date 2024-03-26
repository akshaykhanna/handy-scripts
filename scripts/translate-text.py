from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# Example usage
text_to_translate = "Deep learning has revolutionized the field of artificial intelligence and machine learning in recent years. This powerful domain enables computers to learn and improve their performance on a task with little or no human intervention, making it a game-changer in various industries. In this section, we will delve into the world of deep learning, exploring its core components, applications, and challenges."
translated_text = translate_text(text_to_translate, target_language='hi')
print("Translated text:", translated_text)
