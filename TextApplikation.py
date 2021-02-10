from pynput.keyboard import Key, Controller
import time
import tkinter
#Variables
#########################################################

#   § § § § § SPAM § § § § §

start = 0

Anzahl = 10
#########################################################
#length not valid



#########################################################
def v1():
    global start
    start = 1
    time.sleep(1)
    


def restart():
    main.start()
    
def ende():
    main.destroy()
    time.sleep(2)



main = tkinter.Tk()
lb1 = tkinter.Label(main, text = "Start Spamm Attack")
lb1["font"] = "courier 16 italic"
lb1["height"] = 2
lb1["width"] = 25
lb1["borderwidth"] = 5
lb1["relief"] = "groove"
lb1["bg"] = "#FFFFFF"
lb1["fg"] = "#000000"
lb1["anchor"] = "w"
lb1.pack()



b = tkinter.Button(main, text = "send Text", command = v1)
b.pack()

b = tkinter.Button(main, text = "Ausführen", command = ende)
b.pack()


main.mainloop()


#print(start)



keyboard = Controller()
def write(start):

    if start == 1:
        time.sleep(0.5)
        for i in range(1):
            for char in (spam_phrase):
                time.sleep(0)
                keyboard.press(char)
                keyboard.release(char)
                
            #keyboard.press(Key.enter)
            
    else:
        time.sleep(0.2)
        command = restart


def getinput():    
    spamfile = open("./input.txt", "r")
    spam_phase = str(spamfile.readline(30))
    return spam_phase

spam_phrase = getinput()


write(start)


