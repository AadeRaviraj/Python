# Please follow below rules while designing automation script as
    # Accept input through command line or through file.
    # Display any message in log file instead of console.
    # For separate task define separate function.
    # For robustness handle every expected exception.
    # Perform validations before taking any action.
    # Create user defined modules to store the functionality.


# 4. Design automation script which accept two directory names and one file extension. 
# Copy all files with the specified extension from first directory into second directory.
# Second directory should be created at run time.
# Usage: Directory CopyExt.py "Demo" "Temp" ".exe"
# Demo is name of directory which is existing and contains files in it. 
# We have to create new Directory as Temp and copy all files with extension .exe from Demo to Temp.

import sys
import os
import shutil
def DirCopySpecificFile(Dirname1,Dirname2,extname):
            
    border = "-" * 60 
    LogFileName = "CopyExeLogFile.log"
    headerName = "------------------ Directory Automation --------------------"
    footerName = "------------------- Thank Your For Using  ------------------"

    
    fobj = open(LogFileName,"w")
    fobj.write(border +"\n")
    fobj.write(headerName + "\n")
    fobj.write(border + "\n")  
    
    
    Ret  = os.path.exists(Dirname2)
    if Ret == True:
        print(f"{Dirname2} is already exist..")
        fobj.write(f"{Dirname2} is already exist..\n")
        
        
        for FolderName , SuBFolderName, FileName in os.walk(Dirname1):
            for Fname in FileName:
                if  extname in Fname :
                    print(Fname)
                    shutil.copy(f"{Dirname1}/{Fname}",Dirname2)
                    print(f"Demo Directory {extname} extension are  : ", Fname)
                    fobj.write(f"Demo Directory {extname} extension are  :  {Fname}\n")  
                    print(f"'{Dirname1}' .exe Files Copied to '{Dirname2}' successfully\n")                  
                    fobj.write(f"'{Dirname1}' .exe Files Copied to '{Dirname2}' successfully\n")
    else:
        print(f"{Dirname2} is not exist we will create it ")
        fobj.write(f"{Dirname2} is not exist we will create it \n")
        
        os.makedirs(Dirname2) 
        print(f"{Dirname2} is created ")
        fobj.write(f"{Dirname2} is created \n")
        
        
        for FolderName , SuBFolderName, FileName in os.walk(Dirname1):
            for Fname in FileName:
                if  extname in Fname :
                    shutil.copy(f"{Dirname1}/{Fname}",Dirname2)
                    print(f"Demo Directory {extname} extension are  : ", Fname)
                    fobj.write(f"Demo Directory {extname} extension are  :  {Fname}\n")
                    print(f"'{Dirname1}' .exe Files Copied to '{Dirname2}' successfully\n")
                    fobj.write(f"'{Dirname1}' .exe Files Copied to '{Dirname2}' successfully\n")
        
    fobj.write(border +"\n")
    fobj.write(footerName + "\n")
    fobj.write(border + "\n")
    

def main():
    
    border = "-" * 60      
    
    if len(sys.argv) > 4:
        print("Please pass only 3 arguments ")
        return
    elif(len(sys.argv) != 4):
        print("Please specify the directory name And file name....")
        return

    print(border)    
    print("-------------------- Directory Automation ------------------")
    print(border)
        
    DirCopySpecificFile(sys.argv[1],sys.argv[2],sys.argv[3])
    
    print(border)
    print("-------------------- Thank Your For Using  -----------------")
    print(border)
    
    

if __name__ =="__main__":
    main()
