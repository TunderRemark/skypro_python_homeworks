def bank(x, y):
    for i in range(y):
        x = x * (1 + 0.1)
    print(x)


bank(1000, 5)
