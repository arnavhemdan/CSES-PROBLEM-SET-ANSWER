S=input()
j=1
i=0
count=1
l=len(S)
ans=0
while j<l :
     
    if S[i]==S[j]:
        count+=1    
    else:
        ans=max(ans,count)
        count=1
        i=j
    j+=1
ans=max(ans,count)
      
print(ans)     