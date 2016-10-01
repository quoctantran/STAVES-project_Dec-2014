import glob
import os, os.path
import sys
import subprocess
#os.chdir("/Users/quoctan/Desktop/Test/")
#for file in glob.glob("*.jpg"):
#	print (file)

path = '/Users/minhngo/Desktop/Test'
	
for roots, dirs, files in os.walk(path):
	for file in files: 
		if file.endswith('.jpg'):
			pureName = file.split('.')[0]
			print pureName
#			print file
			print (os.path.join(path,file))
