a=[[1,0,1,0],[0,1,1,0],[0,0,1,1]]
printed = []
for i in range(0, len(a)):
   sum1 = 0
   if a[i][0] == 1:
       sum1 += 8
   if a[i][1] == 1:
       sum1 += 4
   if a[i][2] == 1:
       sum1 += 2
   if a[i][3] == 1:
       sum1 += 1
   printed.append(sum1)
print(printed)
