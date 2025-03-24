a = 2
b = 3
a = a + 1
b = a + b
print(a + b)


a = 2
b = 3
a = a * b
b = a**2
print(a + b)

a = 0
b = 1
a = a +


a = 2
b = 3
a = a + b
b =a+b
print (b)

a = 2
b = 3
a = b
b = 2 *a+b**3
print(a,b)

#4
a=0
b=1
c=a
a=b
b=c
print(a,b,c)

#5
def difference(a,b):
    return(a-b)

print(difference(3,2))

def difference(a,b):
    return(a*b)

print(difference(3,2))

#6 deux côtés de même longueur
def est_isocele(a,b,c):
    if a == b or a == c :
     return True
    else:
     return False

print(est_isocele(3,4,2))

def est_rectangle(a,b,c):
    if a*2 + b*2 == c*2 :
     return True
    else:
     return False

print (est_rectangle(2,2,4))



#7
def lpp(a,b):
    if a > b:
     return b
    else:
     if   a < b:
      return a

print(lpp(11,10))

#8
def valeur_absolue(a):
    if a > 0 :
        return a
    else:
     if a < 0 :
         return a * -1

print(valeur_absolue(10))

#9
def est_entier(a):
    if a == int (a) :
     return True
    else:
     return False
print(est_entier(3))

#10
def est_pair(a):
    if a % 2 == 0 :
     return True
    else:
     return False
print(est_pair(1))

#11
def intervalle1(a):
    if a >= -2 & a<=3:
      return True
    else:
     return False
print(intervalle1(4))

#B
def intervalle2(a):
    if a >= -3 and a <= 5:
     return True
    else :
     return False
print(intervalle2(-2))

#c
def intervalle3(a):
    if (-5 <= a <=-3) or (0 <= a <=2):
     return True
    else :
     return False
print(intervalle3(-6))



