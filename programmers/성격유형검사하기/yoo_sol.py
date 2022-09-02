
survey =["AN", "CF", "MJ", "RT", "NA"]
choices=[5,3,2,7,5]
dic={
  '1':{'R':0,'T':0},
  '2':{'C':0,'F':0},
  '3':{'J':0,'M':0},
  '4':{'A':0,'N':0},
}
result=''

for i in range(len(survey)):
  survey[i]
  choices[i]
  if choices[i]<=3:
    indicator=survey[i][0]
    for d in dic:
      for key in dic[d].keys():
        if key==indicator:
          dic[d][key]+=abs(choices[i]-4)
      
  elif choices[i]>=5:
    indicator=survey[i][1]
    for d in dic:
      for key in dic[d].keys():
        if key ==indicator:
          dic[d][key]+=(choices[i]-4)

for d in dic:
  tmp=-1
  for key,val in dic[d].items():
    if val>tmp:
      tmp=val
  for key,val in dic[d].items():
    if val==tmp:
      result+=key
      break
print(result)


