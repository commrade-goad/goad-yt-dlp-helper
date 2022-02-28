from urllib.parse import urlparse
import os
print("================================")
print("   yt-dlp-helper by Goad V2.3   ")
print("================================")
print("Other options: 'exit' 'update' 'new'")
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
    n1 = -1
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
        n1 = n1 + 1
        testVar = varConf[n1]+listSet[n1]
        if testVar == "cwd11":
            cwd1Conf = True
        elif testVar == "cwd21":
            cwd2Conf = True
        elif testVar == "format1":
            formatConf = True

def vidSourcenOptions():
    global link
    global count
    link=str(input("Source / options : "))
    updateOptions = ['update','UPDATE', 'Update']
    exitOptions = ['exit', 'EXIT', 'Exit']
    urlcheckbolList = []
    countVid= link.count(";")
    link = link.split("; ")
    count = countVid + 1
    n = -1
    for i in range(0, count):
        n = n + 1
        urlcheck = urlparse(link[n])
        urlcheckbol = (all([urlcheck.scheme, urlcheck.netloc, urlcheck.path])
                        and len(urlcheck.netloc.split(".")) > 1)
        urlcheckbolList.append(urlcheckbol)

    if False in urlcheckbolList :
        exitcheck = link[0] in exitOptions
        updatecheck = link[0] in updateOptions
        newFcheck = "new" in link[0]
        if exitcheck == True:
            exit()
        elif updatecheck == True:
            print(" > Running Command : sudo yt-dlp -U")
            os.system("sudo yt-dlp -U")
            vidSourcenOptions()
        elif newFcheck == True:
            print("New Feature :\n Version 2.2 : Now you can download more than one video in one go. Type '; ' at the end of the link and follow by another link.\n Version 2.3 : Tidy up some of the code and adding download all the same format options.")
            vidSourcenOptions()
        else:
            print("Not a valid url or commands!")
            vidSourcenOptions()
    else:
        if cwd1Conf == True:
            dirPrinting()
            whereToSave()
        else:
            whereToSave()

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
    sameFormat = False
    formatList=[]
    if formatConf == True:
        n = -1
        vidNumber = 0
        for i in range(0, count):
            n = n + 1
            vidNumber = vidNumber+1
            print(" > Format of Video no",vidNumber)
            os.system("yt-dlp -F "+link[n])
    else:
        pass
    if cwd2Conf == True:
        dirPrinting()
    else:
        pass
    vidNumber = 0
    for i in range(0, count):
        vidNumber = vidNumber+1
        print(" > Select Format for Video no",vidNumber)
        what=str(input("Type 'all' to select the same format for all Videos\nSelect Format (example: 137+140): "))
        formatList.append(what)
        if "all" in formatList:
            if count == 1:
                sameFormat = False
                print("You are Downloading only one video no need to use the all flag.")
                ytdlpCommand()
            else:
                sameFormat = True
                what=str(input("Select Format for all Videos (example: 137+140): "))
                formatList.append(what)
                break
        else:
            pass
    n = -1
    vidNumber = 0
    if sameFormat == False:
        for i in range(0, count):
            n = n + 1
            vidNumber = vidNumber+1
            print(" > Downloading Video no",vidNumber)
            os.system("yt-dlp -f "+formatList[n]+" "+link[n])
    else:
        for i in range(0, count):
            n = n + 1
            vidNumber = vidNumber+1
            print(" > Downloading Video no",vidNumber)
            os.system("yt-dlp -f "+formatList[1]+" "+link[n])

def dirPrinting():
    print("Current Working Directory is '",os.getcwd(),"'")

main()
f.close()
