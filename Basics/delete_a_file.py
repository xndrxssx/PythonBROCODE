import os
import shutil

path = "test.txt"

try:
    #os.remove(path)
    #os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")