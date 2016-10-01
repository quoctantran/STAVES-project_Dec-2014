import glob
import os, os.path
import sys
import subprocess

#folder = glob.glob("/udd/hongo/desktop/Full Dataset/Dataset 1/CHEVRONV")

#numberOfFile = len(folder)

#print (glob.glob("/udd/hongo/desktop/Full Dataset/Dataset 1/CHEVRONV"))

#for files in folder:
#	os.system("./a.out .Dataset\ 1\ /CHEVRONH" + files + "s > chevronh_" + files+ ".txt")

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
	for i in xrange(files - 1):
		os.system("./a.out CHEVRONV.000" + str(i) + "_result.png s > chevronv_" + str(i)+ ".txt")	

if __name__ == '__main__':
	engine("/home/dmosuser/1.10.2/CHEVRONV")
	main()

