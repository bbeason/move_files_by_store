import os
import shutil

path = "/Users/bobbybeason/Desktop/Work Scripts/"

names = os.listdir(path)
folder_name = ['Houston', 'Conroe', 'TexasCity', 'Cleveland', 'DCC1', 'DCC2', 'Northside']
for x in range(0, 7):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])
for files in names:
    if "houston" in files and not os.path.exists(path+'Houston/'+files):
        shutil.move(path+files, path+'Houston/'+files)
    if "conroe" in files and not os.path.exists(path+'Conroe/'+files):
        shutil.move(path+files, path+'Conroe/'+files)
    if "texas" in files and not os.path.exists(path + 'TexasCity/' + files):
        shutil.move(path + files, path + 'TexasCity/' + files)
    if "cleveland" in files and not os.path.exists(path + 'Cleveland/' + files):
        shutil.move(path + files, path + 'Cleveland/' + files)
    if "dcc1" in files and not os.path.exists(path+'DCC1/'+files):
        shutil.move(path+files, path+'DCC1/'+files)
    if "dcc2" in files and not os.path.exists(path+'DCC2/'+files):
        shutil.move(path+files, path+'DCC2/'+files)
    if "northside" in files and not os.path.exists(path+'Northside/'+files):
        shutil.move(path+files, path+'Northside/'+files)


print("Files moved")

