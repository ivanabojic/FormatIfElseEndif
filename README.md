# FormatIfElseEndif
Format If-Else-Endif statements in rtf template file

At the moment conversion from rtf to text file is manual.
Current script formats the txt files. 

Script and files to be formated resides in the same directory.
         
Create FilesToFormat.txt with the list of all the files that need to be formated, each file name in the new line. Sample FilesToFormat.txt provided.
  
To format run from a command line:
         python FormatFile.py3
         
Example: 
 3 rtf files to be formatted: name1.rtf, name2.rtf, name3.rtf
 Cut and paste them to the text files: name1.txt, name2.txt, name3.txt
 Create FilesToFormat.txt
      name1.txt
      name2.txt
      name3.txt
 
 Put the script FormatFile.py3 in the same directory where all the files are and run it.
 
 Following formatted files will be created:
     name1_formatted.txt
     name2_formatted.txt
     name3_formatted.txt
