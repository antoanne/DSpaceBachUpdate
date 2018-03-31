import glob, os

path = "./export"

root = [f for f in os.listdir(path) if not f.startswith('.')]
for folder in root:
    currentPath = path + "/" + folder
    print ("current folder: " + currentPath)
    contentsFile = [f for f in os.listdir(currentPath) if f == 'contents']
    for c in contentsFile:
        currentContentsPath = os.path.join(currentPath, c)
        print(currentContentsPath)
        for j in glob.glob(currentPath + "/*.jpeg"):
            currentJPEGFileName = j.split('/')[-1] + '	bundle:ORIGINAL'
            print(currentJPEGFileName)
            F = open(currentContentsPath,'r')
            listF = F.readlines()
            print(listF)
            F.close()
            checkHas = False
            for fileOfList in listF:
                if fileOfList.startswith(currentJPEGFileName):
                    print('existe')
                    checkHas = True
            if not checkHas:
                F = open(currentContentsPath,'a')
                F.write(currentJPEGFileName + '\n')
                F.close()
                print('ADD')
    print()