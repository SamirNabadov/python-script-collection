#!/usr/bin/python3.8
from zipfile import ZipFile

def main():

    print('Extract all files in ZIP to current directory')
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile('E:\\samir\\devops\\python\\scripts\\kube.zip', 'r') as zipObj:
       # Extract all the contents of zip file in current directory
       zipObj.extractall()

    print('Extract all files in ZIP to different directory')
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile('sampleDir.zip', 'r') as zipObj:
       # Extract all the contents of zip file in different directory
       zipObj.extractall('temp')

    print('Extract single file from ZIP')
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile('E:\\samir\\devops\\python\\scripts\\kube.zip', 'r') as zipObj:
       # Get a list of all archived file names from the zip
       listOfFileNames = zipObj.namelist()
       # Iterate over the file names
       for fileName in listOfFileNames:
           # Check filename endswith csv
           if fileName.endswith('.csv'):
               # Extract a single file from zip
               zipObj.extract(fileName, 'E:\\samir\\devops\\python\\scripts\\kube_zip_folder')

if __name__ == '__main__':
   main()
