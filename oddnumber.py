


try:
    l = int(input().strip())
    r =int(input().strip())
except(EOFError):
    l=""
    r=""


def oddNumbers(l, r):
    for num in range (l, r+1):
        if num%2!=0:
            print(num)
    return num

oddNumbers(l,r)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    res = oddNumbers(l, r)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()