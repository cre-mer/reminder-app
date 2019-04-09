import time
import webbrowser

total_breaks = 8
break_count = 0

while(break_count < total_breaks):
    time.sleep(3600)
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    break_count = break_count + 1
