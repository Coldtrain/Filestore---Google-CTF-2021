# Filestore   Google CTF 2021
My quick and dirty solution to Filestore, Life has kept me busy so i didn't get a chance to do this writeup, maybe soon.

Code written during the 2021 Google CTF.

Deduplication is the process of storing large amounts of data but removing duplicates / repeating data while having all copies point to one index; By doing so allows databases and backup solutions to save on immense amounts of storage space.

The exploit in this CTF is that deduplication is its own worst enemy.

Google gives you a "file storage" service which you can access through netcat.

![filestore](https://user-images.githubusercontent.com/6278490/148488468-09e21255-5e94-4bbb-a8c0-fbe6b318ef88.JPG)


However once playing around with it you will notice storage size increases only when entering non matching characters.

Both python scripts connect to the Google CTF Python TCP socket server using PwnTools, this is a much simpler and more efficient alternative then using python sockets to send and recieve TCP buffers. (you do not need to specify the TCP buffer size you are waiting for etc.)


PwnTools is an advanced Python library for writing exploits and payloads.

The first python script valid.py loops through all ascii letters one by one and closes the connection to the server, each character which did not increase storage size was already stored by admin. simple.

once it returns all found characters I take this string and store it into a array inside of solver.py

This python script essentialy loops repeating the same process but inserting a new character from the foundChars Array to the start of the Flag string until the entire flag is leaked. (each loop it is checking the bytes stored.)
