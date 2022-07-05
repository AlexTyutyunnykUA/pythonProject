def XOR_cipher(message: str, key: int):
    if type(key) != int:
        return 'Key should be type of integer'
    if key < 1 or key > 128:
        return 'Key should be number from 1 until 128'

    num_list = [ord(char) for char in message]
    encrypt_list = [num ^ key for num in num_list]
    return ''.join([num.to_bytes((num.bit_length() + 7) // 8, 'big').decode() for num in encrypt_list])


message = XOR_cipher('hello',23)
message = XOR_cipher(message,23)
print(message)
