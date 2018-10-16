# Interceptor
By : Arslan ..

## instalation :
pip3 install -r requirments.txt

## Usage :
**For reference Please check screenshots in the end :)**

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


**Starting Script:**
![enter image description here](https://dl.dropbox.com/s/f62yqqvkjp89exh/1.png?dl=1)

**Running Script:**
*Entering file type to intercept* (in my case exe you can select any e.g mp4, mp3, jpg and so on ..)
![enter image description here](https://dl.dropbox.com/s/cjbvbnliv5qtz0x/2.png?dl=1)

**Entering File link by which Intercepted file need to be replaced**
![enter image description here](https://dl.dropbox.com/s/jpptbsn55eih5i8/3.png?dl=1)

**Started Intercepting Victim downloads if any :**
![enter image description here](https://dl.dropbox.com/s/3u585z08s4ir6xn/4.png?dl=1)

**Detected request packets :**

![enter image description here](https://dl.dropbox.com/s/jm2lphpa39o8p5b/5.png?dl=1)

**Detected File download in victim computer:
and Replaced it successfully !**

![enter image description here](https://dl.dropbox.com/s/7umrtah60ogf3jc/6.png?dl=1)
