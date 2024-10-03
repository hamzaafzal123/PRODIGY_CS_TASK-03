import re

def check_password_strength(password):
   
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

   
    score = 0
    if length_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    
    if score == 5:
        return "Password Strength: Very Strong", score
    elif score == 4:
        return "Password Strength: Strong", score
    elif score == 3:
        return "Password Strength: Moderate", score
    elif score == 2:
        return "Password Strength: Weak", score
    else:
        return "Password Strength: Very Weak", score

def password_feedback(password):
    feedback = []
    
   
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    
    
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    
    
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    
    
    if not re.search(r'\d', password):
        feedback.append("Password should contain at least one digit.")
    
   
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password should contain at least one special character.")
    
    return feedback

if __name__ == "__main__":
    
    password = input("Enter a password to check its strength: ")
    
    
    strength, score = check_password_strength(password)
    print(strength)
    
   
    if score < 5:
        print("\nSuggestions to improve your password:")
        for suggestion in password_feedback(password):
            print(f"- {suggestion}")
