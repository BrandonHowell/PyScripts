

def collatz(mNum): # Collatz Function
    if mNum % 2 == 0:
        mNum = mNum/2
    else:
        mNum = (mNum*3) + 1
    return mNum

def main():
    num = int(input("Enter a number: ")) # Main Function
    print(num)
    while(num > 1):
        num = collatz(num)
        print(num)

main()
input()