from urllib.parse import urlparse
import subprocess
import os
print("================================")
print("  yt-dlp-helper by Goad V2.4.4  ")
print("================================")
print("Options: 'exit' 'update' 'new' 'rconf' 'rdown' 'md'")
absoluteHomeFolder = os.path.expanduser("~")

def main():
    check1 = os.path.isfile("/usr/local/bin/yt-dlp")
    check2 = os.path.isfile("/usr/bin/yt-dlp")
    if check1 or check2 == True:
        check = True
        checkconf = os.path.isfile(absoluteHomeFolder+"/yt-dlp-helper.conf")
    else:
        check = False

    if check == True:
        if checkconf == False:
            with open(absoluteHomeFolder+"/yt-dlp-helper.conf", "w+") as infile:
                infile.write("global cwd1, cwd2, formatp, confDebug, defaultLocation\n###CONFIG START HERE###\ncwd1 = True \ncwd2 = True \nformatp = True \nconfDebug = False \ndefaultLocation = 'None' ")
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
    global possiblePattern, cwd1Settings, cwd2Settings, formatpSettings, confDebugSettings, defaultLocationSettings, checkDefaultLocation
    possiblePattern = [True, False]
    try:
        with open(absoluteHomeFolder+"/yt-dlp-helper.conf") as infile:
            exec(infile.read())
    except:
        print("Error reading the config file : invalid config.")
        print("Recreating the config file...")
        os.remove(absoluteHomeFolder+"/yt-dlp-helper.conf")
        main()

    ## debug ##
    try:
        confDebugSettings = confDebug
    except:
        confDebugSettings = False

    ## default location ##
    defaultLocationSettings = "None"
    checkDefaultLocation = False
    try:
        defaultLocationSettings = defaultLocation
        stringCheck = isinstance(defaultLocationSettings, str) # <-- check if string
        if stringCheck == True:
            if defaultLocationSettings != 'None':
                checkDefaultLocation = os.path.isdir(defaultLocationSettings)
                if checkDefaultLocation == False:
                    print("The specified default location '"+defaultLocationSettings+"' doesn't exist.")
            elif defaultLocationSettings == 'None':
                checkDefaultLocation = False
        else:
            print("defaultLocation possible value is a string not",defaultLocation,". Using manual mode...")
    except:
        print("Error reading the config file : missing defaultLocation variable.")
        print("Possible fix (1): at 'source/options' do 'rconf' options and restart the script")
        print("using manual mode...")

    ## general ##
    try:
        cwd1Settings = cwd1
        cwd2Settings = cwd2
        formatpSettings = formatp
    except:
        print("Error reading the config file : missing variable. (or updating to the new config.)")
        print("Recreating the config file...")
        os.remove(absoluteHomeFolder+"/yt-dlp-helper.conf")
        main()

    if cwd1Settings not in possiblePattern:
        print("cwd1 possible value is True(1) or False(0) not",cwd1,"using the default value (1)")
        cwd1Settings = True
    if cwd2Settings not in possiblePattern:
        print("cwd2 possible value is True(1) or False(0) not",cwd2,"using the default value (1)")
        cwd2Settings = True
    if formatpSettings not in possiblePattern:
        print("formatp possible value is True(1) or False(0) not",formatp,"using the default value (1)")
        formatpSettings = True

def vidSourcenOptions():
    global link, count, checkDefaultLocation
    
    ## NEW ##
    ## DEBUG ##
    if confDebugSettings == True:
        try:
            print("==DEBUG======================================")
            print("cwd1 =",cwd1Settings)
            print("cwd2 =",cwd2Settings)
            print("format =",formatpSettings)
            print("confDebugSettings =",confDebugSettings)
            print("defaultLocationSettings = '"+defaultLocationSettings+"'")
            print("checkDefaultLocation =",checkDefaultLocation)
            print("NOTE : template reminder variable is deleted")
            print("==============================================")
        except:
            print("Error reading the config file.")
            print("Note : if some var not defined inside the config file with debug on, this massage will came out.")
    #########

    link=str(input("Source / options : "))
    updateOptions = ['update','UPDATE', 'Update']
    exitOptions = ['exit', 'EXIT', 'Exit']
    urlcheckbolList = []
    countVid= link.count(";")
    link = link.split("; ")
    count = countVid + 1
    n = -1
    for i in range(0, count):
        n += 1
        urlcheck = urlparse(link[n])
        urlcheckbol = (all([urlcheck.scheme, urlcheck.netloc, urlcheck.path])
                        and len(urlcheck.netloc.split(".")) > 1)
        urlcheckbolList.append(urlcheckbol)

    if False in urlcheckbolList :
        exitcheck = link[0] in exitOptions
        updatecheck = link[0] in updateOptions
        newFcheck = "new" in link[0]
        resetConfFile = "rconf" in link[0]
        reDownytdlp = "rdown" in link[0]
        manualDir = "md" in link[0]
        if exitcheck == True:
            exit()
        elif updatecheck == True:
            print(" > Running Command : sudo yt-dlp -U")
            os.system("sudo yt-dlp -U")
            vidSourcenOptions()
        elif newFcheck == True:
            print("New Feature :\n Version 2.2 : Now you can download more than one video in one go. Type '; ' at the end of the link and follow by another link.\n Version 2.3 : Tidy up some of the code and adding download all the same format options. (use 'sf' flag in the format)\n Version 2.3.2 : Rewritten how the config file reading work, a new reset config file option(rconf) and redownload yt-dlp(rdown).\n Version 2.4 : Added preset download. Use 'HD' for 720p and 'FHD' for 1080p video preset.\n Version 2.4.3 : addded Save to Default location.(change 'defaultLocation' variable from 'None' to the location default location. example: defaultLocation='/home/goad/Videos/') (You can turn in off by using 'md') and deleted presetReminderSettings")
            vidSourcenOptions()
        elif resetConfFile == True:
            os.remove(absoluteHomeFolder+"/yt-dlp-helper.conf")
            main()
        elif reDownytdlp == True :
            os.system("sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && sudo chmod a+rx /usr/local/bin/yt-dlp")
            main()
        elif manualDir == True:
            if checkDefaultLocation == False:
                print("Already using manual directory!")
                vidSourcenOptions()
            else:
                checkDefaultLocation = False
                print("Changed to manual directory.")
                vidSourcenOptions()
        else:
            print("Not a valid url or commands!")
            vidSourcenOptions()
    else:
        if cwd1Settings == True:
            dirPrinting(1)
            whereToSave()
        else:
            whereToSave()

