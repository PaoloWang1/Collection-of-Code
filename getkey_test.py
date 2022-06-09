from getkey import getch

while True:
    c = getch()
    print(c[0], ":", chr(c[0]))
    if c==b'\x03':
        break
    if c[0] == 72:
        print("up pressed")
    elif c[0] == 75:
        print("left pressed")
        
