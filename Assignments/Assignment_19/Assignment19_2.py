# Please follow below rules while designing automation script as
    # Accept input through command line or through file.
    # Display any message in log file instead of console.
    # For separate task define separate function.
    # For robustness handle every expected exception.
    # Perform validations before taking any action.
    # Create user defined modules to store the functionality.

# 2. Design automation script which accept directory name and write names of duplicate files 
# from that directory into log file named as Log.txt. Log.txt file should be created into current directory.
# Usage: Directory Dusplicate.py "Demo"
# Demo is name of directory.



import os
import FileModule
import sys

def CheckDuplicate(DirName):
    
    retvalue = os.path.isdir(DirName)
    if retvalue != True:
        print("Directory Does bot exist...")
        return
    
    border = "-" * 60 
    LogFileName = "CheckDuplicateLogfile.log"
    headerName = "------------------ Directory Automation --------------------"
    footerName = "------------------- Thank Your For Using  ------------------"

    
    fobj = open(LogFileName,"w")
    fobj.write(border +"\n")
    fobj.write(headerName + "\n")
    fobj.write(border + "\n")  
    
    Dict1 = {}
    for Foldername, SubFoldername, Filename in os.walk(DirName):
        for Fname in Filename:
        
            result = FileModule.CheckSum(f"{DirName}/{Fname}")
            if result in Dict1:
                Dict1[result].append(Fname)
            else:
                Dict1[result] = [Fname]
            
            
            # fobj.write(f"File {Fname} Checksum value is : {result}\n")
        fobj.write(f"Duplicate files are  {Dict1} \n")

    
    fobj.write(border +"\n")
    fobj.write(footerName + "\n")
    fobj.write(border + "\n")

    

def main():
    border = "-" * 60  

    
    
    if len(sys.argv) > 2:
        print("Please pass only 2 arguments ")
        return
    elif(len(sys.argv) != 2):
        print("Please specify the directory name And file name....")
        return

    print(border)    
    print("-------------------- Directory Automation ------------------")
    print(border)
        
    CheckDuplicate(sys.argv[1])
            
    print(border)
    print("-------------------- Thank Your For Using  -----------------")
    print(border)
    

if __name__ =="__main__":
    main()

