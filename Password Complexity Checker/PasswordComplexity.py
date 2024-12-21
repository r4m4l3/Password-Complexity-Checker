#re is For the Regural Expressions
import re

def password_complexity_checker(password):
    score = 0
    feedback = []

    # Check length:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters:
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters:
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for digits:
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters:
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Password should include at least one special character (!@#$%^&*(), etc.).")

    # Provide feedback:
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

# Main Function for Testing:
if __name__ == "__main__":
    print("Welcome to Password Complexity Checker!")
    user_password = input("Enter a password to check its strength: ")
    result = password_complexity_checker(user_password)

    print(f"\nPassword Strength: {result['strength']}")
    print("Suggestions:")
    for suggestion in result['feedback']:
        print(f"- {suggestion}")
