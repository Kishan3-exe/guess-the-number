import random

wn = random.randint(1,100)

u1 = input("Enter Player 1 name:")
u2 = input("Enter Player 2 name:")

u11 = int(input("Enter Player 1 Number:"))
u22: int = int(input("Enter Player 2 Number:"))

ub1 = 100
print("Player 1 balance is ",ub1)
u111: int=int(input("Enter Player 1 Money "))
ub2 = 100
print("Player 2 balance is ",ub2)
u222: int=int(input("Enter Player 2 Money "))

u = u111+u222

print("Winning Number is::",wn)

if wn == u11:
    print(u1," is Winner ")
    ub = 100 - u111
    ucb = ub + u
    print("Player 1 ballence is:",ucb)
    ubb = 100 -u222
    print("Player 2 ballence is:",ubb)
else:
    if wn == u22:
        print(u2,"is Winner")
        ub = 100 - u222
        ucb = ub + u
        print("Payer 2 ballence is:", ucb)
        ubb = 100 - u111
        print("Player 1 ballence is:", ubb)
    else:
        print("You are loss!!")
        ub1 = 100 - u111
        ub2 = 100 - u222
        print("Player 1 Balance is:",ub1)
        print("Player 2 Balance is:",ub2)


