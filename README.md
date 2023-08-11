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

Also, on costs. Through the entire development cycle (way more token turns than shown in the demo) of this, my total OpenAI costs were a nickel. 

![image](https://user-images.githubusercontent.com/13913671/233161902-924d707f-fba8-415a-83c3-80dffaf560b3.png)

Video and demo of the script in action: https://youtu.be/nDTDlOze-40

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

You can modify the path where the script expects to find your keys.json file from the default of c:\keys\keys.json to a different location by changing the path in the script.

The structure of the keys.json should be like this;

### keys.json format

```
{
    "azure_api_key": "5ccc729abdexxxxxxxxxxxxxxx",
    "azure_region": "westus2",
    "openai_api_key": "sk-ccccccccccccccccccccccc"
}
```

Replace the values with your own keys. You can get your Azure API key and region from the Azure portal, once you have setup an Azure resource for speech services. You can get your OpenAI API key from the OpenAI dashboard.

## Note

Please note that due to time constraints, I was unable to thoroughly test all of the methods or fully document this repository and code. If you encounter any issues, please report them - your contributions are appreciated.

I initially developed this for my personal use and later decided to share it with the community. As I have not maintained any open-source projects before, any assistance or feedback would be greatly appreciated. If you would like to contribute in any way, please feel free to reach out to me with your suggestions.

I will try to use the latest libraries, and future releases will frequently include updates and improvements. Please take this into consideration before deciding to use the library. I want to make it clear that I cannot accept any responsibility for any damage caused by using the code in this repository. If you feel that this is not suitable for your purposes, you are free to explore alternatives.

I am incredibly busy. If I don't respond right away, please accept my apologies and let me know or try again. My GitHub feed gets long since I am not checking it every day and follow several busy repos, so if you @mention me, it should get my attention, or better yet, start a conversation using the Discussions link https://github.com/HaroldMitts/VoAIce/discussions/. 
