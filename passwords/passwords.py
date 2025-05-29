import random
import string


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    user_length = input("Введите длину пароля (по умолчанию 12): ")
    try:
        length = int(user_length)
    except ValueError:
        length = 12

    password = generate_password(length)
    print(f"\n🔐 Ваш сгенерированный пароль: \n\n{password}\n")
