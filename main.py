n = int(input("Check this number:"))
def primechecker(nom):
    is_prime=True
    for i in range(2, n - 1):
        if  n % i==0:
            is_prime=False
    if is_prime:
         print("Its prime no.")
    else:
         print("Its not prime no.")
primechecker(n)