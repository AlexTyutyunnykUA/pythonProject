def is_prime(num:int):
    if num < 0 or num > 1000:
        return 'Число должно быть в границах от 0 до 1000'

    if num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num < 2:
        return False
    return True

print(is_prime(163))
