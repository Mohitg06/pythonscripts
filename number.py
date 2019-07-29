import os

k = int(input().strip())
arr = [int(i) for i in input().split()]


def findNumber(arr, k):
    if k in arr:
        print("YES")
    else:
        print("NO")


findNumber(arr, k)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     arr_count = int(input().strip())
#
#     arr = []
#
#     for _ in range(arr_count):
#         arr_item = int(input().strip())
#         arr.append(arr_item)
#
#     k = int(input().strip())
#
#     res = findNumber(arr, k)
#
#     fptr.write(res + '\n')
#
#     fptr.close()
#
#
