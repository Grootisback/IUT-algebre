x = [4,3,2,1]
y = [2,4,6,8]
print(x)
print(y)

z = x + [7,8]
print(z)
print([12] + x + [9] + y)
print([3]*4)
#création d'une liste vide
v = []
print(v)

y[0]
y[2]
y[0:3]
y[1:3]
y[2:3]
y[1:]
y[2:]

w = x
w[2]=88
print(x)
x = [4,3,2,1]
w[:]=x
w[2]=88
print(x)
print(w)
#les commandes suivantes renvoient la même liste
[0,1,2,3]
list(range(0,4))
list(range(4))
#si on souhaite créer une séquence avec un pas différent de 1 :
list(range(12,2,-1))
list(range(1,9,2))
def pm(a,b):
   plus = a+b
   moins = a-b
   return plus, moins

   def nulpos(liste:list)-> list:
    for i in range (0,len(liste)):
        if liste[i] > 0:
            liste[i]=0
    return liste
    print(nulpos([0,2,-3,5,-8,-9,2]))

    def puiss(liste:list)->list:
    i=0
    while i<len(liste):
        liste[i]=liste[i]**(i+1)
        i+=1
    return liste
        
print(puiss([1,5,3,4,8]))


def nbre_pairs(liste:list)->int:
    i=0
    compt=0
    while i<len(liste):
        if (liste [i])%2==0:
            compt+=1
        i+=1
    return compt
print(nbre_pairs([2,8,5,6,7]))

def minval(liste:list)->int:
    i=0
    nbreMin=liste[0]
    position=0
    while i<len(liste):
        if nbreMin > liste[i]:
            nbreMin=liste[i]
            position=i
        i=i+1
        
    return  nbreMin, position 
print(minval([0,5,6,10,-2]))

def algoeucli(a:int, b:int)->int:
    c=a%b
    while c!=0:
        a=b
        b=c
        c=a%b
    return b
    
print(algoeucli(600,50))
algoeucli(15,10)