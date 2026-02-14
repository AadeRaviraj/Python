# Please follow below rules while designing automation script as
# Accept input through command line or through file.
# Display any message in log file instead of console.
# For separate task define separate function.
# For robustness handle every expected exception.
# Perform validations before taking any action.
# Create user defined modules to store the functionality.
# Please add below features in our project named as Platform Surveillance System


# 3. Add Actual Memory Allocation Feature
# Display real memory usage of each process:
# RSS (Resident Set Size-actual RAM used)
# . VMS (Virtual Memory)
# Memory Percentage
# Requirement
# Show:
# Top 10 memory consuming processes 
import psutil
import time

def RealmemoryUse():
    top10usage = []
    for  proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass
    time.sleep(0.2)
    for  proc in psutil.process_iter():
        try:
            # print(proc.memory_info().rss  )
            
            top10usage.append(proc.memory_info().rss)
            
        except:
            pass
    
    print(f"Ram usage : {psutil.virtual_memory().percent}")       
        
    top10usage.sort()
    top10 = 10
    print(f"Top 10 memory use : {top10usage[-top10:]}") 
    # process = psutil.Process()
    # print(process.memory_info().rss / 1024 ** 2 )


RealmemoryUse()