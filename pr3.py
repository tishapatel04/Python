
# Tisha Patel 20CE106 
p=int(input())  # taking input for p
s=map(int,input().split())  # input for room list
s=sorted(s)  # sorting the list

for i in range(len(s)):
    if(i!=len(s)-1):
      if(s[i]!=s[i-1] and s[i]!= s[i+1]):
          print(s[i])
          break;   
    else:
         print(s[i])
