# while Loop
count=1
while count <=6:
    print(count)
    count +=1
# Nested Loops
for i in range(1,3):
  for j in range(2,4):
   print(i)
   #break Statement
   for i in range(1,6): 
    if i==4:
     break
    print(i)
    #continue Statement
    for x in range(1,4):
     if x == 3:
        continue
    print(x)