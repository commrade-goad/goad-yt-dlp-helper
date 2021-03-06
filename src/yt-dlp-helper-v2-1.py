from urllib.parse import urlparse
import os
print("================================")
print("   yt-dlp-helper by Goad V2.1   ")
print("================================")
print("Other options: 'exit' 'update'")
absoluteHomeFolder = os.path.expanduser("~")

def main():
    check = os.path.isfile("/usr/local/bin/yt-dlp")
    if check == True:
        checkconf = os.path.isfile(absoluteHomeFolder+"/"+"yt-dlp-helper.conf")
        if checkconf == False:
            f = open(absoluteHomeFolder+"/"+"yt-dlp-helper.conf", "w+")
            f.write("cwd1 = 1 \ncwd2 = 1 \nformat = 1 ")
            print("Config file created. Please relaunch the script.")
            exit()
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
    global cwd1Conf
    global cwd2Conf
    global formatConf
    global f
    n = -1
    cwd1Conf = False
    cwd2Conf = False
    formatConf = False
    listSet = []
    varConf = []
    f = open(absoluteHomeFolder+"/"+"yt-dlp-helper.conf", "r")
    for line in f:
        reader = line.split()
        try:
            listSet.append(reader[2])           # cwd1 = 0, cwd2 = 1, format = 2
            varConf.append(reader[0])
        except:
            print("Error reading config file. Config file will be rewritten.")
            os.remove(absoluteHomeFolder+"/"+"yt-dlp-helper.conf")
            main()

    for i in range(3):
        n = n + 1
        testVar = varConf[n]+listSet[n]
        if testVar == "cwd11":
            cwd1Conf = True
        elif testVar == "cwd21":
            cwd2Conf = True
        elif testVar == "format1":
            formatConf = True

def vidSourcenOptions():
    global link
    link=str(input("Source / options : "))
    updateOptions = ['update','UPDATE', 'Update']
    exitOptions = ['exit', 'EXIT', 'Exit']
    exitcheck = link in exitOptions
    updatecheck = link in updateOptions
    urlcheck = urlparse(link)
    urlcheckbol = (all([urlcheck.scheme, urlcheck.netloc, urlcheck.path])
                    and len(urlcheck.netloc.split(".")) > 1)
    if urlcheckbol == True:
        if cwd1Conf == True:
            dirPrinting()
            whereToSave()
        else:
            whereToSave()
    else :
        if exitcheck == True:
            exit()
        elif updatecheck == True:
            print(" >> Running Command : sudo yt-dlp -U")
            os.system("sudo yt-dlp -U")
            vidSourcenOptions()
        else:
            print("Not a valid url or commands!")
            vidSourcenOptions()

def whereToSave():
    where=str(input("Path : "))
    dircheck=os.path.isdir(where)
    if dircheck == False:
        print("Directory '"+where+"' doesn't exist.")
        print("Maybe this will help :\n", os.listdir())       
        whereToSave()
    else:
        os.chdir(where)
        ytdlpCommand()

def ytdlpCommand():
    if formatConf == True:
        os.system("yt-dlp -F "+link) 
    else:
        pass
    if cwd2Conf == True:
        dirPrinting()
    else:
        pass
    what=str(input("Select Format (example: 137+140): "))
    os.system("yt-dlp -f "+what+" "+link)

def dirPrinting():
    print("Current Working Directory is '",os.getcwd(),"'")

main()
f.close()
