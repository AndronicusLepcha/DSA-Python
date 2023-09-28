def isHappy(num):
    slow=num
    fast=num
    
    while True:
        slow=square(slow)
        fast=square(square(fast))

        if slow==fast:
            break

    if slow==1:
        return True
    return False


def square(num):
    ans=0
    while num>0:
        rem=num%10
        ans += rem*rem
        num //= 10
    return ans

num=[10,19,2,13]
for x in num:
    print(isHappy(x))