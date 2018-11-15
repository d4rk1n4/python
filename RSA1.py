#!/usr/bin/python2
from Crypto.PublicKey import RSA
import gmpy2

def long2Text(number, size):
    text = "".join([chr((number >> j) & 0xff) for j in reversed(range(0, size << 3, 8))])
    return text.lstrip("\x00")

C = 'raUcesUlOkx/8ZhgodMoo0Uu18sC20yXlQFevSu7WFDxIy0YRHMyXcHdD9PBvIT2aUft5fCQEGomiVVPv4I'

p = 11
q=17
N=p*q

r=(p-1)*(q-1)
e = 7
d = long(gmpy2.divm(1, e, r))

rsa = RSA.construct((N,e,d,p,q))
pt = rsa.decrypt(C)

print pt
print long2Text(pt,100)
