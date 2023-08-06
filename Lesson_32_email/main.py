import smtplib

my_email = "bebopjunky@googlemail.com"
#smtp.mail.yahoo.com
password = "oYuPqY22XT4Pa8"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="hundreddays@myyahoo.com",msg="Hello")
connection.close()


