#N = 6 , numlist = [3, 2, 5, 6, 1, 4]

#1 2 3 4 5 6   // 그대로 들어가고
#3 2 5 6 1 4
#5 -> 1
#2 -> 2
#6 -> 4
#3 -> 5
#1 -> 3
#4 -> 6
#5 2 1 4 3 6

# N, K 공백으로 입력받음
n = map(int, input())
k = input().split()
numlist = [3, 2, 5, 6, 1, 4]
count = 0

for i in k:
    for j in range(len(numlist)):
        #if i == numlist[j]:
            #count += 1
            #print(i)
            print(numlist[j])

print(count)
