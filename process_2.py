import glob
import os, os.path
import sys
import subprocess
import re

def main():
	if len(sys.argv) - 1:
		engine(''.join(sys.argv[i:]))
	else:
		print os.path.basename(sys.argv[0]), '<directory>'
	
def engine(path):
	directories = files = 0
	for information in os.walk(path):
		directories += len(information[1])
		files += len(information[2])
	print 'Directories = ', directories
	print 'Files = ', files
	
	#if we can detect the image file name, without extension
	#we can use this name for execution with ./a.out 
	#
	for i in xrange(files - 1):
		os.system("./a.out image_" + str(i+1) + ".png s > image_" + str(i+1)+ ".txt")
		#os.system("mv image_"+str(i+1)+".txt /home/dmosuser/1.10.2/results_folder/")
		
		currentPath = "/home/dmosuser/1.10.2/image_" + str(i+1)+".txt"
		
		file_in = open(currentPath, 'r+')
		content = file_in.readlines()
		file_out = open(currentPath, 'w')
		
		for line in content: 
			line_bis = ' '
			for char in line:
				if char == 's':
					line_bis =  line_bis + ' s, ' + str(i+1) + ', amin'
				else:
					line_bis += char
			file_out.writelines(line_bis)
			
		os.system("mv image_"+str(i+1)+".txt /home/dmosuser/1.10.2/results_folder/")
def findWholeWord(w):
	return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search	


if __name__ == '__main__':
	engine("/home/dmosuser/1.10.2/76")
	main()
	os.system("python combine.py" )
	
	os.system("./bonzaiboost -S first -boost adamh -n 5")
	#proc_2 = subprocess.Popen(["./bonzaiboost -S fileName -n 5 - d 2 -C - c single <output.test> result.text"], stdout = subprocess.PIPI, shell = true)
	#(outputFile1, err) = proc_2.communicate();
	
	os.system("./bonzaiboost -S first -boost adamh -n 5 -C -c single <result.data> testResult.txt")
	
	resultPath = "/home/dmosuser/1.10.2/testResult.txt"
	
	#print resultPath
	
	inputFile = open(resultPath, 'r+')
	contentBonzai = inputFile.readlines()
	outputFile = open(resultPath, 'w')	
	
	T = ['amin', 'becarre', 'bemol','diese','dmsoupir']
	#m = T.size()
	keyword = ',s ,'
	#result = []
	
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
		print wordList[245]

#		for t in xrange(m)
#			item = T[t]
#			if findWholeWord((item)(line)):
#				pathChecking = "/home/dmosuser/1.10.2/" + str(item)
#				if os.path.exists(pathChecking)
#					os.system("mkdir" + T.items())
#					
#				#for line i in number of lines, move file txt to corresponding folder
#				#toi day use result [0]
#				
#					os.system("move" + "origninal folder" + "destination folder")
#				else:
#					os.system("move" + "origninal folder" + "destination folder")
#			if findWholeWord(('[]')(line)):
#				pathChecking = "home/dmosuser/Reject"
#				if os.path.exists(pathChecking)
#					os.system("mkdir Reject")
#					os.system("move" + "original folder" + "destination folder")
#				else: 
#					os.system ("move" + "original folder" + pathChecking)
				
	#os.system("./bonzaiboost -S fileName -n 5 - d 2 -C - c single <output.test> result.text")
