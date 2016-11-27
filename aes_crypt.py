import sys
from Crypto.Cipher import AES

argc = len(sys.argv)
print argc
if(argc != 4) :
    print 'Usage: python %s filename key iv' % sys.argv[0]
    quit()

key = sys.argv[2]
iv = sys.argv[3] #initialize vector

f = open(sys.argv[1], 'rb')
binary = f.read()
cipher = AES.new(key, AES.MODE_CBC, iv)

encrypted = cipher.encrypt(binary);
f = open('encrypted.png', 'wb')
f.write(encrypted)
f.close()

