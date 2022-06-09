def alternate_beads(necklace, num):
    silver = 0
    pink = 0
    for x in necklace:
        if x == 0:
            silver+=1
        else:
            pink+=1
    difference = abs(silver - pink)
    if num == difference:
        return True
    else:
        return False
