import time
import threading

class Hoop :

    def __init__(self):
        self.time_up = False

    def timer(self, seconds):
        time.sleep(seconds)
        self.time_up = True

    def Greetings(self) : 
        print("HELLO PLAYER! \nWelcome to Hoop")
        x = int(input( "please choose your difficulty to continue : 1.Easy 2.Medium 3.Hard " ))
        return x

    def Rules(self) :
        x = self.Greetings()

        if x == 1 :
            print ( "see you are going easy \nso this mood is basicly the Hoop Game, first you decide who should play first then one by one we enter numbers and in each 5 cycle we should write 'H' (Hoop) ")
            print ( "you have 45 seconds to complete and reach 50 " ) 
            self.Game_eazy()

        if x == 2 :
            print ( "see you are going med \nso this mood is basicly the Hoop Game with a little bit of change,  we enter numbers and in a 3 cycle press 'H' which is short for Hoop" )
            print ( "you have 35 seconds to complete and reach 60 " ) 
            self.Game_medium()

        if x == 3 :
            print ( "see you are going hard \nso this mood is much harder than the basic Hoop Game, we should enter numbers and in a 3 cycle we press 'H' (Hoop) and the cycle increases by 2 in each cycle \nfor example 12H34567H..." )
            print ( "you have 40 seconds to complete and reach 50 " ) 
            self.Game_hard()

    def Game_eazy(self) :
        p = int( input( "and tell who do you want to start first? \n1.me 2.you " ) )

        t = threading.Thread(target=self.timer, args=(45,), daemon=True)
        t.start()

        if p == 1 :
            print ( "START :" )
            
            for i in range(1,51,1) :
                if self.time_up:
                    print("\aYOU LOST! \nTime finished")
                    return
                time.sleep(0.3)
                if i % 5 == 0 and i % 2 == 0 :
                    n = str(input())
                    if n == "H" :
                        continue
                    else :
                        print ( "YOU LOST!" )
                        return
                if i % 5 == 0 :
                    print ( "H" )
                    continue    
                if  i % 2 == 1  :
                    print(i)
                    continue
                else : 
                    k = int(input())
                    if k == i :
                        continue
                    else :
                        print ( "YOU LOST! \nwrong number entered" )
                        return
            print ( "congratulations \nyou won" )
        
        else : 
            print ( "START :" )
            for i in range(1,51,1) :
                if self.time_up:
                    print("\aYOU LOST! \nTime finished")
                    return
                time.sleep(0.3)
                if i % 5 == 0 and i % 2 == 0 :
                    print ( "H" )
                    continue    
                if i % 5 == 0 :
                    n = str(input())
                    if n == "H" :
                        continue
                    else :
                        print ( "YOU LOST!" )
                        return
                if  i % 2 == 0  :
                    print(i)
                    continue
                else : 
                    k = int(input())
                    if k == i :
                        continue
                    else :
                        print ( "YOU LOST! \n wrong number entered" )
                        return
            print ( "congratulations \nyou won" )
    
    def Game_medium(self) :
        p = int( input( "and tell who do you want to start first? \n1.me 2.you " ) )

        t = threading.Thread(target=self.timer, args=(35,), daemon=True)
        t.start()

        if p == 1 :
            print ( "START :" )
            
            for i in range(1,61,1) :
                if self.time_up:
                    print("\aYOU LOST! \nTime finished")
                    return
                time.sleep(0.3)
                if i % 3 == 0 and i % 2 == 0 :
                    n = str(input())
                    if n == "H" :
                        continue
                    else :
                        print ( "YOU LOST! \nYou should have press H" )
                        return
                if i % 3 == 0 :
                    print ( "H" )
                    continue    
                if  i % 2 == 1  :
                    print(i)
                    continue
                else : 
                    k = int(input())
                    if k == i :
                        continue
                    else :
                        print ( "YOU LOST! \nwrong number entered" )
                        return
            print ( "congratulations \nyou won" )
        
        else : 
            print ( "START :" )
            for i in range(1,61,1) :
                if self.time_up:
                    print("\aYOU LOST! \nTime finished")
                    return
                time.sleep(0.3)
                if i % 3 == 0 and i % 2 == 0 :
                    n = str(input())
                    if n == "H" :
                        continue
                    else :
                        print ( "YOU LOST! \nYou should have press H" )
                        return
                if i % 3 == 0 :
                    print ( "H" )
                    continue  
                if  i % 2 == 0  :
                    print(i)
                    continue
                else : 
                    k = int(input())
                    if k == i :
                        continue
                    else :
                        print ( "YOU LOST! \n wrong number entered" )
                        return
            print ( "congratulations \nyou won" )

    def Game_hard(self) :
        p = int( input( "and tell who do you want to start first? \n1.me 2.you " ) )

        t = threading.Thread(target=self.timer, args=(40,), daemon=True)
        t.start()
        x = 5
        b = 3
        a = 0
        if p == 1 :
            print ( "START :" )
            for i in range (1,51,1) : 
                if self.time_up:
                    print("\aYOU LOST! \nTime finished")
                    return
            
                if i == b : 
                    b += x
                    x += 2
                    a+=1
                    if a % 2 == 1 :
                        print ("H")
                    else :
                        n = str(input())
                        if n == "H" :
                            continue
                        else :
                            print ( "YOU LOST! \nYou should have press H" )
                            return
                if  i % 2 == 1  :
                    print(i)
                    continue
                else : 
                    k = int(input())
                    if k == i :
                        continue
                    else :
                        print ( "YOU LOST! \nwrong number entered" )
                        return
            print ( "congratulations \nyou won" )
        
        if p == 2 :
            print ( "START :" )
            for i in range (1,51,1) :
                if self.time_up:
                    print("\aYOU LOST! \nTime finished")
                    return
                
                if i == b : 
                    b += x
                    x += 2
                    a+=1
                    if a % 2 == 1 :
                        n = str(input())
                        if n == "H" :
                            continue
                        else :
                            print ( "YOU LOST! \nYou should have press H" )
                            return
                    else :
                        print ("H")
                if  i % 2 == 0  :
                    print(i)
                    continue
                else : 
                    k = int(input())
                    if k == i :
                        continue
                    else :
                        print ( "YOU LOST! \nwrong number entered" )
                        return
            print ( "congratulations \nyou won" )

h = Hoop()
h.Rules()