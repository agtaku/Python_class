ch = 'y'
while ch == 'y':
  Lrange = int(input("Enter low range value: "))
  Hrange = int(input("Enter High range value: "))
  l = []
  for n in range(Lrange, Hrange+1 ):

    c = len(str(n))
    temp = n
    s = 0

    while temp > 0:
        p = temp % 10
        s += p ** c
        temp //= 10

    if n == s:
        l.append(n)
  print("\nArmstrong Numbers in range  "+str(Lrange)+" - "+str(Hrange)+"  are below -\n\n ")
  for num in l:
      print(num,",",end='')
  ch = input("\n\n\tDo you want to continue - y/n  :")
~
