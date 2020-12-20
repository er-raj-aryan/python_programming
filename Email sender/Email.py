import smtplib 

# variables
smtpServer = input("Enter the smtp server: ")
port = input("Enter the port (587): ")
email = input("Enter the email: ")
password = input("Enter the password: ")
receiverMail = input("Enter the Receiver Mail: ")
message = input("Enter the Message: ")

# mail services
server = smtplib.SMTP(smtpServer, port) #for gmail use >>>  smtp.gmail.com
server.starttls()
server.login(email,password)
server.sendmail(email,receiverMail,message)
server.quit()