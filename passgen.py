import secrets
import string


def generate_password(length=16, use_digits=True, use_symbols=True):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if length < 4:
        raise ValueError("Password length must be at least 4.")

    return "".join(secrets.choice(characters) for _ in range(length))


def main():
    print("🔐 Secure Password Generator")
    print("-" * 30)

    try:
        length = int(input("Password length [16]: ") or 16)

        digits = input("Include numbers? [Y/n]: ").lower() != "n"
        symbols = input("Include symbols? [Y/n]: ").lower() != "n"

        password = generate_password(
            length=length,
            use_digits=digits,
            use_symbols=symbols
        )

        print("\nGenerated password:")
        print(password)

    except ValueError as error:
        print(f"\n❌ Error: {error}")


if __name__ == "__main__":
    main()
