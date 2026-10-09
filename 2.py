n = int(input())
arr = [int(input()) for _ in range(n)]
avg = sum (arr) / n
greater = sum(1 for x in arr if x > avg)
less = sum(1 for x in arr if x < avg)
print(greater - less)