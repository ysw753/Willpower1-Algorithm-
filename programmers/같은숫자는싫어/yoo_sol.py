arr=[1,1,3,3,0,1,1]

answer=[]

for x in arr:
  if len(answer)==0:
    answer.append(x)
  elif answer[-1]!=x:
    answer.append(x)
print(answer)