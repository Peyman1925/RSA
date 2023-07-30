def Inverse(a,b):
    for i in range(b):
        if (i*a%b)==1:
            a = i
            break
    return a
     
def For_Big_Power_in_mod(input,pow,n):
    input = input%n
    
    a = 1
    while pow>0:
        
        a*=input
        a = a%n
        pow = pow-1
    return a%n    
def To_Bin(a):
    a_bin = []
    b_bin = []
    x = 0
    while a>=1:
        a_bin.append(a%2)
        b = a/2
        a = int(b)
        if(a<1): x = a
    a_bin.append(x)
    for i in reversed(a_bin) :
        b_bin.append(i)
    b_bin.remove(0)    
    return b_bin 

def str_to_bin(a):
    stri = ""
    b = To_Bin(a)
    c = []
    for i in range(len(To_Bin(a))):
        
        b[i] = str(b[i])
        stri = stri+b[i]
    return stri 


plain = 'Peyman Veysi'
print("Plinetext: ", plain)
plain = [ord(char)-96 for char in plain.lower()]
print("binary Plaintext : ",end = "")
for i in range(len(plain)):
    print(str_to_bin(plain[i]),end = "")


p = 251
print('\n',"P = ",str_to_bin(p))
q = 521
print("Q = ",str_to_bin(q))
n = p*q
print("N = ",str_to_bin(n))
phi = (p-1)*(q-1)
print("Phi = ",str_to_bin(phi))
e = 2
for i in range(100,phi):
    if phi%i!=0:
        e = i
        break


print("Public key = ",str_to_bin(e))
Ciphertext = []
for i in range(len(plain)):
    Ciphertext.append(For_Big_Power_in_mod(plain[i],e,n))

print("Ciphertext : ",end = "")
for i in range(len(Ciphertext)):
    print(str_to_bin(Ciphertext[i]),end="")

d = Inverse(e,phi)

print('\n',"Private key = ",str_to_bin(d))

message = []
for i in range(len(plain)):
    message.append(For_Big_Power_in_mod(Ciphertext[i],d,n))
    message[i] = chr(message[i]+96)

print("message : ", end="")
for i in range(len(message)):
    print(message[i],end ="")
