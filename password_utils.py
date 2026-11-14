from werkzeug.security import generate_password_hash, check_password_hash

def demo_password_hashing():
    password = "example-password"
    password_hash = generate_password_hash(password)
    print("Password:", password)
    print("Hash:", password_hash)

    print("Correct password check:", check_password_hash(password_hash, "example-password"))
    print("Wrong password check:", check_password_hash(password_hash, "wrong-password"))
