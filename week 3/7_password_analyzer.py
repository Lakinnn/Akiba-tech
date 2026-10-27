print("====== Password Analyzer ======")
import string


def check_minimum_length(password, minimum_length=8):
    return len(password) >= minimum_length


def has_uppercase(password):
    return any(character.isupper() for character in password)


def has_lowercase(password):
    return any(character.islower() for character in password)


def has_digit(password):
    return any(character.isdigit() for character in password)


def has_special_character(password):
    return any(character in string.punctuation for character in password)


def analyze_password(password, minimum_length=8):
    if not isinstance(password, str):
        raise ValueError("Password must be a string.")

    if minimum_length < 1:
        raise ValueError("Minimum length must be positive.")

    checks = {
        "minimum_length": check_minimum_length(
            password, minimum_length
        ),
        "uppercase_letter": has_uppercase(password),
        "lowercase_letter": has_lowercase(password),
        "digit": has_digit(password),
        "special_character": has_special_character(password)
    }

    missing_requirements = [
        requirement
        for requirement, passed in checks.items()
        if not passed
    ]

    passed_count = sum(checks.values())
    total_requirements = len(checks)

    if passed_count == total_requirements:
        strength = "Strong"
    elif passed_count >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "passed": checks,
        "all_requirements_met": not missing_requirements,
        "missing_requirements": missing_requirements,
        "strength": strength
    }


# Fictional test passwords
test_passwords = [
    "Sunrise42!",
    "password",
    "Short1!",
    "WELCOME2026",
    "River@Blue7"
]

for password in test_passwords:
    report = analyze_password(password)

    print(f"\nPassword: {password}")
    print(f"Strength: {report['strength']}")
    print(f"All requirements met: {report['all_requirements_met']}")

    print("Requirements:")
    for requirement, passed in report["passed"].items():
        status = "PASS" if passed else "FAIL"
        print(f"  {requirement}: {status}")

    if report["missing_requirements"]:
        print("Missing requirements:")
        for requirement in report["missing_requirements"]:
            print(f"  - {requirement}")
