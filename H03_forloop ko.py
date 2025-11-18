x=10
for i in "python" :
    print(i)

for i in range(5) :
    print( "hello")
sentence = "Learning Python is fun"
A=sentence.split(" ")
for i in range(len(A)) :
    print(A[i])
C= ""

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


vovewl = ["a","e","i","o","u"]
idk="Programming is powerful"
for i in idk:
    if i in vovewl:
        print(i)

secstring=""
for i, char in enumerate("Artificial Intelligence") :
    if i % 2 != 0 :
        secstring += char 
print(secstring)

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


s = "loop"
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j])
