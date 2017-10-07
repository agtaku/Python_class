ch = 'y'
while ch == 'y':
  Lrange = int(input("Enter low range value: "))
  Hrange = int(input("Enter High range value: "))

  for n in range(Lrange, Hrange + 1):

    c = len(str(n))
    temp = n
    s = 0

    while temp > 0:
        p = temp % 10
        s += p ** c
        temp //= 10

    if n == s:
        print(n)
    else:
        print("There is no Armstrong number in that range")
        break

ch = input("Do you want to continue : y/n")