import time
def countdown(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
    print("Time’s up!")
s=int(input())
countdown(s)
