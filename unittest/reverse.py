# Тестируемая функция
def reverse(s):
    if type(s) != str:
        raise TypeError('Expected str, got {}'.format(type(s)))

    return s[::-1]

# # Тестируемая функция
#def reverse(s):
#   return int(s)/1


if __name__ == '__main__':
    print(reverse(42))