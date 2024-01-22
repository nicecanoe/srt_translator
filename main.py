import os
import webvtt
from googletrans import Translator
import codecs

def read_webvtt(file_path):
    webvtt_file = webvtt.from_srt(file_path)
    subtitles = webvtt_file.captions
    return subtitles


def translate_subtitles(subtitles, target_lang):
    translator = Translator()
    translated_subtitles = []
    for subtitle in subtitles:
        translated_text = translator.translate(subtitle.text, dest=target_lang)
        translated_subtitles.append(translated_text.text)
    return translated_subtitles

def generate_dual_webvtt(subtitles, translated_subtitles):
    dual_subtitles = []
    i = 0
    for original, translated in zip(subtitles, translated_subtitles):
        i += 1
        dual_subtitles.append(f"{i}\n{original.start} --> {original.end}\n{original.text}\n{translated}\n\n")
    return dual_subtitles

def translate_and_save_folder(input_folder, output_folder, target_lang):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        i = 0
        if filename.endswith(".srt"):
            print(filename)
            if filename not in os.listdir(output_folder):
                i += 1
                print(filename)
                input_filepath = os.path.join(input_folder, filename)
                output_filepath = os.path.join(output_folder, filename)

                subtitles = read_webvtt(input_filepath)
                translated_subtitles = translate_subtitles(subtitles, target_lang)
                dual_subtitles = generate_dual_webvtt(subtitles, translated_subtitles)

                with codecs.open(output_filepath, "w", encoding="utf-8-sig") as f:
                    for subtitle in dual_subtitles:
                        f.write(subtitle)

if __name__ == "__main__":
    source_lang = "en"
    target_lang = "zh-cn"
    input_folder_path = "01 - Welcome to the course! Here we will help you get started in the best conditions"
    output_folder_path = "01 - Welcome to the course! Here we will help you get started in the best conditions/output"

    translate_and_save_folder(input_folder_path, output_folder_path, target_lang)
