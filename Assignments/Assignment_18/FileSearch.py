# Please follow below rules while designing automation script as
    # Accept input through command line or through file.
    # Display any message in log file instead of console.
    # For separate task define separate function.
    # For robustness handle every expected exception.
    # Perform validations before taking any action.
    # Create user defined modules to store the functionality.
    
# 1. Design automation script which accept directory name and file extension from user. Display all files with that extension.
# Usage: Directory FileSearch.py "Demo" ".txt"
# Demo is name of directory and .txt is the extension that we want to search.


import os
import sys
def findFile(Dirname,fileExtension):
    border = "-" * 60 
    LogFileName = "RealeyeLogFile.log"
    headerName = "------------------ Directory Automation --------------------"
    footerName = "------------------- Thank Your For Using  ------------------"

    
    fobj = open(LogFileName,"w")
    fobj.write(border +"\n")
    fobj.write(headerName + "\n")
    fobj.write(border + "\n")  
    
    
    for FolderName , SuBFolderName, FileName in os.walk(Dirname):
        for Fname in FileName:
            if  fileExtension in Fname :
                print(f"Total Files of {fileExtension} extension are  : ", Fname)
                fobj.write(f"Total Files of {fileExtension} extension are  :  {Fname}\n")
    
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
        
    findFile(sys.argv[1],sys.argv[2])
    
    print(border)
    print("-------------------- Thank Your For Using  -----------------")
    print(border)



if __name__ == "__main__":
    main()