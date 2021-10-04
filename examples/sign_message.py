from dsb_client.api import crypto

payload = '{"id":1,"name":"some_name","active":false}' # random json string
private_key = "0xe2caca2e7c22fc5bf985cc6838e152753c52b925620bf2449e388c90e3d853f7"
did = 'did:ethr:0x37d37b10d1186aE41737D38b2dBC5C88316c9FBd'

crypto_instance = crypto.Crypto()

print(f'signing payload \'{payload}\' using {did}')

signature = crypto_instance.get_payload_signature(payload, private_key)

print(f'signature = {signature}')

valid = crypto_instance.verify_payload_signature(payload, signature, did)

print(f'is valid? = {valid}')
