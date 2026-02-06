def DesignFun():
    border = "-" * 60 
    LogFileName = "LogFile.log"
    return border , LogFileName

def CheckDuplicateDeleteTime():
    border = "-" * 60 
    border1,LogFileName = DesignFun()
    print(LogFileName)
    print(border1)
    
def main():
    border = "-" * 60  


    # print(border)    
    # print("-------------------- Directory Automation ------------------")
    # print(border)
        
    CheckDuplicateDeleteTime()
            
    # print(border)
    # print("-------------------- Thank Your For Using  -----------------")
    # print(border)
    

if __name__ =="__main__":
    main()