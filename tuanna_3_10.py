primes_list = [2]
count = 0
prime_number = 3
while len(primes_list) < 10:
    for i in primes_list:
        if prime_number % i == 0:
            break
    else:
        primes_list.append(prime_number)
    prime_number +=1
print primes_list
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]