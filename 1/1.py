from pwn import *                                    # 导入 pwntools。
context(arch='amd64', os='linux', log_level='debug') # 一些基本的配置。
# io = process('./pwn')             # 在本地运行程序。
# gdb.attach(io)                    # 启动 GDB
io = connect("127.0.0.1",37949)          

io.recvuntil(b"hint.")
num = io.recv(8)
print(num)
num = u64(num.ljust(8,b"\x00")) 
print(num)
print(1)
print(str(num).encode)                      
io.sendline(str(num)) 

io.interactive()                