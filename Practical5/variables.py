# some simple math


a='020607'
b='190784'
c='210316'
d=b-a
e=c-a

if d-e>0：
    print('d is bigger than e')
elif d-e<0:
    print('e is bogger than d')
else:
    print('d is equals to e')


# booleans
X = True
Y = False
Z = (X and not Y) or (Y and not X)
if Z == True:
    print('True')
else:
    print('False')

W = (X!=Y)
if Z == W:
    print('Z = W')

else:
    print('Z != W')

