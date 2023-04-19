# VoAIce v1
 Voice of AI
 
A Python script which leverages OpenAI GPT API and (ACS) Azure Cognitive Services (Azure Speech Services) to create a talking AI. 
 
v1 waits for an exit keyword and loops through continuously conversing with the user until it hears one of a few designated keywords to exit to script.

I chose ACS over the popular ElevenLabs text to speech engine due to costs. You can get a lot of free speech services from Azure, whereas ElevenLabs is kind of pricy. Yes, ElevenLabs has a free plan, but it is limited to 3 voices and 10k characters per month. ACS on the other hand has hundreds of voices, including international, and has 20k characters per month for the free plan and the paid plan is very cheap. Also, ACS supports SAML, which enables you fine control over pronuciations. 

