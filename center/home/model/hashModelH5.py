import hashlib
import os

def hashModel():
    # path = os.getcwd()
    SRC= './home/model/models/multiclass-1.h5'
    BLOCK_SIZE = 65536 # The size of each read from the file
    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish

    with open(SRC, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file

    result = file_hash.hexdigest()

    return result # Get the hexadecimal digest of the hash

def compareModel(server_hashcode, ana_hashcode):
    if server_hashcode == ana_hashcode:
        return True
    else:
        return False
    
# print(hashModel())