import hashlib

def check_password_strength(password: str) -> list:
    reasons = []
    if len(password) < 8:
        reasons.append("Minimum length must be 8 characters.")
    if not any(char.isupper() for char in password):
        reasons.append("Must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        reasons.append("Must contain at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        reasons.append("Must contain at least one number.")
    special_characters = "!@#$%^&*_-"
    if not any(char in special_characters for char in password):
        reasons.append(f"Must contain at least one special character ({special_characters}).")
    return reasons

def check_jwt_secret_strength(secret: str) -> list:
    reasons = []
    common_weak_values = ["admin", "123456", "password", "secret", "jwtsecret"]
    if secret.lower() in common_weak_values:
        reasons.append("Value is a common weak password (e.g., admin, 123456, secret).")
        return reasons
    if len(secret) < 16:
        reasons.append("Minimum length must be 16 characters for security.")
    if not any(char.isupper() for char in secret):
        reasons.append("Must contain uppercase letters.")
    if not any(char.islower() for char in secret):
        reasons.append("Must contain lowercase letters.")
    if not any(char.isdigit() for char in secret):
        reasons.append("Must contain numbers.")
    special_characters = "!@#$%^&*_-"
    if not any(char in special_characters for char in secret):
        reasons.append("Must contain special characters.")
    return reasons

def generate_sha256_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def main():
    print("\n" + "="*40)
    print("   🛡️  Security Checker CLI Tool  🛡️")
    print("="*40)
    
    user_password = input("\nEnter Password to test: ")
    password_errors = check_password_strength(user_password)
    
    if not password_errors:
        print(" [✓] Password is strong!")
        pwd_hash = generate_sha256_hash(user_password)
        print(f"     ↳ SHA-256 Hash: {pwd_hash}")
    else:
        print(" [✗] Password is weak:")
        for error in password_errors:
            print(f"      - {error}")
            
    print("-" * 40)
    
    user_secret = input("Enter JWT Secret to test: ")
    secret_errors = check_jwt_secret_strength(user_secret)
    
    if not secret_errors:
        print(" [✓] JWT Secret is strong and secure!")
    else:
        print(" [✗] JWT Secret is weak:")
        for error in secret_errors:
            print(f"      - {error}")
    print("="*40 + "\n")

if __name__ == "__main__":
    main()
