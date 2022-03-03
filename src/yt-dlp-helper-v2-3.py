from urllib.parse import urlparse
import os
import subprocess
print("================================")
print("  yt-dlp-helper by Goad V2.3-1  ")
print("================================")
print("Other options: 'exit' 'update' 'new'")
absoluteHomeFolder = os.path.expanduser("~")

def main():
    check = os.path.isfile("/usr/local/bin/yt-dlp")
    if check == True:
        checkconf = os.path.isfile(absoluteHomeFolder+"/"+"yt-dlp-helper.conf")
        if checkconf == False:
            f = open(absoluteHomeFolder+"/"+"yt-dlp-helper.conf", "w+")
            f.write("cwd1 = 1 \ncwd2 = 1 \nformat = 1 \nformatCheck = 1 ")
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
    global formatCheckConf
    global f
    n1 = -1
    cwd1Conf = False
    cwd2Conf = False
    formatConf = False
    formatCheckConf = False
    listSet = []
    varConf = []
    f = open(absoluteHomeFolder+"/"+"yt-dlp-helper.conf", "r")
    for line in f:
        reader = line.split()
        try:
            listSet.append(reader[2])           # cwd1 = 0, cwd2 = 1, format = 2, formatCheckConf = 3
            varConf.append(reader[0])
        except:
            print("Error reading config file. Config file will be rewritten.")
            os.remove(absoluteHomeFolder+"/"+"yt-dlp-helper.conf")
            main()
    formatCheckConfC = "formatCheck" in varConf
    if formatCheckConfC == False:
        print("This new version added new config called 'formatCheck' so please delete the config file at '~/yt-dlp-helper.conf' and restart the script or add 'formatCheck = (0 or 1)' in the config file.\nNote: this format checking will take sometime (more video more longer), so if you dont want to wait just turn off this feature (set to 0).")
        exit()
    for i in range(4):
        n1 = n1 + 1
        testVar = varConf[n1]+listSet[n1]
        if testVar == "cwd11":
            cwd1Conf = True
        elif testVar == "cwd21":
            cwd2Conf = True
        elif testVar == "format1":
            formatConf = True
        elif testVar == "formatCheck1":
            formatCheckConf = True
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
            print("New Feature :\n Version 2.2 : Now you can download more than one video in one go. Type '; ' at the end of the link and follow by another link.\n Version 2.3 : Tidy up some of the code and adding download all the same format options. (use 'sf' flag in the format) and added format availablity checking (not always work because of some factor.)")
            vidSourcenOptions()
        else:
            print("Not a valid url or commands!")
            vidSourcenOptions()
    else:
        if cwd1Conf == True:
            dirPrinting(1)
            whereToSave()
        else:
            whereToSave()

def whereToSave():
    global runFormatCheck
    runFormatCheck=[]
    where=str(input("Path : "))
    dircheck=os.path.isdir(where)
    if dircheck == False:
        print("Directory '"+where+"' doesn't exist.")
        print("Maybe this will help :\n", os.listdir())       
        whereToSave()
    else:
        os.chdir(where)
        if formatCheckConf == True:
            print("Please Wait. Checking Available format...")
            n = -1
            for i in range(0, count):
                queueFormatCheck = subprocess.run(['yt-dlp', '-F', link[n]], stdout=subprocess.PIPE)
                runFormatCheck.append(queueFormatCheck)
            print("Done!")
        else:
            pass
        ytdlpCommand()

def ytdlpCommand(): #sf bug is caused because i call the function again.
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
        dirPrinting(2)
    else:
        pass
    vidNumber = 0
    print("Type 'sf' to select the same format for all Videos")
    for i in range(0, count):
        vidNumber = vidNumber+1
        print(" > Select Format for Video no",vidNumber)
        what=str(input("Select Format (example: 137+140): "))
        formatList.append(what)
        funcRunFormatCheck(formatList, vidNumber)
        if notValid == True:
            ytdlpCommand()
        else:
            pass
        if "sf" in formatList[0]:
            if count == 1:
                sameFormat = False
                print("You are Downloading only one video no need to use the 'sf' flag.")
                ytdlpCommand()
            else:
                sameFormat = True
                what=str(input("Select Format for all Videos (example: 137+140): "))
                formatList.append(what)
                funcRunFormatCheck(formatList, 1)
                if notValid == True:
                    ytdlpCommand()
                else:
                    pass
                break
        else:
            pass
    n = -1
    vidNumber = 0
    if sameFormat == False:
        if count == 1:
            vidNumber = vidNumber+1
            print(" > Downloading Video no",vidNumber)
            os.system("yt-dlp -f "+formatList[0]+" "+link[0])
            exit()
        else:
            for i in range(0, count):
                n = n + 1
                vidNumber = vidNumber+1
                print(" > Downloading Video no LMAO",vidNumber)
                print("yt-dlp -f "+formatList[n]+" "+link[n])
            exit()

    else:
        for i in range(0, count):
            n = n + 1
            vidNumber = vidNumber+1
            print(" > Downloading Video no",vidNumber)
            os.system("yt-dlp -f "+formatList[1]+" "+link[n])
        exit()

def dirPrinting(printType):
    if printType == 1:
        print("Current Working Directory is '"+os.getcwd()+"'")
    else:
        print("The File will be saved at '"+os.getcwd()+"'")

def funcRunFormatCheck(formatChoice, videoNo):
    global notValid
    notValid = False
    if formatChoice not in runFormatCheck:
        notValid = True
        print("Format", formatChoice,"not available for video", videoNo)


main()
f.close()
