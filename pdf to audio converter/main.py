import pyttsx3
import PyPDF2


speak = pyttsx3.init()

# variable section 
start__Pages = int(input("Enter the starting page : "))
audioBook = input("Enter the name of pdf with extension : ")
# end__Pages = input("Enter the end page ")

p = PyPDF2.PdfFileReader(audioBook)
# print( pdfRead.documentInfo)
pages = p.numPages
for read in range(start__Pages,10):
    # if end__Pages == pages:
        print('audio book is start playing ..  ')
        page = p.getPage(read)
        text = page.extractText()
        print (text)
    
    # speak.say(text)
    # speak.runAndWait()