import glob, os

path = "./export"

root = [f for f in os.listdir(path) if not f.startswith('.')]
F = open('import.mapfile','w')
for folder in root:
    H = open(os.path.join(path, folder, 'handle'), 'r')
    F.write(folder + " " + H.readline())
    print(folder + " " + H.readline())
    H.close()
F.close()