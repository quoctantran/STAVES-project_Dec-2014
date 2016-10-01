#!/usr/bin/env python 
#import module 
import os 
import re

# Define input and output finename  
outputFileName = 'diese-svm.txt'

# Define path to input and output files 
inputPath = '/Users/minhngo/Desktop/Collection'
outputPath = '/Users/minhngo/Desktop/Collection'

# Convert forward/backward slashes
inputPath = os.path.normpath(inputPath)
outputPath = os.path.normpath(outputPath)
# Define input file 
print inputPath

# Define output file and open for writing 
fileName = os.path.join(outputPath, outputFileName)
file_out = open(fileName, 'w')
print "Output file opened"

# Loop through each line in the input file
#f = open (inputFileName)
#f.seek(0)
#f.readline()

for file in os.listdir(inputPath):
	# get the file's name without extension
	#coreName = str(file).replace('.txt', '')
	
	# get the path for input file and
	# then get the name without extension
	# for creating the svm data version of the input file 
	
	fileName = os.path.join(inputPath, file)
	print 'fileName = ', fileName
	#print inputFileWithoutExtension
	
	# output file information
	#outputFileName =  inputFileWithoutExtension + '-svm.txt'
	#outFileName = os.path.join(outputPath, outputFileName)
	#file_out = open(outFileName, 'w')
	
	# create the corresponding output file 
	# first - check the type of the input file: txt 
	
	if fileName[len(fileName)-3:len(fileName)] == 'txt':
		if os.path.isfile(fileName):
			file_in = open(fileName, 'r+')
			content = file_in.readlines()
			#print 'XXXXXXXXXXXXXX',content[0]
			#print 'YYYYYYYYYYYYYY',content[1]
			
			for line in content:
				print len(line)
				counting = 2
				line_bis = 'diese 1: '
				for char in line:
					if char == ',':
						line_bis = line_bis + str(counting) + ':'
						counting+=1
					else:
						line_bis += char
				file_out.writelines(line_bis)			

# Close output file 
file_out.close()
print "Output file closed "