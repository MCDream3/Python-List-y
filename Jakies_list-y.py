#sposób 1
x = list(range(5))
for item in x:
  print(item)

#sposób 2
  
for item2 in range(4):
  print(item2)

#sposób 3 []
  
print(len(x))

#sposób 4

for i in range(len(x)):
  print(x)

# deklaracja i interacja listy

L = [3, 5, 8, 13, 17, 27]

for elem in L:
  print(elem, end="")

  print("\n")

for i in range(len(L)):
  print(L[i], end="")

# funkcje w listach

# append

A = [4, 7, 5, 7, 3, 3, 2, 8, 7]
print(A)

A.append(3)
print(A)
print("\n")

#count

C = [4, 7, 5, 7, 3, 3, 2, 8, 7]
print(C)

C.count(7)
print(C)
print("\n")

#index

I = [4, 7, 5, 7, 3, 3, 2, 8, 7]
print(I)

I.index(7)
print(I)
print("\n")

#insert

N = [4, 7, 5, 7, 3, 3, 2, 8, 7]
print(N)

N.insert(2,4)
print(N)
print("\n")

#pop

P = [4, 7, 5, 7, 3, 3, 2, 8, 7]
print(P)

P.pop() #domyślnie usunie ostatnią
print(P)
print("\n")

#reverse

R = [4, 7, 5, 7, 3, 3, 2, 8, 7]
print(R)

R.reverse()
print(R)
print("\n")

#sort

S = [4, 7, 5, 7, 3, 3, 2, 8, 7]
print(S)

S.sort() #lub sort(reverse=True) <-- malejąco
print(S)
print("\n")

# usuń z listy wszystkie 7

R = [4, 7, 5, 7, 3, 3, 2, 8, 7]
print(R)

for i in range(R.count(7)):
  R.remove(7)
print(R)

#sposób 2

K = [4, 7, 5, 7, 3, 3, 2, 8, 7]
print(K)

for i in range(K.count(7)):
  K.pop(K.index(7))
print(K)

#wyszukaj max w tablicy

B = [4, 7, 5, 7, 3, 3, 2, 8, 7]
print(B)

print(max(B))

#sposób 2

maxik=B[0]
for i in K:
  if i > maxik:
    maxik=i
print(maxik)

#sposób 3

maksik=B[0]
for i in range(len(B)):
  if B[i]>maksik:
    maksik=B[i]
print(maksik)