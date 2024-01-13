#rejected.. 01.01.24 - Player must not be able to place his mark in a already occupied space.
# no input validation, code is not optimized too long can be shorten to almost half.
markedspaces=[]
player1=input("Player1(X): ")
player2=input("Player2(O): ")
player1moves=[]
player2moves=[]
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
    
def m1(x,player1moves): 
    print(x)
    
    move1=input(f"Where do you want to place your mark {player1} ? ")
    if move1 in markedspaces :
        print("\nThis space has already marked.\n")
        return m1(x,player1moves)
    else:
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
                print("\nInvalid coordinate please enter a number 1 to 9.\n")
                return move1(x)
        markedspaces.append(move1)
        player1moves.append(move1)

        if "1" in player1moves and "2" in player1moves and "3" in player1moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player1}, you won with no effort at all!")
            return
        elif "4" in player1moves and "5" in player1moves and "6" in player1moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player1}, you won with no effort at all!")
            return
        elif "7" in player1moves and "8" in player1moves and "9" in player1moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player1}, you won with no effort at all!")
            return
        elif "1" in player1moves and "4" in player1moves and "7" in player1moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player1}, you won with no effort at all!")
            return
        elif "2" in player1moves and "5" in player1moves and "8" in player1moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player1}, you won with no effort at all!")
            return
        elif "3" in player1moves and "6" in player1moves and "9" in player1moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player1}, you won with no effort at all!")
            return
        elif "1" in player1moves and "5" in player1moves and "9" in player1moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player1}, you won with no effort at all!")
            return
        elif "3" in player1moves and "5" in player1moves and "7" in player1moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player1}, you won with no effort at all!")
            return
        if len(player1moves) == 5:
            print("\nGame over.\n")
            print("TIE !!!")
            return
        return m2(x,player2moves)
def m2(x,player2moves):    
    
    print(x)
    move2=input(f"Where do you want to place your mark {player2} ? ")
    if move2 in markedspaces :
        print("\nThis space has already marked.\n")
        return m2(x,player2moves)
    else:
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
                print("\nInvalid coordinate please enter a number 1 to 9.\n")
                return m2(x,player2moves)
        markedspaces.append(move2)
        player2moves.append(move2)
        
        if "1" in player2moves and "2" in player2moves and "3" in player2moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player2}, you won with no effort at all!")
            return
        elif "4" in player2moves and "5" in player2moves and "6" in player2moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player2}, you won with no effort at all!")
            return
        elif "7" in player2moves and "8" in player2moves and "9" in player2moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player2}, you won with no effort at all!")
            return
        elif "1" in player2moves and "4" in player2moves and "7" in player2moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player2}, you won with no effort at all!")
            return
        elif "2" in player2moves and "5" in player2moves and "8" in player2moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player2}, you won with no effort at all!")
            return
        elif "3" in player2moves and "6" in player2moves and "9" in player2moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player2}, you won with no effort at all!")
            return
        elif "1" in player2moves and "5" in player2moves and "9" in player2moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player2}, you won with no effort at all!")
            return
        elif "3" in player2moves and "5" in player2moves and "7" in player2moves :
            print(x)
            print("\nGame over.\n")
            print(f"Congrulations {player2}, you won with no effort at all!")
            return    
        return m1(x,player1moves)
    
while True :
    m1(x,player1moves)
    break


#x="""
#     |     |     
#     |     |     
#_____|_____|____
#     |     |    
#     |     |    
#_____|_____|____
#     |     |    
#     |     |    
#     |     |    
#"""
#1,2,3
#4,5,6
#7,8,9
#1,5,9
#3,5,7
#1,4,7
#2,5,8
#3,6,9
#
#