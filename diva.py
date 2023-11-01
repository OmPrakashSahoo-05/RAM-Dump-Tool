import os
import shutil
import platform

# username = os.getlogin()
os_name = platform.system()
# print(username)

extension = ".dmp"
folder_name = "Dumps"

if os_name == "Linux":
    username = os.getlogin()
    directory = "/home/" + username + "/"

elif os_name == "Windows":
    directory = "C:\\Users\\"

elif os_name == "Darwin":
    username = os.getlogin()
    directory = "/Users/username/"

# Printing the names of all dump files in system

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(extension):
            print(os.path.join(root, file))

# Create a new directory to store the dump files

try:
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                # copy the dump file to the new directory
                shutil.copy2(os.path.join(root, file),
                             os.path.join(folder_name, file))

except shutil.SameFileError:
    pass
