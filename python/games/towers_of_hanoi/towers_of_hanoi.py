numDisks = 5

pegA = [disk for disk in range(numDisks-1, -1, -1)]
pegB = []
pegC = []

print(pegA)

def move(peg1, peg2):
    """!
    Performs a legal move between peg1 and peg2.
    """
    if len(peg2) > 0 and \
        (len(peg1) < 1 or \
            peg2[-1] < peg1[-1]
            ):
        peg1.append(peg2.pop())
    else:
        peg2.append(peg1.pop())

def isSuccess(peg):
    """!
    Checks if the amount of disks is on peg.
    """
    if len(peg) == numDisks:
        return True
    return False

while True:

    # even number of disks
    if numDisks%2 == 0:
        move(pegA, pegB)
        if isSuccess(pegC):
            break
        move(pegA, pegC)
        if isSuccess(pegC):
            break
    else:
        move(pegA, pegC)
        if isSuccess(pegC):
            break
        move(pegA, pegB)
        if isSuccess(pegC):
            break
    move(pegB, pegC)
    if isSuccess(pegC):
        break

print(pegA)
print(pegB)
print(pegC)
