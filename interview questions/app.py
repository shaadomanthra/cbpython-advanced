# def hey(a):
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if a[i][j] == 0:
#                 zeros(i, j, a)
#     for i in a:
#         print(i)


def zeros(k, l, a):
    for i in range(len(a)):
        for j in range(len(a)):

            if j == l:
                if a[i][j] == 1:
                    a[i][j] = 0


a = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

# hey(a)
a = 5
b = []

for i in range(a):
    c = []
    for j in range(i + 1):
        if j == 0 or j == i:
            c.append(1)
            print(c,'if block')
        else:
            c.append(b[i - 1][j - 1] + b[i - 1][j])
            print(c,'else block')
    b.append(c)
    print(b,' -b- ')
print(c)
print(b)
# [1, 4, 6, 4, 1]
# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
