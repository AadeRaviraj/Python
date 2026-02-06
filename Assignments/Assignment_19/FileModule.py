import hashlib
def CheckSum(FileName):
    fobj = open(FileName,"rb")
    
    hobj = hashlib.md5()
    
    buffer = fobj.read(1024)
    
    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fobj.read(1024)
    
    fobj.close()
    return hobj.hexdigest()

