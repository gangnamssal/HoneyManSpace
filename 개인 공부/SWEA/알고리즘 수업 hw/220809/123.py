heigh = [5,3,4,9,5,5,2]
for i in range(len(heigh)):
    for j in range(len(heigh)-1):
         if heigh[j] > heigh[j+1]:
            heigh[j], heigh[j+1] = heigh[j+1], heigh[j]
print(heigh)
heigh[0] += 2
print(heigh)