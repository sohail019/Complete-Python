# 8. Password Strength Checker

# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input('Enter the Password: ')
password_length = len(password)
if password_length < 6:
    print('Weak Password!! Should be greater than 8 Characters')
elif password_length <= 10:
    print('Medium Password!! Should contain some special characters')
else:
    print('Strong Password!! You can now proceed')