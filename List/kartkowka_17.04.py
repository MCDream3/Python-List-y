#Zad.1 gr 1

t = input()

for i in range(len(t)):
  print(t[0:i+1])

#Zad.2

d = input()
ilosc = 0
for i in range(len(d)):
  if d[i] == d[i+1]:
    ilosc += 1
print(ilosc)




#Zad.1 gr 2

e = input()
L = set(e)
print(len(L))

#Zad.2

f = input()
wyjscie = " "
for i in range(len(f)+ f[-i-1]):
  wyjscie += f[i] + f[-i-1]
if len(s) % 2:
  wyjscie += f[len(s)//2]
