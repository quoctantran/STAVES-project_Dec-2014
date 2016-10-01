#!/usr/bin/env python 
#import module 
import os 

# Define output finename 
outputFileName = 'result_mezzo.test'

# Define path to input and output files 
inputPath = '/home/dmosuser/1.10.2/results_folder/'
outputPath = '/home/dmosuser/1.10.2/results_folder/'

# Convert forward/backward slashes
inputPath = os.path.normpath(inputPath)
outputPath = os.path.normpath(outputPath)

# Define output file and open for writing 
fileName = os.path.join(outputPath, outputFileName)
file_out = open(fileName, 'w')
print "Output file opened"

# Loop through each file in input directory 
for file in os.listdir(inputPath):
	# Define full filename
	fileName = os.path.join(inputPath, file)
	if fileName[len(fileName)-3:len(fileName)] == 'txt':
		if os.path.isfile(fileName):
			print " Adding :" + file
			file_in = open(fileName, 'r')
			content = file_in.read()
			file_out.write(content)
			file_in.close()
		
# Close output file 
file_out.close()
print "Output file closed "