import string

#input not contain spaces
p = "theuniversityofinformationtechnology".upper()
k = "vigenere".upper()

def encrypt(p, k):
    k_length = len(k)
    k_int = [ord(i) for i in k]
    p_int = [ord(i) for i in p]
    c = ''
    for i in range(len(p_int)):
        value = (p_int[i] + k_int[i % k_length]) % 26
        c += chr(value + 65)
    return c
 
print encrypt(p,k)

c = "ababa".upper()
def decrypt(c, k):
    k_length = len(k)
    k_int = [ord(i) for i in k]
    c_int = [ord(i) for i in c]
    p = ''
    for i in range(len(c_int)):
        value = (c_int[i] - k_int[i % k_length]) % 26
        p += chr(value + 65)
    return p
