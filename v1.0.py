import azure.cognitiveservices.speech as speechsdk
import os
import tempfile
import openai

import json

def load_api_keys(file_path):
    with open(file_path, "r") as f:
        keys = json.load(f)
    return keys


def transcribe_audio(speech_config):
    audio_config = speechsdk.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    result = speech_recognizer.recognize_once_async().get()
    return result.text.strip()



def generate_response(input_text):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": input_text}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    assistant_response = response['choices'][0]['message']['content']
    return assistant_response


def synthesize_speech(speech_config, response_text):
    audio_config = speechsdk.AudioConfig(filename=None)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    result = synthesizer.speak_text_async(response_text).get()
    return result.audio_data

def save_audio_to_mp3(audio_data, output_path):
    with open(output_path, "wb") as f:
        f.write(audio_data)

def play_mp3(audio_file_path):
    os.system(f"powershell -c (New-Object Media.SoundPlayer \"{audio_file_path}\").PlaySync();")

def main():
    keys = load_api_keys("C:\\GitHub\\VoAI\\VoAI\\keys.json")
    azure_api_key = keys["azure_api_key"]
    azure_region = keys["azure_region"]
    openai_api_key = keys["openai_api_key"]

    speech_config = speechsdk.SpeechConfig(subscription=azure_api_key, region=azure_region)
    openai.api_key = openai_api_key

    while True:
        print("Listening...")

        # Transcribe audio from the microphone
        input_text = transcribe_audio(speech_config)
        print(f"Input: {input_text}")

        if "ai quit" in input_text.lower():
            break

        # Generate a response using GPT-4
        response_text = generate_response(input_text)
        print(f"Response: {response_text}")

        # Synthesize speech from the response text
        audio_data = synthesize_speech(speech_config, response_text)

        # Save synthesized speech as an MP3 file
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            save_audio_to_mp3(audio_data, f.name)
            audio_file_path = f.name

        # Play the MP3 file
        play_mp3(audio_file_path)

        # Remove the temporary MP3 file
        os.remove(audio_file_path)

if __name__ == "__main__":
    main()
