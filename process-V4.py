#this version is modified with some differences: 
#instead of checking the number of files
#this script will immediately scan the working folder for image file 
#create the corresponding output text file
#then ILIB extraction and BonzaiBoost

import glob
import os, os.path
import sys
import subprocess
import re
import shutil

def main():
	if len(sys.argv) - 1:
		engine(''.join(sys.argv[i:]))
	else:
		print os.path.basename(sys.argv[0]), '<directory>'

def engine(path):
	#this is from the old version to count the number of files
	#directories = files = 0
	#for information in os.walk(path):
	#	directories += len(information[1])
	#	files += len(information[2])
	#print 'Directories = ', directories
	#print 'Files = ', files
	
	#detect folders, for each folder, detect the images within each folder 
	#extract the link for each image
	#extract the name for each image, without extension
	#./a.out images'link + " s > " + fileName + ".txt"
	
	for roots, dirs, files in os.walk(path):
		for file in files: 
			if file.endswith('.png'):
				pureName = file.split('.')[0]
				filePath = os.path.join(path,file)	
				
				#feature extraction step with ILIB library
				#execute the command line for conversion
				
				os.system("./a.out " + filePath + " s > " + file + ".txt")
				
				currentPath = "/home/dmosuser/1.10.2/" + file + ".txt"
		
				#open the featured files for modification
				file_in = open(currentPath, 'r+')
				content = file_in.readlines()
				file_out = open(currentPath, 'w')
		
				#modify the file to add the image's index with temporary label
				for line in content: 
					line_bis = ''
					for char in line:
						if char == 's':
							line_bis =  line_bis + ' s, ' + file + ',a'
						else:
							line_bis += char
					file_out.writelines(line_bis)
		
				# move the file to results_folder Folder
				os.system("mv " + file +".txt /home/dmosuser/1.10.2/results_folder/")

# add more line of codes 
# to remove the data from musicData and results_folder for new test
# create others folder 
# move files to this folder - images left 	

def fileMove(path): 
	for the_file in os.listdir(path):
		fileName = os.path.join(path,the_file)
		
		if fileName[len(fileName)-3:len(fileName)] == 'png':
			pathName = "/home/dmosuser/1.10.2/others"
			if os.path.exists(pathName):
				os.system("mv " +str(fileName) + " /home/dmosuser/1.10.2/others/")
			else:
				os.system("mkdir others")
				os.system("mv " +str(fileName) + " /home/dmosuser/1.10.2/others/")

def removeFiles(path): 
	for the_file in os.listdir(path):
		file_path = os.path.join(path, the_file)
		try: 
			if os.path.isfile(file_path):
				os.unlink(file_path)
		except Exception, e: 
			print e	
		
if __name__ == '__main__':
	os.system("python /home/dmosuser/WorkspaceDocRead/STAVES/bin/StaffLineRemoval.py")
	
	engine("/home/dmosuser/1.10.2")
	main()
	os.system("python combine.py" )
	#os.system("mv /home/dmosuser/1.10.2/results_folder/result.data /home/dmosuser/1.10.2/")
	
	os.system("./bonzaiboost -S experiment6 -boost adamh -n 50")
	os.system("./bonzaiboost -S experiment6 -boost adamh -n 50 -C -c single <result.data> testResult.txt")
	
	resultPath = "/home/dmosuser/1.10.2/testResult.txt"
	
	inputFile = open(resultPath, 'r+')
	contentBonzai = inputFile.readlines()
	outputFile = open(resultPath, 'w')	
	
	T = ['amin', 'becarre', 'bemol','diese','dmsoupir','finpedale','forte','huit','mezzo','neuf','pause','pedale','piano','point','quatre','sept','six','soupir','talon','trois','un', 'chevronh', 'chevronv', 'clesol', 'clefa', 'cleut', 'cbar']
	
	for line in contentBonzai:
		line_extra = ''
		for char in line:
			if char == ',':
				line_extra = line_extra + ' '
			else:
				line_extra += char
		outputFile.writelines(line_extra)
	outputFile.close()
	
	newFile = open(resultPath, 'r+')	
	content = newFile.readlines()
	for line in content:
		wordList = line.split()
		t = wordList[245]
		# this one will demonstrate the label, find a way to eliminate []
		u = wordList[248]
		v = u.split('[')
		w = v[1].split(']')
		y = w[0]
		# then use this for organizing the images.
		
		if y == '': 
			pathCheck1 = "/home/dmosuser/1.10.2/Reject"
			if os.path.isdir(pathCheck1):
				os.system("mv /home/dmosuser/1.10.2/" + str(t) +" /home/dmosuser/1.10.2/Reject")
			else: 
				os.system("mkdir Reject")
				os.system("mv /home/dmosuser/1.10.2/" +str(t) +" /home/dmosuser/1.10.2/Reject")
		
		#edit from this line till the end. 
		for item in xrange(27):
			z = T[item]
			if y == z: 
				pathChecking2 = "/home/dmosuser/1.10.2/" + str(y) +"/"	
				if os.path.exists(pathChecking2):
					os.system("mv /home/dmosuser/1.10.2/" + str(t) + " /home/dmosuser/1.10.2/" + str(y) +"/")
				else:
					os.system("mkdir " + str(y))
					os.system("mv /home/dmosuser/1.10.2/" + str(t) + " /home/dmosuser/1.10.2/" + str(y) +"/")		
		
		folderRemove_1 = '/home/dmosuser/1.10.2/results_folder/'
		#folderRemove_2 = '/home/dmosuser/1.10.2/musicData/'
		removeFiles(folderRemove_1)
		#removeFiles(folderRemove_2)
		pathMove = 'home/dmosuser/1.10.2/'
		fileMove(pathMove)