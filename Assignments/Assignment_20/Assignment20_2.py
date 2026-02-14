    # Please follow below rules while designing automation script as
    # Accept input through command line or through file.
    # Display any message in log file instead of console.
    # For separate task define separate function.
    # For robustness handle every expected exception.
    # Perform validations before taking any action.
    # Create user defined modules to store the functionality.
    # Please add below features in our project named as Platform Surveillance System

# 2. Add Open Files Monitoring Feature
# For each process, display:
# Number of files opened by the process
# Requirement
# Count open file descriptors using system/library calls
# Handle permission errors properly
# Mention "Access Denied" in log if required

import psutil 
import time   



def ProcessScan(): 
    listProces = [] 
    # warm up CPU percent
    for  proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass
    time.sleep(0.2)
    
    
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid","name","username","status","create_time"])
            # Convert create_time 
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(info["create_time"]))
            except:
                info["create_time"] ="N/A"

            # CPU & Memory
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            
            # Memory details
            mem_info = proc.memory_info()
            info["rss"] = mem_info.rss
            info["vms"] = mem_info.vms
            
            # Threads
            info["threads"] = proc.threads()
            info["num_threads"] = proc.num_threads()
            
            # Open files (Windows)
            try:
                info["open_files"] = proc.num_handles()
            except:
                info["open_files"] = "Access Denied"
            
             
            listProces.append(info)
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) :
            pass
    return listProces
    
def main():
    Border = "-" * 60

    LogFileName = "LogfileName.log"
    fobj = open(LogFileName,"w")
    fobj.write(Border+"\n")
        
    Data = ProcessScan()
    fobj.write("\n-------------------- File monitoring q2 --------------------\n")
    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("Open files %s:\n" %info.get("open_files"))
        fobj.write(Border+"\n")
    fobj.write(Border+"\n")


if __name__ == "__main__":
    main()