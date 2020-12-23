#Franciele de Paula
from Crypto.Util import number
from Crypto.Util.number import *
from Crypto.Random import random 


def exponenciacao(a,x,p):
	resultado = 1
	fator = a
	while x > 0:
		if ((x%2)==1):
			resultado = (resultado * fator) % p
		fator = (fator*fator) % p
		x //= 2
	return resultado

def euclidiano_estendido(a,b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0 

def gerar_expoentes(phi):
	while True:
		e = random.randint(3, phi - 1)
		mdc, x = euclidiano_estendido(e, phi)
		if mdc == 1:
			break 
	if x < 0:
		return e, n + x
	return e, x

if __name__ == '__main__':
	msg = "The RSA algorithm is an asymmetric cryptography algorithm, named after those who invented it in 1978: Ron Rivest, Adi Shamir, and Leonard Adleman. It uses a public key and a private key."
	
	N = 2048
	p = number.getPrime(N)
	q = number.getPrime(N)
	print("P:\n",p,"\nQ:\n",q,"\n")
	n = p*q
	print("N:\n",n)
	phi = (p-1)*(q-1)
	e, d = gerar_expoentes(phi)
	print("\nE:\n",e,"\nD:\n",d)
	m = bytes_to_long(msg.encode('utf-8'))
	c = exponenciacao(m,e,n) #encriptação 
	print("\nTEXTO CIFRADO:\n",c)
	dec = exponenciacao(c,d,n) #decriptação 
	print("\nTEXTO DECRIPTADO:\n",dec,"\n")
	print("\nTEXTO DECRIPTADO CONVERTIDO PARA STRING:\n",(long_to_bytes(dec)))
	



		
