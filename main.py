import math
import openai
from pydub import AudioSegment
import datetime
import gradio as gr


def loadAudioFile(inputFile, subtitleTime, outputSRT,APIkey):
    openai.api_key = APIkey
    transcript = ""
    audio = AudioSegment.from_file(inputFile)
    # PyDub handles time in milliseconds
    if outputSRT == False:
        subtitleTime = 10 *60 # 10 minutes
    section_time = subtitleTime * 1000
    numSections = int(math.ceil((audio.duration_seconds) / (subtitleTime)))
    for i in range(0, numSections):
        print("section " + str(i) + " of " + str(numSections))
        Seconds_of_section = audio[i *section_time:section_time * (i + 1)]
        print(audio.duration_seconds)
        Seconds_of_section.export("tmp/section.mp3", format="mp3")
        filename = "inputFile! " + str(audio.duration_seconds)
        audio_file= open("tmp/section.mp3", "rb")
        fromTimeToTime = str(datetime.datetime.fromtimestamp((i *section_time) / 1000.0, tz=datetime.timezone.utc).strftime("%X")) + " --> " + str(datetime.datetime.fromtimestamp((section_time * (i + 1)) / 1000.0, tz=datetime.timezone.utc).strftime("%X"))
        transcribed = openai.Audio.transcribe("whisper-1", audio_file).text
        print(fromTimeToTime)
        if outputSRT == False:
            transcript = transcript + transcribed
        else:
            if len(transcribed) > 10:
                for j in range(0, math.ceil(len(transcribed)/2) + 9):
                    print("j: " + str(j) + " " + transcribed[j])
                    if transcribed[j] == " ":
                        transcribed[j].replace(" ", "\n" )
            transcript = transcript + str(i+1) + "\n" + fromTimeToTime + "\n" + transcribed + "\n" + "\n"
    return transcript

demo = gr.Interface(
    fn=loadAudioFile,
    inputs=[gr.Audio(source="upload", type="filepath", label="Upload an audio file"), gr.Slider(1, 30,label="seconds of audio to transcribe",value=10,step=1),gr.Checkbox(label="Output to SRT format",default=True),gr.Textbox(label="OpenAI API Key",type="password",default="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")],
    outputs=["text"],
)


#print(input("Enter your name: "))
if __name__ == "__main__":
    print('get started')
    demo.launch()

