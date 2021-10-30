n = int(input())
m = int(input())
ma = [[int(j) for j in input().split()] for i in range(n)]  # make the Matrix

s = input().split()
k = int(s[0])
l = int(s[1])
for i in range(len(ma)):
    ma[i][k], ma[i][l] = ma[i][l], ma[i][k]  # column exchenge

for i in ma:
    print(' '.join(map(str, i)))  # print the matrix