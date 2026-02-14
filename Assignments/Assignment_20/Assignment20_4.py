    # Please follow below rules while designing automation script as
    # Accept input through command line or through file.
    # Display any message in log file instead of console.
    # For separate task define separate function.
    # For robustness handle every expected exception.
    # Perform validations before taking any action.
    # Create user defined modules to store the functionality.
    # Please add below features in our project named as Platform Surveillance System



# 4. Add Periodic Email Reporting Feature
# Automatically send system report through email at regular intervals.
# Email must contain:
# Log file attachment
# Summary of:
# Total processes
# Top CPU usage processes
# Top Memory usage processes
 
# Top Thread count processes
# Top Open file processes
# Usage
# PlatformSurveillance.py "MarvellousLogs" "receiver@gmail.com"
# 10
# Where:
# MarvellousLogs →→ log folder
# receiver@gmail.com receiver mail
# 10 interval in minutes

# Expected Output in Log File
# Each process entry should include:
# Process Name
# PID
# CPU %
# Memory (RSS)
# Threads Count
# Open Files Count
# Timestamp