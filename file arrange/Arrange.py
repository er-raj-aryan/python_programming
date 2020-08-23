import os
import time

# create folder section 
def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# move section
def move(folderName,files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")


# this section is main section
if __name__ == "__main__":
    print("\n\n\t\t   Welcome to Arrange Software \n")
    print("\t\t---------------------------------\n")
    time.sleep(1)
    files =os.listdir()
    #files.remove("Arrange.py")             #for execute the python file then uncomment this line
    files.remove("Arrange.exe")             #for execute the exe file then uncomment this 
    createIfNotExists('Images')
    print("\t\t    Images folder Created..\n")
    time.sleep(1)
    createIfNotExists('Docs')
    print("\t\t    Docs folder Created..\n")
    time.sleep(1)
    createIfNotExists('Media')
    print("\t\t    Media folder Created..\n")
    time.sleep(1)
    createIfNotExists('Others')
    print("\t\t    Others folder Created..\n\n")
    time.sleep(1)


    imgExts = [".png",".jpg",".ico",".jpeg",".gif",".tiff",".psd",".raw"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".txt",".doc" ,".pdf",".docx",".xls",".xlsx",".ppt",".pptx"]
    docs=[file for file in files if os.path.splitext(file)[1].lower() in docExts]

    mediaExts = [".mkv",".mp3",".mp4",".flv",".ogg",".wmv",".webm",".wav",".avi"]
    media=[file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    others =[]
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            others.append(file)


    move("Images",images)
    move("Docs",docs)
    move("Media",media)
    move("Others",others)
    print("\t\t    all file are arranged\n")
    time.sleep(1)
    print("\t\t---------------------------------\n")
    print("\t\t    Software Developed By :-\n\t\t\t Raj Aryan \n\n ")
    input('press Enter to exit.....')