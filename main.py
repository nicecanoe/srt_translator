import os
import webvtt
from googletrans import Translator

def read_webvtt(file_path):
    webvtt_file = webvtt.from_srt(file_path)
    subtitles = webvtt_file.captions
    return subtitles


def translate_subtitles(subtitles, target_lang):
    translator = Translator()
    translated_subtitles = []
    for subtitle in subtitles:
        translated_text = translator.translate(subtitle.text, dest=target_lang)
        print(type(translated_text))
        translated_subtitles.append(translated_text.text)
    return translated_subtitles

def generate_dual_webvtt(subtitles, translated_subtitles):
    dual_subtitles = []
    for original, translated in zip(subtitles, translated_subtitles):
        dual_subtitles.append(f"{original.start} --> {original.end}\n{original.text}\n{translated}\n\n")
    return dual_subtitles

def translate_and_save_folder(input_folder, output_folder, target_lang):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".srt"):
            print(filename)
            if filename not in os.listdir(output_folder):
                print(filename)
                input_filepath = os.path.join(input_folder, filename)
                output_filepath = os.path.join(output_folder, filename)

                subtitles = read_webvtt(input_filepath)
                translated_subtitles = translate_subtitles(subtitles, target_lang)
                dual_subtitles = generate_dual_webvtt(subtitles, translated_subtitles)

                with open(output_filepath, "w", encoding="utf-8") as f:
                    for subtitle in dual_subtitles:
                        f.write(subtitle)

if __name__ == "__main__":
    source_lang = "en"
    target_lang = "zh-cn"
    input_folder_path = "03 CSS Fundamentals"
    output_folder_path = "output"

    translate_and_save_folder(input_folder_path, output_folder_path, target_lang)
