#This file sets up working environment

#dpath is location for data folder where all the training image encoded data will be saved.
dpath = './data'

#fpath is the location of the folder with ppsized picture with person's name is saved in jpg extension.
fpath = './gID'

#This will adjust the image size
mlr=2 #image multiplier

#url for ipcamera, edid as per your need
url="http://192.168.1.100/capture"

#Do not touch beyound this unless you are sure
images = []
classNames = []


