from tkinter import *
import smtplib

#Main Screen Init
master = Tk()


#Functions
def send():
    try:
        username = temp_username.get()
        password = temp_password.get()
        to       = temp_receiver.get()
        subject  = temp_subject.get()
        body     = temp_body.get()
        if username=="" or password=="" or to=="" or subject=="" or body=="":
            notif.config(text="Заполните все поля", fg="red")
            return
        else:
            finalMessage = 'Тема: {}\n\n{}'.format(subject, body)
            server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
            server.login(username, password)
            server.sendmail(username,to,finalMessage)
            notif.config(text="Сообщение было отправлено", fg="green")
    except:
        notif.config(text="Ошибка отправки", fg="red")


def reset():
  usernameEntry.delete(0,'end')
  passwordEntry.delete(0,'end')
  receiverEntry.delete(0,'end')
  subjectEntry.delete(0,'end')
  bodyEntry.delete(0,'end')

#Labels
Label(master, text="mail.ru почтовый клиент", font=('Calibri',15)).grid(row=0, sticky=N)
Label(master, text="Внимание в поле своей почты нужно использовать почты Mail.ru и для отправки сообщений используйте внешний пароль", font=('Calibri',11)).grid(row=1, sticky=W, padx=5 ,pady=10)

Label(master, text="Ваша почта", font=('Calibri', 11)).grid(row=2,sticky=W, padx=5)
Label(master, text="Ваш пароль", font=('Calibri', 11)).grid(row=3,sticky=W, padx=5)
Label(master, text="Кому", font=('Calibri', 11)).grid(row=4,sticky=W, padx=5)
Label(master, text="Тема", font=('Calibri', 11)).grid(row=5,sticky=W, padx=5)
Label(master, text="Сообщение", font=('Calibri', 11)).grid(row=6,sticky=W, padx=5)
notif = Label(master, text="", font=('Calibri', 11),fg="red")
notif.grid(row=7,sticky=S)

#Storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject  = StringVar()
temp_body     = StringVar()

#Entries
usernameEntry = Entry(master, textvariable = temp_username)
usernameEntry.grid(row=2,column=0)
passwordEntry = Entry(master, textvariable = temp_password)
passwordEntry.grid(row=3,column=0)
receiverEntry  = Entry(master, textvariable = temp_receiver)
receiverEntry.grid(row=4,column=0)
subjectEntry  = Entry(master, textvariable = temp_subject)
subjectEntry.grid(row=5,column=0)
bodyEntry     = Entry(master, textvariable = temp_body)
bodyEntry.grid(row=6,column=0)

#Buttons
Button(master, text = "Отправить", command = send).grid(row=7,   sticky=W,  pady=15, padx=5)
Button(master, text = "Сброс", command = reset).grid(row=8,  sticky=W,  padx=5, pady=15)

#Mainloop
master.mainloop()