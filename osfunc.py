import time , os , path , keyboard , getpass , requests , sys , threading , shutil
from subprocess import call



os.chdir(path.path)
os.chdir('usr')
#############
usrName = open('name','r').read()
usrPass = open('password','r').read()
##############
os.chdir(path.path)
os.chdir('downloads')
downloads = os.getcwd()
os.chdir(path.path)
os.chdir('Files')
Files = os.getcwd()
os.chdir(path.path)
###############

def restart():
    selection = choice()

    if selection == True:
        os.chdir(path.path)
        clr()
        os.system("kernel.py")
        sys.exit(0)
    
    else:
        print("Operation cancelled by user!")

def astatus():
    threading.Thread(os.chdir(path.path))
    threading.Thread(os.chdir('sysconfig'))
    activationStatus = open('activation','r').read()
    threading.Thread(os.chdir(path.path))
    return activationStatus


winclr = "cls"

def wait(seconds):
    time.sleep(seconds)

def clr():
    call(winclr,shell=True)

def bootAnim():
    print('.')
    wait(0.5)
    clr()
    print('..')
    wait(0.5)
    clr()
    print('...')
    wait(0.5)
    clr()
    print('....')
    wait(0.5)
    clr()
    print('.....')
    wait(0.5)
    print("OS Booted Successfully!")
    wait(0.5)
    clr()


def login(passwordReal):
    chkpass = getpass.getpass("Enter your password:")
    if chkpass != passwordReal:
        print("Invalid password!")
        login(passwordReal)
    else:
        return True


def CopyBytes():
    cdir = os.getcwd()
    fname = input("File name for file to be copied:")
    byte = open(fname,'rb').read()
    
    threading.Thread(os.chdir(path.path))
    threading.Thread(open("clipboard","wb").write(byte))
    threading.Thread(os.chdir(cdir))

def PasteClipb(bytes):
    fname = input("Enter new name for copied file:")
    try:
        open(fname,'ab').write(bytes)
    except:
        print("Clipboard is empty!!")

def choice() -> bool:
    print("[Y] to continue [N] to abort!")
    key = keyboard.read_key()
    if key == "y":
        return True

    elif key == "n":
        return False
    
    else:
        choice()

webinstall = ["webinstall" , "webdownload" , "wbd", "web"]

def webdownloadProcess():
    url = input("Enter url:")
    cdir = os.getcwd()
    try:
        f = requests.get(url)
        
        threading.Thread(os.chdir(downloads))
        fname = input("Enter name for the file:")
        threading.Thread(open(fname,'ab').write(f.content))
    except:
        print("Invalid URL!")
    
    os.chdir(cdir)

def createFile():
    fname = input("Enter new name for the file:")
    try:
        open(fname,'x')
    except:
        print("Specified file alreadys exists!")

def readFile():
    fname = input("Enter file name:")
    try:
        text = open(fname,"r").read()
        threading.Thread(print("***************START******************" +"\n"))
        threading.Thread(print(text+"\n"))
        threading.Thread(print("_________________END__________________"))
    except:
        print("Specified file does not exist!")

def chdir():
    dirname = input("Enter the directory name:")
    try:
        os.chdir(dirname)

    except:
        print("Specified directory not found!")

def newdir():
    cdir = os.getcwd()

    if cdir == path.path:
        print("Cannot create a directory in root system!")
        pass

    else:

        dirname = input("Enter new directory's name:")

        os.makedirs(os.getcwd() + "/" + dirname)

def removedir():
    cdir = os.getcwd()

    dirname = input("Enter name of the directory:")
    selection = choice()

    if cdir != path.path:
        if selection == True:
            try:
                shutil.rmtree(dirname)
                print("Directory deleted successfully!")
            except:
                print("Invalid directory!")
        
        else:
            print("Operation cancelled by user!")
    
    else:
        print("Cannot delete any folder in root directory!!")