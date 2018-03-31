import glob, os, sys
from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image, ImageFile

path = "./export"

root = [f for f in os.listdir(path) if not f.startswith('.')]
for folder in root:
    currentPath = path + "/" + folder
    print ("current folder: " + currentPath)
    #print os.listdir(currentPath)
    for file in os.listdir(currentPath):
        if file.endswith(".pdf"):
            currentPDFFile = os.path.join(currentPath, file)
            print(currentPDFFile)
            currentPage = 1
            for jpegs in convert_from_path(currentPDFFile):
                saveTo = '.' + str(currentPDFFile).split('.')[1] + "-" + str(currentPage).zfill(2) + ".jpeg"
                jpegs.save(saveTo, format='JPEG', quality=100)
                print(saveTo)
                currentPage += 1
            print
    print
print