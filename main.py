import smtplib
import pandas
from email_details import sender_email_id, sender_email_id_password

data=pandas.read_csv("receiver_emails.csv")
names_list=data["name"].to_list()
emails_list=data["email"].to_list()
#print(emails_list)

with open("starting_letter.txt", "r") as rp:
    letter_text=rp.read()
    #print(letter_text)

s=smtplib.SMTP('smtp.gmail.com')
s.connect('smtp.gmail.com', 587)
s.starttls()
s.login(sender_email_id, sender_email_id_password)
    
for i in range(len(names_list)):
    new_letter=letter_text.replace("[name]", names_list[i].strip())
        
    with open(f"/Users/gayathriu/Documents/Email Automator/new_{names_list[i].strip()}.txt", mode="w") as fp:
        writefiles=fp.write(new_letter)
        
    s.sendmail(sender_email_id, emails_list[i], new_letter)

s.quit()

