i=0
for i<=100:
    i=i+1
    if i%7==0:
        continue
    if i%10==7:
        continue
    if i//10==0:
        continue
    print(i)
