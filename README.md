# Gunnarrs-eindwerk

CCTV camera system w/a Raspberry Pi 5 over wireless connection to a network (4 cameras)  
The Raspberry Pi will capture frames from the four cameras and host a webserver using Flask where the video feed of will be available, the Windows app will pull the video feed of the currently selected camera from the matching page on the webserver.  
With object detection the windows app can automatically sta  rt recording once a person enters the frame, and notify the owner of the system.
Windows app will be a WinUI 3 app and have an easy to use graphical user interface.

Libraries used: Flask (webserver)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OpenCV (frame captures)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ultralytics (object detection)  

exampleCode is a simplefied version of the finalized python code the Raspberry Pi 5 will be running.

