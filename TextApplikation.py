from pynput.keyboard import Key, Controller
import time
import tkinter
#Variables
#########################################################
start = 0
num = int(open("./input.txt").readlines()[1])
sleep = int(open("./input.txt").readlines()[2])

def v1():
    global start
    start = 1
    time.sleep(1)
    


#def restart():
    #main.start()
    
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



keyboard = Controller()
def write(start, num, sleep):

    if start == 1:
        time.sleep(0.5)
        for i in range(num):
            for char in (spam_phrase):
                time.sleep(0)
                keyboard.press(char)
                keyboard.release(char)
                
            keyboard.press(Key.enter)
            
            if i == num:
                pass
            else:
                time.sleep(sleep)

    else:
        time.sleep(0.2)
        #command = restart


def getinput():    
    spamfile = open("./input.txt", "r")
    spam_phase = str(spamfile.readline(30))
    return spam_phase

spam_phrase = getinput()


write(start, num, sleep)


