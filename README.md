# Whisper-API-GUI
First commit
This uses whisper to translate speech to text.
It uses built in gradio functions to get a file via gui then;
it then uses pydub to split the file.

The first problem I came across was trying to setup a virtual environment from batch, I want it to be 
accessible to others so I want the app to be installable via one click. When entering a virtual environment 
you cant just activate it outright you must call it from the batch file via 
"call %CD%/whateveryounamedyourvenv/Scripts/activate.bat" and then you can install your requirements file

This relies on FFMPEG which can be installed from https://ffmpeg.org/

future improvments i could make would be to split the file into 24mb sizes with 10 seconds of 
additional overlap to account for split words for example:
input audio:    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
time       :    0--------------------------------------------------------------------------------------------------------------------------30s
split chunks:   |-------------------------------------------||-----------------------------------------------------------------------------30s
overlap     :                                  |-----------------------------------|

because the speech-to-text will have issues with sections where the words were cut off.

Anyway here is some Beautiful ascii art depicting the great Emu War (generated by GPT-3)

		    \  /
		   --oo--
		  /||  ||
		 / ||  ||
		/  ||  ||
	   /   ||  ||
	  /____||__||
	  |____|/ \|
	   \___/ \_/
	 ____\_/\_/
	/       \/
	\_______/
	   /\_/\
	  |___|_|
	   \_U_/
