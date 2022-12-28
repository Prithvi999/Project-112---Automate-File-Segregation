import os
import shutil
##os.getcwd()

from_dir = "C:/Users/kalya/Downloads"
to_dir = "C:/Users/kalya/Desktop"

list_of_files = os.listdir(from_dir)
##print(list_of_files)

extension = [ '.txt', '.doc', '.docx', '.pdf']

for files in list_of_files:
    root,ext = os.path.splitext(files)
    print("Root of the Path:", root, "Extension of the Path", ext)



    if ext == "":
        continue
    if ext in extension:
        path1 = from_dir+"/"+files
        path2 = to_dir + "/" + "Document_Files"
        path3 = to_dir + "/" + "Document_Files" + "/" + files
        print("Path 1", path1)
        print("Path 2", path2)
    if os.path.exists(path2):
        print("Moving"+ files+ "......")
        shutil.move(path1, path3)

    else:
        os.makedirs(path2)
        print("moving"+ files+ "......")
        shutil.move(path1, path3)



