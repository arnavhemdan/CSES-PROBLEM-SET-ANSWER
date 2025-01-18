n=int(input())
arr=list(map(int,input().split()))
ans=0
for i in range(1,n):
    if arr[i-1]>arr[i]:
        diff=arr[i-1]-arr[i]
        ans+=diff
        arr[i]+=diff 
print(ans)        
