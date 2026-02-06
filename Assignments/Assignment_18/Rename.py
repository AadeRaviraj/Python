# Please follow below rules while designing automation script as
    # Accept input through command line or through file.
    # Display any message in log file instead of console.
    # For separate task define separate function.
    # For robustness handle every expected exception.
    # Perform validations before taking any action.
    # Create user defined modules to store the functionality.

# 2. Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extension.
# Usage: Directory Rename.py "Demo" ".txt" ".doc"
# Demo is name of directory and .txt is the extension that we want to search and rename with.doc.
# After execution this script each.txt file gets renamed as .doc.

import sys
import os
from pathlib import Path
def RenameFile(Dirname, exttxt, extdoc):
    
    border = "-" * 60 
    LogFileName = "RealeyeRenameLogFile.log"
    headerName = "------------------ Directory Automation --------------------"
    footerName = "------------------- Thank Your For Using  ------------------"

    
    fobj = open(LogFileName,"w")
    fobj.write(border +"\n")
    fobj.write(headerName + "\n")
    fobj.write(border + "\n")  
    
    for FolderName , SubFlderName, FileName in os.walk(Dirname):
        for fname in FileName:
            if exttxt in fname:
                
                oldpath = os.path.join(Dirname,fname)
                newpath =os.path.join(Dirname, Path(fname).stem + extdoc)
                
                os.rename(oldpath,newpath)
                print(f"File renamed {oldpath} to {newpath} \n ")
                fobj.write(f"File renamed {oldpath} to {newpath} \n ")
    
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
        
    RenameFile(sys.argv[1],sys.argv[2],sys.argv[3])
    
    print(border)
    print("-------------------- Thank Your For Using  -----------------")
    print(border)

if __name__ == "__main__":
    main()