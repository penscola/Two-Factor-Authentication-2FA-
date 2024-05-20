import pyotp
import qrcode

key = 'NeuralNineMySuperSecretKey'

uri = pyotp.totp.TOTP(key).provisioning_uri(name='penscola',
                                            issuer_name='Penscola@Tech'
                                            )

print(uri)

qrcode.make(uri).save('totp.png')
