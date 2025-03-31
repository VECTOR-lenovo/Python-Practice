def decimal_to_binary(n):
    if n == 0:
        return 0
    binary = []
    while n > 0:
        bits=n % 2
        binary.append(bits)
        n = n // 2
    binary.reverse()
    for i in binary:
        print(i, end="")
n=int(input("Enter the number: "))
decimal_to_binary(n)
