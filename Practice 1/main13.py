# Car game

startcount = False
while True :
    value = input("> ").lower()
    if value == "help":
        print(''' start - to start the car
 stop - to stop the car
 quit - to quit the game''')
    elif value == "start":
        if startcount == False:
            print(" Car started... Ready to go")
            startcount = True
        else:
            print(" Car is already started")
    elif value == "stop":
        if startcount == True:
            print(" Car stopped")
            startcount = False
        else:
            print(" Car is already stopped")
    elif value == "quit":
        break
    else:
        print(" I don't understand")
