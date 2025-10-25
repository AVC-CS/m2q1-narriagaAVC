def getPivot(number):
    number.sort()
    pivot = number[len(number) // 2]
    return pivot

def split(number):
    

def main():
    # number = list(map(int, input().split()))
    number = [65, 15, 10, 20, 40, 55]
    number = split(number)
    print(number)


if __name__ == '__main__':
    main()
