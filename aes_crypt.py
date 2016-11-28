import sys
from Crypto.Cipher import AES
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 

argc = len(sys.argv)
print argc
if(argc != 4) :
    print 'Usage: python %s filename key iv' % sys.argv[0]
    quit()

key = sys.argv[2]
iv = sys.argv[3] #initialize vector

f = open(sys.argv[1], 'rb')
binary = f.read()
binary = pad(binary)
cipher = AES.new(key, AES.MODE_CBC, iv)

encrypted = cipher.encrypt(binary);
f = open('encrypted.png', 'wb')
f.write(encrypted)
f.close()

