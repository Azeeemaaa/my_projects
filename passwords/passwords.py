import random
import string


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    user_lenght = input("Введите длину пароля (по умолчанию 12): ")
    try:
        length = int(user_lenght)
    except ValueError:
        lenght = 12

    password = generate_password(length)
    print(f"🔐 Ваш сгенерированный пароль: {password}")
