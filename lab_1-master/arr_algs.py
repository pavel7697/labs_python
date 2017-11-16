
arr = [8, 4, -15, -33, -5, 1, 0, 14]
x=min(arr)
y=max(arr)
print(x)
print(y)
def avg (arr):
    i = 0
    m = 0
    while i<len(arr):
        m+=arr[i]
        i+=1
    n=m/len(arr)
    print(n)
avg (arr)
