from urllib.parse import urlparse
import os
print("================================")
print(" yt-dlp Helper by Goad for Goad ")
print("================================")
print("Other options: 'exit' 'update'")

def main():
    check=os.path.isfile("/usr/local/bin/yt-dlp")
    if check == True:
        link=str(input("Source : "))
        exitcheck= "exit" in link
        updatecheck= "update" in link
        if exitcheck == True:
            exit()
        elif updatecheck == True:
            print(" >> Running Command : sudo yt-dlp -U")
            os.system("sudo yt-dlp -U")
            main()
        else:
            urlcheck = urlparse(link)
            urlcheckbol = (all([urlcheck.scheme, urlcheck.netloc, urlcheck.path])
                           and len(urlcheck.netloc.split(".")) > 1)
            if urlcheckbol == False :
                print("Not a valid url or commands!")
                exit()
        print("Current Working Directory is",os.getcwd()) # add "#" at the start of the line to disable current working directory"
        where=str(input("Path : "))
        dircheck=os.path.isdir(where)
        if dircheck == False:
            print("Directory '"+where+"' doesn't exist.")
            main()
        os.chdir(where)
        os.system("yt-dlp -F "+link) # add "#" at the start of the line to disable format printing
        print("The file will be saved at",os.getcwd()) # add "#" at the start of the line to disable new cwd 
        what=str(input("Select Format (example: 137+140): "))
        os.system("yt-dlp -f "+what+" "+link)
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
main()
