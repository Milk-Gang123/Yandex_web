from werkzeug.security import generate_password_hash, check_password_hash

#password = input("Введите новый пароль?")
# Создаем хэш для пароля:
hashed_password = "pbkdf2:sha256:260000$JeiAtXd3KQQmdF46$51f537f1cd696090772813080738aea57ba37b8c992171550a34bb0c42f7b4cf"
# Выводим хэш:
print(hashed_password)
bool_check = False
while not bool_check:
    check_password = input("Введите пароль:")
    # Проверяем пароль на правильность:
    bool_check = check_password_hash(hashed_password,
                                        check_password)
    # Сообщаем пользователю результат и заодно отслеживаем хэш:
    if bool_check:
        print("Пароль верный! У него хэш:")
    else:
        print("Неверный пароль! У него хэш:")
    print(generate_password_hash(check_password))
