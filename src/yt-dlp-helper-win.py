from urllib.parse import urlparse
import os
print("================================")
print("  yt-dlp-helper windows V2.5.3  ")
print("================================")
print("Options: 'exit' 'new' 'rconf' 'md'")
absoluteHomeFolder = os.path.expanduser("~")

def main():
    checkconf = os.path.isfile(absoluteHomeFolder+"\\yt-dlp-helper.conf")
    if checkconf == True :
        readTheConfigFile()
        vidSourcenOptions()
    else:
        createConfig()
        readTheConfigFile()
        vidSourcenOptions()

def readTheConfigFile():
    global possiblePattern, cwd1Settings, cwd2Settings, formatpSettings, confDebugSettings, defaultLocationSettings, checkDefaultLocation, versionInfo, askExitSettings, ytdlpPathSettings
    possiblePattern = [True, False]

    try:
        with open(absoluteHomeFolder+"\\yt-dlp-helper.conf") as infile:
            exec(infile.read())
    except:
        print("Error reading the config file : invalid config.")
        askUser = input("Do you want to recreate the config file? (y/n) : ")
        if askUser == "y":
            print("Recreating the config file...")
            os.remove(absoluteHomeFolder+"\\yt-dlp-helper.conf")
            main()
        else:
            exit()
    ## VERSION ##
    try:
        versionInfo = version
        if versionInfo < 2.53:
            print("You are using the old config file '",versionInfo,"'. Please update the config file using 'rconf' option.")
    except:
        versionInfo = "Unknown"
        print("You are using the old config file '",versionInfo,"'. Please update the config file using 'rconf' option.")
    ## debug ##
    try:
        confDebugSettings = confDebug
    except:
        confDebugSettings = False

    ## yt-dlp path ##
    try:
        ytdlpPathSettings = 'None'
        ytdlpPathSettings = ytdlpPath
        exeCheck = os.path.isfile(ytdlpPathSettings)
        if exeCheck == False:
            if ytdlpPathSettings != 'None':
                print("ERROR : The executable at ", ytdlpPathSettings, "doesnt exist!")
                print("Please update to the right path from the config file or do 'rconf'.")
            else:
                ytdlpPathSettings = 'yt-dlp'
    except:
        print("ERROR : Can't detect the yt-dlp.exe path!")
        print("Possible fix(1) : do the 'rconf' options in source/options.")
        print("Possible fix(2) : update yt-dlp-helper.conf to include the yt-dlp.exe right path.")

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

    # askExit #
    try:
        askExitSettings = askExit
    except:
        print("Error reading the config file : Missing askExit variable. using the default value...")
        askExitSettings = 1
    if askExitSettings not in possiblePattern:
        print("askExit possible value is True(1) or False(0) not", askExit,"using the default value (1)")
        askExitSettings = 1
    else:
        pass

    ## general ##
    try:
        cwd1Settings = cwd1
        cwd2Settings = cwd2
        formatpSettings = formatp
    except:
        print("Error reading the config file : missing variable.")
        askUser = input("Do you want to recreate the config file? (y/n) : ")
        if askUser == "y":
            print("Recreating the config file...")
            os.remove(absoluteHomeFolder+"\\yt-dlp-helper.conf")
            main()
        else:
            exit()

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
            print("version =", versionInfo)
            print("cwd1 =",cwd1Settings)
            print("cwd2 =",cwd2Settings)
            print("format =",formatpSettings)
            print("confDebugSettings =",confDebugSettings)
            print("defaultLocationSettings = '"+defaultLocationSettings+"'")
            print("checkDefaultLocation =",checkDefaultLocation)
            print("askExitSettigns =", askExitSettings)
            print("ytdlpPathSettings = '"+ ytdlpPathSettings+"'")
            print("==============================================")
        except:
            print("Error reading the config file.")
            print("Note : if some var not defined inside the config file with debug on, this massage will came out.")
    #########

    link=str(input("Source / options : "))
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
        newFcheck = "new" in link[0]
        resetConfFile = "rconf" in link[0]
        manualDir = "md" in link[0]
        if exitcheck == True:
            exit()
        elif newFcheck == True:
            print("Version :",versionInfo)
            print("Windows version.")
            #print("New Custom configuration (no need to change it manually at your home folder.)")
            vidSourcenOptions()
        elif resetConfFile == True:
            usrInput=input("are you sure? (y/n) : ")
            if usrInput == "y":
                os.remove(absoluteHomeFolder+"\\yt-dlp-helper.conf")
            else:
                exit()
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
            os.system(ytdlpPathSettings+" -F "+ link[n])
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
    print("Preset : 'HD' for 720p(136+140), 'FHD' for 1080p(137+140), 'small' for 480p(135+140)")
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
                os.system(ytdlpPathSettings+" -f 136+140 "+link[0])
            elif formatList[0] == "FHD":
                os.system(ytdlpPathSettings+" -f 137+140 "+ link[0])
            elif formatList[0] == "small":
                os.system(ytdlpPathSettings+" -f 135+140 "+ link[0])
            elif formatList[0] == "webmHD":
                os.system(ytdlpPathSettings+" -f 247+251 "+ link[0])
            elif formatList[0] == "webmFHD":
                os.system(ytdlpPathSettings+" -f 248+251 "+ link[0])
            #########
            else:
                os.system(ytdlpPathSettings+" -f "+ formatList[0]+" " + link[0])
            endProgram()
        else:
            # MORE THAN ONE VIDEOS DOWNLOADS
            for i in range(0, count):
                n += 1
                vidNumber = vidNumber+1
                print(" > Downloading Video no",vidNumber)
                ## NEW ##
                if formatList[n] == "HD":
                    os.system(ytdlpPathSettings+" -f 136+140 "+link[n])
                elif formatList[n] == "FHD":
                    os.system(ytdlpPathSettings+" -f 137+140 "+link[n])
                elif formatList[n] == "small":
                    os.system(ytdlpPathSettings+" -f 135+140 "+ link[n])
                elif formatList[n] == "webmHD":
                    os.system(ytdlpPathSettings+" -f 247+251 "+ link[n])
                elif formatList[n] == "webmFHD":
                    os.system(ytdlpPathSettings+" -f 248+251 "+ link[n])

            #########
                else:
                    os.system(ytdlpPathSettings+" -f "+formatList[n]+" "+link[n])
            endProgram()

    else:
        # MORE THAN ONE VIDEOS DOWNLOAD WITH THE SAME FORMAT
        for i in range(0, count):
            n +=1
            vidNumber = vidNumber+1
            print(" > Downloading Video no",vidNumber)
            ## NEW ##
            if formatList[1] == "HD":
                os.system(ytdlpPathSettings+" -f 136+140 "+link[n])
            elif formatList[1] == "FHD":
                os.system(ytdlpPathSettings+" -f 137+140 " + link[n])
            elif formatList[1] == "small":
                os.system(ytdlpPathSettings+" -f 135+140 "+ link[n])
            elif formatList[1] == "webmHD":
                os.system(ytdlpPathSettings+" -f 247+251 "+ link[n])
            elif formatList[1] == "webmFHD":
                os.system(ytdlpPathSettings+" -f 248+251 "+ link[n])
            #########
            else:
                os.system(ytdlpPathSettings+" -f " + formatList[1]+" " + link[n])
        endProgram()

