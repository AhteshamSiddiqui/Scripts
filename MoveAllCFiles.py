import os
import shutil
for root, dirs, files in os.walk("./temp"):
    for file in files:
        if file.endswith(".c"):
             print(os.path.join(root, file))
             shutil.move((os.path.join(root, file)),'All_C_Files')