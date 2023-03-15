This uses whisper to translate speech to text.
It uses tkinter to get a file via gui then after checking filetype and size;
it then uses pydub to split the file into 24mb sizes with 10 seconds of 
additional overlap to account for split words for example:
input audio:    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
time       :    0--------------------------------------------------------------------------------------------------------------------------30s
split chunks:   |-------------------------------------------||-----------------------------------------------------------------------------30s
overlap     :                                  |-----------------------------------|

splitting it as such should allow for more accurate reconstruction

The first problem I came across was trying to setup a virtual environment from batch, I want it to be 
accessible to others so I want the app to be installable via one click. When entering a virtual environment 
you cant just activate it outright you must call it from the batch file via 
"call %CD%/whateveryounamedyourvenv/Scripts/activate.bat" and then you can install your requirements file

This relies on FFMPEG which can be ionstalled from https://ffmpeg.org/


