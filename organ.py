import os
import shutil
#function to organize file
def organize(floder_path):
    files=[f for f in os.listdir(floder_path) if os.path.isfile(os.path.join(floder_path,f))]
    for file in files:
        floder_name=os.path.splitext(file)[1][1:].upper()+"_files"
        if not os.path.exists(os.path.join(floder_path,floder_name)):
                              os.makedirs(os.path.join(floder_path,floder_name))
        shutil.move(os.path.join(floder_path,file),os.path.join(floder_path,floder_name,file))
    print("file organisation complete")
floder_path=input("Enter the path:")
organize(floder_path)