def whereToSave():
    if checkDefaultLocation == False:
        where=str(input("Path : "))
        dircheck=os.path.isdir(where)
        if dircheck == False:
            print("Directory '"+where+"' doesn't exist.")
            print("Maybe this will help :\n", os.listdir())
            whereToSave()
        else:
            os.chdir(where)
            ytdlpCommand()
    else:
        os.chdir(defaultLocationSettings)
        ytdlpCommand()


def ytdlpCommand(): #sf bug is caused because i call the function again.
    sameFormat = False
    formatList=[]
    if formatpSettings == True:
        n = -1
        vidNumber = 0
        for i in range(0, count):
            n += 1
            vidNumber = vidNumber+1
            print(" > Format of Video no",vidNumber)
            os.system("yt-dlp -F "+link[n])
    else:
        pass
    if cwd2Settings == True:
        dirPrinting(2)
    else:
        pass
    vidNumber = 0
    if count > 1:
        print("Type 'sf' to select the same format for all Videos")
    else:
        pass
    ## NEW ##
    print("Preset : 'HD' for 720p(136+140), 'FHD' for 1080p(137+140)")
    #########
    for i in range(0, count):
        vidNumber = vidNumber+1
        print(" > Select Format for Video no",vidNumber)
        what=str(input("Select Format (example: 137+140): "))
        formatList.append(what)

        if "sf" in formatList[0]:
            if count == 1:
                sameFormat = False
                print("You are Downloading only one video no need to use the 'sf' flag.")
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
        # 1 VIDEO DOWNLOAD
        if count == 1:
            vidNumber = vidNumber+1
            print(" > Downloading Video no",vidNumber)
            ## NEW ##
            if formatList[0] == "HD":
                os.system("yt-dlp -f 136+140 "+link[0])
                exit()
            elif formatList[0] == "FHD":
                os.system("yt-dlp -f 137+140 "+link[0])
                exit()
            #########
            os.system("yt-dlp -f "+formatList[0]+" "+link[0])
            exit()
        else:
            # MORE THAN ONE VIDEOS DOWNLOADS
            for i in range(0, count):
                n += 1
                vidNumber = vidNumber+1
                print(" > Downloading Video no",vidNumber)
                ## NEW ##
                if formatList[n] == "HD":
                    os.system("yt-dlp -f 136+140 "+link[n])
                elif formatList[n] == "FHD":
                    os.system("yt-dlp -f 137+140 "+link[n])
            #########
                else:
                    print("yt-dlp -f "+formatList[n]+" "+link[n])
            exit()

    else:
        # MORE THAN ONE VIDEOS DOWNLOAD WITH THE SAME FORMAT
        for i in range(0, count):
            n +=1
            vidNumber = vidNumber+1
            print(" > Downloading Video no",vidNumber)
            ## NEW ##
            if formatList[1] == "HD":
                os.system("yt-dlp -f 136+140 "+link[n])
            elif formatList[1] == "FHD":
                os.system("yt-dlp -f 137+140 "+link[n])
            #########
            else:
                os.system("yt-dlp -f "+formatList[1]+" "+link[n])
        exit()

def dirPrinting(printType):
    if printType == 1:
        if checkDefaultLocation == True:
            print("Current Working Directory is '"+defaultLocationSettings+"'")
        else:
            print("Current Working Directory is '"+os.getcwd()+"'")
    else:
        print("The File will be saved at '"+os.getcwd()+"'")

main()
