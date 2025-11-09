from pwn import *

context(arch='amd64', os='linux', log_level='debug') # 一些基本的配置。

io = connect("127.0.0.1",45803)