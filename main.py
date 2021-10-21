
import random 
print("--------------------------------------------------------Up/Down Game----------------------------------------------------")
print("main EXP = 100 , at the end of the game if your Exp > 100 you win, EXP = 100 you are a lucky bastard, EXP < 100 you lose")
choix = 0
while (choix!=2) :
    exp = 100
    choix = int(input("choisir une option: \n 1 - Jouer \n 2 - Exit\nOPTION: "))
    
    if (choix == 1):
        y=int(input("saisir le domain: "))
        res= random.randint(1,y)
        x = 0
        k = 0
        while (x!= res):
            x = int(input("Devinez le nombre: "))
            v=str(x)
            #if (v==exit):
             #   break
            if (x < res):
                print("Trop faible!")
                exp = exp - 10
            else:
                if (x > res):
                    print("Trop eleve!")
                    exp = exp + 10
            k+=1
        print("Success!\nResultat: " + str(res))
        print("Nombre d'essais: " + str(k))
        if (exp==100):
            print("you are a lucky bastard! ---> Exp: "+str(exp))
        elif (exp<100):
            print("you lose! ---> Exp: "+str(exp))
        else:
            print("you win! ---> Exp: "+str(exp))
    #print("have a nice day :)")            

