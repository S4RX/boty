import glob
import os

shlyah = r'C:\pybot\Songs'
files_path = os.path.join(shlyah, '*')
files = sorted(
    glob.iglob(files_path), key=os.path.getctime, reverse=True)
#for i in range(len(files)):
#	files[i] = files[i].replace(shlyah , '')
print (files[0])