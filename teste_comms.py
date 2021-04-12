from worldstate import world
from server import proxy

ws = world.World()

proxy = proxy.Proxy()
proxy.main()

while True:
    msg = proxy.getMessagesFromAgent('1')
    if msg != '':
        print(msg)
        print("\n")