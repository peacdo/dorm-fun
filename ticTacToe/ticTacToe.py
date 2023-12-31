x="""
     |     |     
     |     |     
_____|_____|____
     |     |    
     |     |    
_____|_____|____
     |     |    
     |     |    
     |     |    
"""
player1=input("Player1(X): ")
player2=input("Player2(O): ")

while True:
    print(x)
    move1=input(f"Where do you want to place your mark {player1} ? ")
    match move1 :
        case "1":
            #1.kordinat
            x=x[:21]+"X"+x[22:]
        case "2":
            #2.kordinat
            x=x[:27]+"X"+x[28:]
        case "3":
            #3.kordinat
            x=x[:33]+"X"+x[34:]
        case "4":
            #4.kordinat
            x=x[:73]+"X"+x[74:]
        case "5":
            #5.kordinat
            x=x[:79]+"X"+x[80:]
        case "6":
            #6.kordinat
            x=x[:85]+"X"+x[86:]
        case "7":    
            #7.kordinat
            x=x[:124]+"X"+x[125:]
        case "8":
            #8.kordinat
            x=x[:130]+"X"+x[131:]
        case "9":
            #9.kordinat
            x=x[:136]+"X"+x[137:]
        case _ :
            print("Invalid coordinate please enter a number 1 to 9.")
    
    print(x)
    move2=input(f"Where do you want to place your mark {player2} ? ")
    match move2 :
        case "1":
            #1.kordinat
            x=x[:21]+"O"+x[22:]
        case "2":
            #2.kordinat
            x=x[:27]+"O"+x[28:]
        case "3":
            #3.kordinat
            x=x[:33]+"O"+x[34:]
        case "4":
            #4.kordinat
            x=x[:73]+"O"+x[74:]
        case "5":
            #5.kordinat
            x=x[:79]+"O"+x[80:]
        case "6":
            #6.kordinat
            x=x[:85]+"O"+x[86:]
        case "7":    
            #7.kordinat
            x=x[:124]+"O"+x[125:]
        case "8":
            #8.kordinat
            x=x[:130]+"O"+x[131:]
        case "9":
            #9.kordinat
            x=x[:136]+"O"+x[137:]
        case _ :
            print("Invalid coordinate please enter a number 1 to 9.")
