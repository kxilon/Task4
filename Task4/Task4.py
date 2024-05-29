

with open('D:\inputTask4.txt', 'r') as f:
    file = f.read().split("\n")
a = [int(x) for x in file]




m = sorted(a)[len(a) // 2]
counter = 0

for i in range(len(a)):
    if m != i:
        counter += abs(m - a[i])

print(counter)