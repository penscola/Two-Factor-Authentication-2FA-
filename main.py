import pyotp

key = 'NeuralNineMySuperSecretKey'

# initializes a Time-Based One-Time Password (TOTP)
totp = pyotp.TOTP(key)

print(totp.now())

input_code = input('Enter 2FA code: ')

print(totp.verify(input_code))