def dirPrinting(printType):
    if printType == 1:
        if checkDefaultLocation == True:
            print("Current Working Directory is '"+defaultLocationSettings+"'")
        else:
            print("Current Working Directory is '"+os.getcwd()+"'")
    else:
        print("The File will be saved at '"+os.getcwd()+"'")

def createConfig():
    print(" > Configure Configuration file")
    yes=["Y", "y"]
    no=["n", "N"]
    usrInput = input("Do you want to use the default settings (y/n): ")
    if usrInput in yes:
        with open(absoluteHomeFolder+"\\yt-dlp-helper.conf", "w+") as infile:
            infile.write("global cwd1, cwd2, formatp, confDebug, defaultLocation, version, askExit, ytdlpPath\n###CONFIG START HERE###\nversion = 2.53\ncwd1 = True \ncwd2 = True \nformatp = True \nconfDebug = False \ndefaultLocation = 'None' \naskExit = True \nytdlpPath = 'None' ")
        print("Config file created. Please relaunch the script.")
        exit()
    else:
        with open(absoluteHomeFolder+"\\yt-dlp-helper.conf", "w+") as infile:
            infile.write("global cwd1, cwd2, formatp, confDebug, defaultLocation, version, askExit, ytdlpPath\n###CONFIG START HERE###\nversion = 2.53\n")
            print("Do you want to specify yt-dlp directory ?")
            option0=input("(y/n) : ")
            if option0 in yes:
                print("NOTE : use '\\\\' instead of '\\'\nExample: C:\\\\users\\\\user")
                option01 = input("Type the executable location here : ")
                infile.write("ytdlpPath = '"+option01+"'\n")
            else:
                infile.write("ytdlpPath = 'None'\n")
            print("ytdlpPath configured.")
            
            print("Do you want to enable current working directory printing?")
            option1=input("(y/n) : ")
            if option1 in yes:
                infile.write("cwd1 = True\n")
            elif option1 in no:
                infile.write("cwd1 = False\n")
            else:
                infile.write("cwd1 = True\n")
            print("cwd1 configured.")

            print("Do you want to enable second current working directory printing?")
            option2=input("(y/n) : ")
            if option2 in yes:
                infile.write("cwd2 = True\n")
            elif option2 in no:
                infile.write("cwd2 = False\n")
            else:
                infile.write("cwd2 = True\n")
            print("cwd2 configured.")

            print("Do you want to enable format printing?")
            option3=input("(y/n) : ")
            if option3 in yes:
                infile.write("formatp = True\n")
            elif option3 in no:
                infile.write("formatp = False\n")
            else:
                infile.write("formatp = True\n")
            print("formatp configured.")

            print("Do you want to enable Exit Dialog?")
            option3=input("(y/n) : ")
            if option3 in yes:
                infile.write("askExit = True\n")
            elif option3 in no:
                infile.write("askExit = False\n")
            else:
                infile.write("askExit = True\n")
            print("askExit configured.")

            print("Do you want to enable default location?")
            option4=input("(y/n) : ")
            if option4 in yes:
                print("NOTE : use '\\\\' instead of '\\'\nExample: C:\\\\users\\\\user")
                option5 = input("Type the default save location here : ")
                infile.write("defaultLocation = '"+option5+"'\n")
            else:
                infile.write("defaultLocation = 'None'\n")
            print("defaultLocation configured.")
            infile.write("confDebug = False")
        print("Done Creating configuration file. Please restart the script.")
        exit()

def endProgram():
    if askExitSettings == True :
        usrInput = input("Do you want to exit? (y/n) : ")
        if usrInput == "y":
            exit()
        else:
            main()
    else:
        exit()

main()
