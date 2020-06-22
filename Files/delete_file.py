""" Delete a File"""
import os

os.remove('demofile.txt')

""" Check if File exist:"""

if os.path.exists('demofile2.txt'):
    os.remove('demofile2.txt')
else:
    print("File Not Existed")

""" Delete Folder """

os.rmdir('myfolder')
