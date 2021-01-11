# OpenCV project for fun

Author: Niranjan Shrestha niranjan@chautari.net

Prerequisits:
This sript is written under following environment.
Python 3.6.17
Additional python packages
    opencv-python
    os
    pickle
    gzip
    requests
    face_recognition
    numpy
    

    
Testing:
Post setting the environment, clone/download the repo.
Put person's pp-sized pictures inside gID folder with person full name.  At the moment only jpg picture file extension only supported.
Ensure to create gID and data folders exists.

Configuration:
Edit varbles.py file as per your environment.
The variables are self explanatory.


Run the following command
python recog_encode.py

This will create picture encoding and save in data folder.  Be patient, since it may take a while.

Once completed, now you can run following command and enjoy
python recog.py
