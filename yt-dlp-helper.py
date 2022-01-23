import os
print("================================")
print(" yt-dlp Helper by Goad for Goad ")
print("================================")
print("Other options: 'exit' 'update'")

def main():
    check=os.path.isfile("/usr/local/bin/yt-dlp")
    if check == True:
        link=str(input("Source : "))
        checker2= "exit" in link
        checker3= "update" in link
        if checker2 == True:
            exit()
        elif checker3 == True:
            os.system("sudo yt-dlp -U")
            main()
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
        install=input("yt-dlp is not installed. Do you want to install it? (UNIX Like system only)(y/n) : ")
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
