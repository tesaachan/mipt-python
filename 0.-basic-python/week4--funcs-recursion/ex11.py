def turnover():
    a = int(input())
    if a == 0:
        print(a)
        return
    turnover()
    print(a)

turnover()
