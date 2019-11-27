import os
for root, dirs, files in os.walk("./Academic-Projects"):
    for file in files:
        if file.endswith(".c"):
             print(os.path.join(root, file))