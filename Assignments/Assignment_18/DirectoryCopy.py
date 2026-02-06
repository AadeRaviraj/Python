# Please follow below rules while designing automation script as
    # Accept input through command line or through file.
    # Display any message in log file instead of console.
    # For separate task define separate function.
    # For robustness handle every expected exception.
    # Perform validations before taking any action.
    # Create user defined modules to store the functionality.


# 3. Design automation script which accept two directory names.
# Copy all files from first directory into second directory. Second directory should be created at run time.
# Usage: DirectoryCopy.py "Demo" "Temp"
# Demo is name of directory which is existing and contains files in it.
# We have to create new Directory as Temp and copy all files from Demo to Temp.

import sys
import shutil
import os

def DirectoryCopy(DirName1, DirName2):
        
    border = "-" * 60 
    LogFileName = "RealeyeRenameLogFile.log"
    headerName = "------------------ Directory Automation --------------------"
    footerName = "------------------- Thank Your For Using  ------------------"

    
    fobj = open(LogFileName,"w")
    fobj.write(border +"\n")
    fobj.write(headerName + "\n")
    fobj.write(border + "\n")  
    
    Ret  = os.path.exists(DirName2)
    if Ret == True:
        print(f"{DirName2} is already exist..")
        fobj.write(f"{DirName2} is already exist..\n")
        shutil.copytree(DirName1,DirName2,dirs_exist_ok= True) #https://docs.python.org/3/library/shutil.html
        print(f"'{DirName1}' Data Copied to '{DirName2}' successfully")
        fobj.write(f"'{DirName1}' Data Copied to '{DirName2}' successfully\n")
    else:
        print(f"{DirName2} is not exist we will create it ")
        fobj.write(f"{DirName2} is not exist we will create it \n")
        
        os.makedirs(DirName2) 
        print(f"{DirName2} is created ")
        fobj.write(f"{DirName2} is created \n")
        shutil.copytree(DirName1,DirName2,dirs_exist_ok= True) #https://docs.python.org/3/library/shutil.html
        print(f"'{DirName1}' Data Copied to '{DirName2}' successfully")
        fobj.write(f"'{DirName1}' Data Copied to '{DirName2}' successfully\n")
        
    
    fobj.write(border +"\n")
    fobj.write(footerName + "\n")
    fobj.write(border + "\n")

    
    
def main():
    
    border = "-" * 60  

    
    
    if len(sys.argv) > 3:
        print("Please pass only 2 arguments ")
        return
    elif(len(sys.argv) != 3):
        print("Please specify the directory name And file name....")
        return

    print(border)    
    print("-------------------- Directory Automation ------------------")
    print(border)
        
    DirectoryCopy(sys.argv[1],sys.argv[2])
    
    print(border)
    print("-------------------- Thank Your For Using  -----------------")
    print(border)
    
    

if __name__ == "__main__":
    main()

