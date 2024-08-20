import os
import shutil
#function to organize file
def organize(floder_path):
    files=[f for f in os.listdir(floder_path) if os.path.isfile(os.path.join(floder_path,f))]

    #create floders
    for file in files:
        
        file_extention=os.path.splitext(file)[1][1:]
        floder_name=file_extention.upper()+"_files"
        #create floder if it doesn`t exist
        if not os.path.exists(os.path.join(floder_path,floder_name)):
                              os.makedirs(os.path.join(floder_path,floder_name))

        #move the file to the respective floder
        shuil.move(os.path.join(floder_path,file),os.path.join(floder_path,floder_name,file))
    print("file organisation complete")

floder_path="D:\Java"
organize(floder_path)
