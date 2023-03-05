import os
import getpass
from pathlib import Path
import shutil
import zipfile

print(getpass.getuser())
username = getpass.getuser()
basepath = '/home/' + username + '/'

# get all files and folders
entries = os.listdir(basepath)
p = Path(basepath + 'Documents/backup')
if p.exists():
    shutil.rmtree(p)
p.mkdir() 
for entry in entries:
	# check if entry is a filename
	if os.path.isfile(os.path.join(basepath, entry)):
            print(entry)
            shutil.copy(os.path.join(basepath, entry), p)
            
with zipfile.ZipFile(basepath + 'Documents/backup/backup.zip', 'w') as new_zip:
    for entry in entries:
        if os.path.isfile(os.path.join(basepath, entry)):
            new_zip.write(os.path.join(basepath, entry))             
# create folder /home/username/Documents/backup

