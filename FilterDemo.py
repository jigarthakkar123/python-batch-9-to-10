def oddeven(x):
    if x%2==0:
        return x

l=[1,2,3,4,5,6,7,8,9]

ans=filter(oddeven,l)

print(list(ans))
