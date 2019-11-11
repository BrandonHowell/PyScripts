def freq():
    f = open("freq.txt")
    total = 0
    for line in f:
        total += int(line)
    f.close()
    return total

def main():
    print(freq())

main()
input()