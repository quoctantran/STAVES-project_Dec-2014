import glob
import os, os.path
import sys
import subprocess
#os.chdir("/Users/quoctan/Desktop/Test/")
#for file in glob.glob("*.jpg"):
#	print (file)

path = '/home/dmosuser/WorkspaceDocRead/STAVES/bin/'
	
for roots, dirs, files in os.walk(path):
	for file in files: 
		if file.endswith('.jpeg'):
			pureName = file.split('.')[0]
			filePath = os.path.join(path,file)	
			#the image files must be put in the bin folder, not in any subfolders
			os.system("./v-detectstaves_PC ../data/STAVES_portee.par " + filePath)
			os.system("rm "+filePath)
			
os.system("mogrify -format png /home/dmosuser/WorkspaceDocRead/STAVES/bin/*.jpg")

for roots, dirs, files in os.walk(path):
	for file in files: 
		if file.endswith('.png'):
			pureName2 = file.split('.')[0]
			filePath2 = os.path.join(path,file)
			os.system("mv " + filePath2 + " /home/dmosuser/1.10.2/")
		elif file.endswith('.jpg'):
			pureName3 = file.split('.')[0]
			filePath3 = os.path.join(path,file)
			os.system("rm " + filePath3)
