import pyotp

key = 'NeuralNineMySuperSecretKey'

totp = pyotp.TOTP(key)

while True:
    print(totp.verify(input('Enter code: ')))
