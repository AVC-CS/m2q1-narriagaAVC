def getPivot(number):
    number.sort()
    pivot = number[len(number) // 2]
    return pivot

def split(number):
    pivot = getPivot(number)
    leftsub = []
    rightsub = []
    for i in range(len(number)):
        if number[i] < pivot:
            leftsub.append(number[i])
        if number[i] > pivot:
            rightsub.append(i)
    newlist = leftsub + [pivot] + rightsub
    return newlist

def main():
    # number = list(map(int, input().split()))
    number = [65, 15, 10, 20, 40, 55]
    number = split(number)
    print(number)


if __name__ == '__main__':
    main()
