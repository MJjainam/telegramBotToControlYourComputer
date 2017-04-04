import time
import datetime
import telepot  #Telegram library
import subprocess
import os

def handle(msg):
    chat_id = msg['chat']['id']     #Get the userID of the chat
    command = msg['text']           #Get the text message

    print 'Got command: %s' % command  

    if command[0:2] == "cd":    #If 'cd' command is passed, change the 
        path = command[3:]      #working directory by using
        os.chdir(path)          # using os.chdir command.  
        p = os.getcwd()
    	bot.sendMessage(chat_id,"working directory changed to "  + p)
        
    else:
        command = command.split(" ")   #convert the linux command string to array.
        output = subprocess.Popen(command,stdout=subprocess.PIPE,stderr = subprocess.PIPE) #Executes the Command passed
        strOut = output.stdout.read()  #Get the output from terminal
        strErr = output.stderr.read()  #Get the error output from terminal
        if strOut:                     #If strOut is not empty
            bot.sendMessage(chat_id,strOut)  #send the message back to user
        if strErr:                      #If strErr is not empty
            bot.sendMessage(chat_id,strErr)   #send the error message back to user
  

bot = telepot.Bot('365050885:AAHaGjTJzEke-4DkEWOW1yXzlbNsUdD-pQg')
bot.message_loop(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)