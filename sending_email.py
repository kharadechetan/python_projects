import smtplib as s 
ob = s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login('Write your own email address',password='Write your own password')
subject="Test python"
body="I love Python"
message="subject:{}\n\n{}".format(subject,body)
listadd=['add the email addresses which you want to send email']
ob.sendmail('from which email do you want to send add that email',listadd,message)
print("Send mail")
ob.quit()