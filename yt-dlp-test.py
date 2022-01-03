import os
print("================================")
print(" yt-dlp Helper by Goad for Goad ")
print("(exit)==========================")

def main():
    check=os.path.isfile("/usr/local/bin/yt-dlp")
    if check == True :
        link=str(input("Source : "))
        checker2= "exit" in link
        if checker2 == True:
            exit()
        where=str(input("Path : "))
        dircheck=os.path.isdir(where)
        if dircheck == False:
            print("Directory '"+where+"' doesnt exist.")
            main()
        checker2="exit" in where
        if checker2 == True:
            exit()
        os.chdir(where)
        os.system("yt-dlp -F "+link)
        print("The file will be saved at",os.getcwd())
        what=str(input("Select Format (example: 137+140): "))
        checker2="exit" in what
        if checker2 == True:
            exit()
        os.system("yt-dlp -f "+what+" "+link)
    else :
        print("yt-dlp is not installed. Please install it first.")
        exit()
main()
