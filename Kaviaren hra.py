import random
N=1
C=5
M=500
a=80
V=3
q=70
Z=1
rent=50
Ml=1000
moneyz=500
D=1


while moneyz >-100:
    go=False
    Ml=1000+Z*500
    if q>100:
        Ml=Ml*1.2
    elif q>80:
        Ml=Ml*1.1
    elif q<60:
        Ml=Ml*0.9
    elif q<50:
        Ml=Ml*0.8
    elif q<40:
        Ml=0
    I= random.uniform(0.8,1.2)
    P = I*N*(C*(M-a*C)-V*(M-a*C)-q*Z-rent)
    moneyz= moneyz+P
    print("Day: ", D)
    print("Todays profit: ", P)
    print("Saved up: ", moneyz)
   
    while go ==False:
        action=input("Any changes?")
        if action=="Ad campaign":
            moneyz-=100
            M+=50
        elif action=="coffee quality+":
            a-=15
            V+=1
        elif action=="coffee quality-":
            a+=15
            V-=1
        elif action=="recruitment":
            Ml+=500
            Z+=1
        elif action=="fire somebody":
            Ml-=1000
            Z-=1
        elif action=="salary":
            q=int(input("How much should they earn?"))
        elif action=="set price":
            C=float(input("New price: "))
        elif action=="expand":
            moneyz-= 1000
            N+=1
        elif action=="make it fancy":
            moneyz -=500
            a-=15
            M+=100
            rent+=50
        elif action=="ok":
            go =True
        elif action=="Even thou this game is excelent I do not wish to play it for the time being": 
            quit()
        else:
            print("wrong command") 
        

    
    D +=1
