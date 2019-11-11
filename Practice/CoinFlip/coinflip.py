import random

def toss():
    coin = 0
    toss_total = 0
    while coin == 0:
        coin = random.randint(0, 1)
        toss_total += 1
    
    return toss_total

def main():
    total = 0
    for i in range(10000):
        total += toss()
    
    print(total/10000)
        
main()
input()