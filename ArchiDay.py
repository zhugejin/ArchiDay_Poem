#Architecture Day
import random
from time import sleep
import colorama
from colorama import init
from colorama import Fore, Back, Style


dates = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
beautifulthoughts = ["Some beautiful in my view", "Some wonderful in my mind", "something like miracle", "something like special one"]
thinkend = ["Something like I never seen never thought", "Woo"]
draw = ["I boolean the mass", "I extrude the line", "I line the points", "I merge the surface"]
nothing = ["nothing on my mind", "on my mind", "I feel nothing", "I draw nothing", "I do nothing", "I think nothing"]



def date():
	date = random.choice(dates)
	print (Fore.RED + Style.BRIGHT + "Today is " + date + Fore.RESET + Back.RESET + Style.RESET_ALL)
	

def think():
	think = random.choice(beautifulthoughts)
	print (think)

def endthink():
	endthink = random.choice(thinkend)
	print (Style.BRIGHT + endthink + Style.RESET_ALL)

def drawing():
	drawing = random.choice(draw)
	print(drawing)

def stop():
	stop = random.choice(nothing)
	print(Style.BRIGHT + stop + Style.RESET_ALL)

def thinktime():
	date()
	sleep(3)
	think()
	sleep(3)
	think()
	sleep(3)
	think()
	sleep(3)
	endthink()
	sleep(8)
	print("")

def drawtime():
	print("I think I envision I draw ")
	sleep(6)
	print("...")
	sleep(6)
	print("...")
	sleep(3)
	print("I draw a wall")
	print("pale from altitude ")
	sleep(4)
	print("I draw a window")
	print("tearful with a pane of glass")
	sleep(4)
	drawing()
	sleep(3)
	drawing()
	sleep(8)
	print("")

def crush():
	print(Fore.BLACK + Back.RED + Style.BRIGHT + "I crush my computer" + Fore.RESET + Back.RESET + Style.RESET_ALL)
	sleep(8)
	print("")
	print(Fore.BLACK + Back.RED + Style.BRIGHT + "orz" + Fore.RESET + Back.RESET + Style.RESET_ALL)
	sleep(3)
	print("")
	sleep(3)
	print(Fore.BLACK + Back.RED + Style.BRIGHT + "Did I save it?" + Fore.RESET + Back.RESET + Style.RESET_ALL)
	sleep(3)
	print("")
	sleep(3)
	print(Fore.BLACK + Back.RED + Style.BRIGHT + "nvm I keep working" + Fore.RESET + Back.RESET + Style.RESET_ALL)
	sleep(8)
	print("")

def stopwork():
	sleep(8)
	print("")
	stop()
	sleep(3)
	stop()
	sleep(3)
	stop()
	sleep(3)
	stop()
	sleep(6)
	print("...")
	sleep(6)
	print("...")
	sleep(6)
	print(Style.BRIGHT + Fore.RED + "Wow I have time to sleep" + Style.RESET_ALL + Fore.RESET)
	sleep(8)
	print("")

def loop():
	thinktime()
	drawtime()
	crush()
	drawtime()
	print(Style.BRIGHT + Fore.RED + "I need to sleep" + Style.RESET_ALL + Fore.RESET)
	stopwork()
	print("")
	print("")
	print(Style.BRIGHT + Fore.RED + "I am going to sleep " + Style.RESET_ALL + Fore.RESET)
	sleep(12)
	print("")
	print("")
	print(Fore.RED + Style.BRIGHT + "I love my life :)" + Fore.RESET + Style.RESET_ALL)

loop()








