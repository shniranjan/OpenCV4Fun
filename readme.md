# OpenCV project for fun

<b> Author: </b> Niranjan Shrestha niranjan@chautari.net

<b> Prerequisits: </b> <br>
This sript is written under following environment. <br>
Python 3.6.17 <br><br>
<b>Additional python packages </b><br><ul>
   <li> opencv-python </li>
   <li> os </li>
   <li> pickle </li>
   <li> gzip </li>
   <li> requests </li>
   <li> face_recognition </li>
   <li> numpy </li></ul>
    

    
<b>Testing: </b><br>
Post setting the environment, clone/download the repo.
Put person's pp-sized pictures inside gID folder with person full name.  At the moment only jpg picture file extension only supported. <br>
Ensure to create gID and data folders exists.
 <br>
<b>Configuration: </b><br>
Edit varbles.py file as per your environment.
The variables are self explanatory.
 <br> <br>

Run the following command: <br>
python recog_encode.py <br>
 <br>
This will create picture encoding and save in data folder.  Be patient, since it may take a while.
 <br>
Once completed, now you can run following command and enjoy: <br>
python recog.py
