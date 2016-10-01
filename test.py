import glob
import os, os.path
import sys

#os.getcwd()

#print os.getcwd()

#def count_em(valid_path):
#	x = 0
#	for root, dirs, files in os.walk(valid_path):
#		for f in files:
##	print "There are " + str(x) + " files in this directory"
#	return x
#		
#count_em("/Users/minhngo/Desktop/Dataset/Music/")

def main():
	if len(sys.argv) - 1:
		engine(''.join(sys.argv[1:]))
	else:
		print os.path.basename(sys.argv[0]), '<directory>'
		
def engine(path):
	directories = files = 0
	for information in os.walk(path):
		directories += len(information[1])
		files += len(information[2])
	print 'Directories =', directories
	print 'Files =', files

if __name__ == '__main__':
#	engine("/Users/minhngo/Desktop/Music/CHEVRONV")
	main()
	
## need more lines of code for loading the ./a.out to execute the extraction
## the problem is because the current working folder is 1.10.2 but 
## the images stay in the sub-folders of this main one. 

## suggested solution: try the option

if os.path.exists("path")
	f = open(path, 'option')