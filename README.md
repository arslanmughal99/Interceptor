# Interceptor
By : Arslan ..

## instalation :
pip3 install -r requirments.txt

## Usage :
python3 interceptor.py

after running the script will prompt you to enter the file type to be Intercept from the victim computer 

\
**EXAMPLE :**

[~] Please Enter file extension to intercept\
[~] e.g ('exe', 'mp4', 'mp3', 'jpg' etc... ) \
[?] 
just enter the file type (i.e exe, mp4, mp3, jpg, jpeg ... etc)

**EXAMPLE :**

[~] Please Enter file extension to intercept\
[~] e.g ('exe', 'mp4', 'mp3', 'jpg' etc... ) \
[?] **exe**

Press Enter and then script will prompt you to Enter the file download link by which you want to replaced the intercepted file of victim

**NOTE:** *first upload the file to any online drive or host file locally by apache server*  file by which you want to replace the intercepted file can be of any type 

**EXAMPLE:**

[~] Please Enter modified file download link (URL)\
[~] e.g ('https://www.ExampleDownloadLink.com') \
[?] 

Here i want to replace the victim "exe" file download with a "jpg" image
 
**EXAMPLE:**

[~] Please Enter modified file download link (URL)\
[~] e.g ('https://www.ExampleDownloadLink.com') \
[?] https://images.pexels.com/photos/1310788/pexels-photo-1310788.jpeg?cs=srgb&dl=architecture-art-classic-1310788.jpg&fm=jpg

Press Enter and main process for intercepting files will be start 
if the file is intercepted and replaced it will indicate you 

**Note:** Before running script in local network you must be MAN IN THE MIDDLE using arpspoof or any other programe you are comfortable with
also currently this script only supports HTTP and will not work with HTTPS  we are working for HTTPS support and hopefully we'll  soon update :)
Pull Request are Welcome :) 