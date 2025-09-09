def check_password(password):
    if len(password) < 8:
        return "Weak: Less than 8 characters"
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():   
            has_special = True
    if has_upper and has_lower and has_digit and has_special:
        return "Strong Password"
    else:
        return "Weak Password"
print(check_password("Hello123"))      
print(check_password("Hello@123"))     
