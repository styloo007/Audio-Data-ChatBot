import assemblyai as aai
from constants import assembly_api_key

aai.settings.api_key= 'PASTE YOUR ASSEMBLY API KEY IN HERE, GET IT FROM THE LINK BELOW'
#https://www.assemblyai.com/app

audio_url = 'PASTE YOUR AUDIO URL IN HERE, SAMPLE GIVEN BELOW"
#audio_url= "https://storage.googleapis.com/aai-web-samples/architecture-call.mp3"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(audio_url)

result = transcript.lemur.task(
  "I've Attached a transcript of an Audio Call, Go through it thouroughly and answer the questions",
  final_model= aai.LemurModel.claude3_5_sonnet
  )

#print(result.response)
while(True):
  prompt= input(" USER: ")
  if prompt.lower()=='exit' or prompt.lower()=='quit':
    print("It was nice chatting with you. Feel free to reach out if you have any other questions.")
    break

  result=transcript.lemut.task(prompt, final_model=aai.LemurModel.claude3_5_sonnet)
  print("ChatBot: ", result.response)
  
    

