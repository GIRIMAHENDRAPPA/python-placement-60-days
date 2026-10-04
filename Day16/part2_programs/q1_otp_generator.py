# Day16 P2 Q1 - OTP Generator using random module
import random

def generate_otp(length=6):
    otp = ""
    for i in range(length):
        otp += str(random.randint(0, 9))
    return otp

# Test
print(f"Your OTP is: {generate_otp(6)}")
print(f"Your 4-digit OTP is: {generate_otp(4)}")

# Advanced: 6-digit OTP using sample
def otp_advanced():
    digits = "0123456789"
    otp = "".join(random.sample(digits, 6))
    return otp

print(f"Advanced OTP: {otp_advanced()}")