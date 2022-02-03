import os
print("====================================")
print(" youtube-dl Helper by Goad for Goad ")
print("====================================")
print("Type 'exit' to exit")

def main():
    try:
        link=str(input("Source : "))
        checker2= "exit" in link
        if checker2 == True:
            exit()
        print("Current Working Directory is",os.getcwd())
        where=str(input("Path : "))
        dircheck=os.path.isdir(where)
        if dircheck == False:
            print("Directory '"+where+"' doesn't exist.")
            main()
        os.chdir(where)
        os.system("youtube-dl -F "+link)
        print("The file will be saved at",os.getcwd())
        what=str(input("Select Format (example: 137+140): "))
        checker2= "exit" in what
        if checker2 == True:
            exit()
        os.system("youtube-dl -f "+what+" "+link)
    except:
        print("Error occured.")
main()