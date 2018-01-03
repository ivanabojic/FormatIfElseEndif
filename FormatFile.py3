#Read a text file, format <if xxx><else></if> statements, write it with the _formated extension
#
# Expect files for formating to be in the same directory as this file
# Expect file with the list of files to format - FilesToFormat.txt to be in the same directory
# FilesToFormat.txt contains each file in the new line, at the beginning of the line
# sample:
#     10017.txt
#     10044.txt
#     10049.txt
#     10056.txt
#     10079.txt


import sys
import os

#def main():
#	filepath = sys.argv[1]
filepath = "FilesToFormat.txt" #"10044.txt"
outFile = filepath.replace(".txt","_formated.txt")

if not os.path.isfile(filepath):
	print("file path {} dose not exist. Exiting...".format(filepath))
	sys.exit

#read all file names 
with open(filepath, encoding='utf8') as filesToFormat:
	#read the whole file into a string
	fileNames = filesToFormat.read()

	#split file into lines and remove \n from the end
	fileNames = fileNames.splitlines().strip()

	#loops through all the files and formats them
	for file in fileNames:
		#generate output file name
		outFile = file.replace(".txt","_formatted.txt")

		#open the file
		if not os.path.isfile(file):
			print("file path {} dose not exist. Exiting...".format(file))
			sys.exit

		#read the whole file
		with open(file, encoding='utf8') as inFile:
			document = inFile.read()
	
			#prefix if, else, endif with new line
			document = document.replace('<IF','\n<if' )
			document = document.replace('<If','\n<if' )
			document = document.replace('<if','\n<if' )

			document = document.replace('<else>','\n<else>')
			document = document.replace('<ELSE>','\n<else>')
			document = document.replace('<Else>','\n<else>')

			document = document.replace('</IF>','\n</if>' )
			document = document.replace('</If>','\n</if>' )
			document = document.replace('</if>','\n</if>' )

			#split a string into array of lines
			docList = document.splitlines()

			#add indentation
			countIf = 0
			outDoc = ""

			for line in docList:
				if line.startswith("<if"):
					countIf += 1
					line = ' '*4*(countIf-1) + line
				elif line.startswith('</if>'):
					line = ' '*4*(countIf-1) + line
					countIf -= 1	    
				elif line.startswith('<else>'):
					line = ' '*4*(countIf-1) + line
				outDoc += line + '\n'

			file = open(outFile,"w") 
			file.write(outDoc) 	 
			file.close() 


