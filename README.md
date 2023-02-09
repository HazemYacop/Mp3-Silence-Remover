# Mp3-Silence-Remover V0.22
A Windows Software that deletes the silence at the beginning of mp3 file(s)

Important Notes :

-When You Run the project's main file ("main.py"), it may give you an ERROR due to missing files.
 You can fix that by simply installing ffmpeg on your windows or you can just download these files and add them to the project:
 - ffmpeg.exe
 - ffplay.exe
 - ffprobe.exe

-If you are trying to export the project into an excutable (.exe) file by Pyinstaller or any other libraries like it, you have to add the above files with it too

-The Program Deletes only Silence at the beginning and the end of any mp3 file(s)

# Used packages in this project :
- PySide2
- webbrowser
- pydub
