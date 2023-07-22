import os
import shutil

fromDir = "D:/whitehat/class 102/classProject"
toDir = "D:/whitehat/class 102/classProject/"
listOfFiles = os.listdir(fromDir)

#print(listOfFiles)
for fileName in listOfFiles:
    name,extension = os.path.splitext(fileName)
    #print(name)
    #print(extension)
    if extension == "":
        continue
    if extension in [ '.txt', '.doc', '.docx', '.pdf']:
        path1 = fromDir+'/'+fileName
        path2 = toDir+'/'+'DocumentFiles'
        path3 = toDir+'/'+'DocumentFiles'+'/'+fileName
        #print(path1)
        #print(path2)
        #print(path3)
        if os.path.exists(path2):
            print('moving')    
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('moving')
            shutil.move(path1,path3)    