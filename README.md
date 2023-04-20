# VoAIce v1
 Voice of AI
 
A Python script which leverages OpenAI GPT API and (ACS) Azure Cognitive Services (Azure Speech Services) to create a talking AI. 
 
v1 waits for an exit keyword and loops through continuously conversing with the user until it hears one of a few designated keywords to exit to script.

1. Listen for spoken audio from a microphone
2. Transcribe the audio from step 1 into text for use in step 3
3. Input the transcribed text from step 2 into GPT API for processing by GPT
4. Produce a response to the input from step 3 using GPT API
5. Convert the text produced by step 4 into audio
6. Play the audio from step 5 back to the user
7. Wait for the user response and repeat the cycle again, based on the user response. If the user uses a keyword, end the routine.

I chose ACS over the popular ElevenLabs text to speech engine due to costs. You can get a lot of free speech services from Azure, whereas ElevenLabs is kind of pricy. Yes, ElevenLabs has a free plan, but it is limited to 3 voices and 10k characters per month. ACS on the other hand has hundreds of voices, including international, and has 20k characters per month for the free plan and the paid plan is very cheap. Also, ACS supports SAML, which enables you fine control over pronuciations. 

Also, on costs. Through the entire development cycle of this, my total OpenAI costs were a nickel. 

![image](https://user-images.githubusercontent.com/13913671/233161902-924d707f-fba8-415a-83c3-80dffaf560b3.png)

Video and demo of the script in action: https://youtu.be/1Z4Z4Z4Z4Z4

## Modules required to be installed

To run this script, you'll need to meet the following system requirements:

1. Python: The script requires Python 3.6 or higher. Some of the libraries and syntax used may not be compatible with Python 2.x or older versions of Python 3.x.
2. Libraries and packages: You'll need to install the following packages using pip or your preferred package manager:
    
- azure-cognitiveservices-speech: This package is required for speech recognition and text-to-speech capabilities provided by Azure Speech Services.

`pip install azure-cognitiveservices-speech`

- openai: This package is needed to access the OpenAI API and interact with the GPT-4 language model.

`pip install openai`

- FFmpeg: While not a Python package, FFmpeg is required for audio playback using the ffplay command in the play_audio function. You'll need to download and install FFmpeg on your system. Installation instructions can be found on the official FFmpeg website (https://ffmpeg.org/download.html).

Ensure that you have these packages installed with the appropriate versions before running the script. You might also want to set up a virtual environment for your project to manage these dependencies more efficiently.

## JSON file format

You can modify the path where the script expects to find your keys.json file from the default of c:\GitHub\VoAI\VoAI\keys.json to a different location by changing the path in the script.

The structure of the keys.json should be like this;

keys.json format [just show an on-screen example of the format expected]

```
{
    "azure_api_key": "5ccc729abdexxxxxxxxxxxxxxx",
    "azure_region": "westus2",
    "openai_api_key": "sk-ccccccccccccccccccccccc"
}
```

Replace the values with your own keys. You can get your Azure API key and region from the Azure portal, once you have setup an Azure resource for speech services. You can get your OpenAI API key from the OpenAI dashboard.