from pwn import *                                    # 导入 pwntools。
context(arch='amd64', os='linux', log_level='debug') # 一些基本的配置。

# 有时我们需要在本地调试运行程序，需要配置 context.terminal。详见入门指北。

# io = process('./pwn')             # 在本地运行程序。
# gdb.attach(io)                    # 启动 GDB
io = connect("127.0.0.1",34769)              # 与在线环境交互。
io.sendline(b'114511')              # 什么时候用 send 什么时候用 sendline？

payload  = p32(0xdeadbeef)          # p32(0xdeadbeef)、b"\xde\xad\xbe\xef"、b"deadbeef" 有什么区别？
                                    # 你看懂原程序这里的检查逻辑了吗？
payload += b'shuijiangui'           # strcmp

io.sendafter(b'password.', payload) # 发送！通过所有的检查。

io.interactive()                    # 手动接收 flag。