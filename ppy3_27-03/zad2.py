import math

def prime(number):
    is_prime = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break

    if number < 2:
        is_prime = False

    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")

if __name__ == '__main__':
    for i in range(0, 100):
        prime(i)