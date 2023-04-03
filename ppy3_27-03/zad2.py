import math

def prime(*numbers):
    for number in numbers:
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
    prime(1,2,3,4,5,6,7,8,9,10,11,12,13,15,17,18,19,23,24,25,29,30)