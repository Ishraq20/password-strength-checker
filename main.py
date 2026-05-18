import hashlib

def check_password_strength(password):
    reasons = []
    
    if len(password) < 8:
        reasons.append("Minimum length must be 8 characters.")
        
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        reasons.append("Must contain at least one uppercase letter.")
        
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        reasons.append("Must contain at least one lowercase letter.")
        
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        reasons.append("Must contain at least one number.")
        
    special_characters = "!@#$%^&*_-"
    has_special = False
    for char in password:
        if char in special_characters:
            has_special = True
            break
    if not has_special:
        reasons.append(f"Must contain at least one special character ({special_characters}).")
        
    return reasons

def check_jwt_secret_strength(secret):
    reasons = []
    common_weak_values = ["admin", "123456", "password", "secret", "jwtsecret"]
    
    if secret.lower() in common_weak_values:
        reasons.append("Value is a common weak password (e.g., admin, 123456, secret).")
        return reasons
        
    if len(secret) < 16:
        reasons.append("Minimum length must be 16 characters.")
        
    has_upper = False
    for char in secret:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        reasons.append("Must contain uppercase letters.")
        
    has_lower = False
    for char in secret:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        reasons.append("Must contain lowercase letters.")
        
    has_digit = False
    for char in secret:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        reasons.append("Must contain numbers.")
        
    special_characters = "!@#$%^&*_-"
    has_special = False
    for char in secret:
        if char in special_characters:
            has_special = True
            break
    if not has_special:
        reasons.append("Must contain special characters.")
        
    return reasons

def generate_sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def main():
    print("=== Security Checker CLI Tool ===")
    
    user_password = input("Enter Password: ")
    password_errors = check_password_strength(user_password)
    
    if len(password_errors) == 0:
        print("Password is strong")
        pwd_hash = generate_sha256_hash(user_password)
        print(f"Hash: {pwd_hash}")
    else:
        print("Password is weak")
        for error in password_errors:
            print(f" - {error}")
            
    print("-" * 40)
    
    user_secret = input("Enter JWT Secret: ")
    secret_errors = check_jwt_secret_strength(user_secret)
    
    if len(secret_errors) == 0:
        print("JWT Secret is strong")
    else:
        print("JWT Secret is weak")
        for error in secret_errors:
            print(f" - {error}")

if __name__ == "__main__":
    main()
