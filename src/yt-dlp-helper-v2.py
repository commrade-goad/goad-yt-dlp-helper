from urllib.parse import urlparse
import os
import time
print("================================")
print("   yt-dlp-helper by Goad V2.0   ")
print("================================")
print("Other options: 'exit' 'update'")
homefolder = "~"
absoluteHomeFolder = os.path.expanduser(homefolder)

def main():
    check = os.path.isfile("/usr/local/bin/yt-dlp")
    if check == True:
        checkconf = os.path.isfile(absoluteHomeFolder+"/"+"yt-dlp-helper.conf")
        if checkconf == False:
            print("Creating config file...")
            f = open(absoluteHomeFolder+"/"+"yt-dlp-helper.conf", "w+")
            f.write("cwd1 = 1\ncwd2 = 1\nformat = 1")
        readTheConfigFile()
        vidSourcenOptions()
    else:
        install=input("yt-dlp is not installed. Do you want to install it? (y/n) : ")
        if install == "y":
            print("sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && sudo chmod a+rx /usr/local/bin/yt-dlp")
            install=input("you will execute the  command from above, do you want to proceed? (y/n) : ")
            if install == "y":
                os.system("sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && sudo chmod a+rx /usr/local/bin/yt-dlp")
                main()
            else:
                exit()
        else:
            exit()

def readTheConfigFile():
    global listSet
    listSet = []
    f = open(absoluteHomeFolder+"/"+"yt-dlp-helper.conf", "r")
    for line in f:
        reader = line.split()
        try:
            listSet.append(reader[2]) # cwd1 = 0, cwd2 = 1, format = 2
        except:
            print("Error reading config file.")
            print("Please delete the config file at '~/yt-dlp-helper.conf' and restart the program!")
            exit()
def vidSourcenOptions():
    global link
    link=str(input("Source / options : "))
    updateOptions = ['update','UPDATE', 'Update']
    exitOptions = ['exit', 'EXIT', 'Exit']
    exitcheck = link in exitOptions
    updatecheck = link in updateOptions
    if exitcheck == True:
        exit()
    elif updatecheck == True:
        print(" >> Running Command : sudo yt-dlp -U")
        os.system("sudo yt-dlp -U")
        vidSourcenOptions()
    else:
        urlcheck = urlparse(link)
        urlcheckbol = (all([urlcheck.scheme, urlcheck.netloc, urlcheck.path])
                        and len(urlcheck.netloc.split(".")) > 1)
        if urlcheckbol == False :
            print("Not a valid url or commands!")
            vidSourcenOptions()
        else:
            if listSet[0] == '0':
                whereToSave()
            else:
                dirPrinting()
                whereToSave()

def whereToSave():
    where=str(input("Path : "))
    dircheck=os.path.isdir(where)
    if dircheck == False:
        print("Directory '"+where+"' doesn't exist.")
        whereToSave()
    else:
        os.chdir(where)
        ytdlpCommand()

def ytdlpCommand():
    if listSet[2] == '1':
        os.system("yt-dlp -F "+link) # add "#" at the start of the line to disable format printing
    else:
        pass
    if listSet[1] == '1':
        dirPrinting()
    else:
        pass
    what=str(input("Select Format (example: 137+140): "))
    os.system("yt-dlp -f "+what+" "+link)

def dirPrinting():
    print("Current Working Directory is '",os.getcwd(),"'")

main()
f.close()
