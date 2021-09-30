from dsb_client.api import crypto

payload = '{"id":1,"name":"some_name","active":false}' # random json string
private_key = "0xe2caca2e7c22fc5bf985cc6838e152753c52b925620bf2449e388c90e3d853f7"

crypto_instance = crypto.Crypto()

signature = crypto_instance.get_payload_signature(payload, private_key)

print(f'signature = {signature}')
