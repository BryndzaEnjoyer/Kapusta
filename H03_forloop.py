x=10
for i in "python" :
    print(i)

for i in range(5) :
    print( "hello")

A=["Learning", "python", "is", "fun", "juchuuu"]
for i in range(len(A)) :
    print(A[i])
C= ""

#sentence = "Learning Python is fun"
#for word in sentence.split():
#print(word)

for i in "computer" :
    C = i + C
print(C)

for i, L in enumerate("science") :
    print(i, L)
q=0
for i in "Experience teaches slowly":
    if i == "e" or i == "E":
        q+=1
print(q)

V=0
vovewl = ["a","e","i","o","u"]
for i in "Programming is powerful":
    if i in vovewl:
        V+=1
print(V)

for i, char in enumerate("Artificial Intelligence") :
    if i % 2 != 0 :
        print(char)

K=[]
for i in "Python":
    K.append(i)
    W =" ".join(K)
print(W)

#abcd="abcdefghijklmnopqrstuvwxyz"
secret = "secret"
for i in secret :
    P = ord(i) +1
    E = chr(P)
print(E)