n = int(input("ENTER A NUMBER::"))

print("*************** HALF PYRAMID STAR PATTERN ***************")
for i in range(1, n+1):
    for j in range(1, i+1):
        print("* ", end="")
    print("")

print("*************** HALF INVERTED PYRAMID STAR PATTERN ***************")
for i in range(1, n+1):
    for j in range(n+1, i, -1):
        print("* ", end="")
    print("")

print("*************** MIRRORED HALF PYRAMID STAR PATTERN ***************")
for i in range(1, n+1):
    for j in range(n, i, -1):
        print("  ", end="")
    for j in range(1, i+1, 1):
        print("* ", end="")
    print("")

print("*************** MIRRORED HALF INVERTED PYRAMID STAR PATTERN ***************")
for i in range(1, n+1):
    for j in range(2, i+1):
        print("  ", end="")
    for j in range(n+1, i, -1):
        print("* ", end="")
    print("")

print("*************** HALF HOLLOW PYRAMID STAR PATTERN ***************")
for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1 or j == i or i == n:
            print("* ", end="")
        else:
            print("  ", end="")
    print("")

print("*************** HALF HOLLOW INVERTED PYRAMID STAR PATTERN ***************")
for i in range(1, n+1):
    for j in range(i, n+1):
        if i == 1 or j == i or j == n:
            print("* ", end="")
        else:
            print("  ", end="")
    print("")

print("*************** MIRRORED HALF HOLLOW PYRAMID STAR PATTERN ***************")
for i in range(1, n+1):
    for j in range(n, i, -1):
        print("  ", end="")
    for j in range(1, i+1):
        if j == 1 or i == n or j == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print("")

print("*************** MIRRORED HALF INVERTED HOLLOW PYRAMID STAR PATTERN ***************")
for i in range(1, n+1):
    for j in range(2, i+1):
        print("  ", end="")
    for j in range(i, n+1):
        if j == n or i == 1 or j == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print("")
