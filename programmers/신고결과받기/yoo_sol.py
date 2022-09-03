id_list =["con", "ryan"]
report =["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
result =[]

#report배열 중복제거
report =list(set(report))

#신고를 한사람
#신고를 당한사람 딕셔너리
reporter=[]
reportedDic={}
for a in report:
  er=a.split(' ')[0]
  ed=a.split(' ')[1]
  reporter.append(er)
  reportedDic[ed]=reportedDic.get(ed,0)+1

#정지당한사람
stoped =[]
for key,val in reportedDic.items():
  if val>=k:
    stoped.append(key)

#신고안한사람이 받을 통보를 저장한 dic
notreporter={}
for a in id_list:
  if a not in reporter:
    notreporter[a]=notreporter.get(a,0)


#신고한사람이 받을 통보를 저장한 dic
reporterDic={}
for a in report:
  er=a.split(' ')[0]
  ed=a.split(' ')[1]
  if ed in stoped:
    reporterDic[er]=reporterDic.get(er,0)+1
  reporterDic[er]=reporterDic.get(er,0)

#신고안한애가 받을통보 + 신고한애가 받을통보 합치기
Alldic = dict(reporterDic,**notreporter)

#id_list순서대로 출력
for a in id_list:
  for key,val in Alldic.items():
    if a==key:
      result.append(val)
print(result)
