import base64
import binascii
from eth_keys import keys


class Crypto:

    def __base64_url_encode(self, string):
        """Removes any `=` used as padding from the encoded string.

        Parameters
        ----------
        string : str

        Returns
        -------
        str
        """
        encoded = base64.urlsafe_b64encode(string.encode('utf-8')).decode('utf-8')
        return encoded.rstrip("=")

    def __base64_url_decode(self, string):
        """Adds back in the required padding before decoding.

        Parameters
        ----------
        string : str

        Returns
        -------
        str
        """
        padding = 4 - (len(string) % 4)
        string = string + ("=" * padding)
        return base64.urlsafe_b64decode(string.encode('utf-8')).decode('utf-8')

    def ensure_not_0x(self, hex_string: str) -> str:
        return hex_string.replace('0x', '')

    def get_identity_token(self, did: str, private_key: str) -> str:
        """Sign a message with a private key

        Parameters
        ----------
        payload : str
        private_key : str

        Returns
        -------
        str
        """
        encoded_header = self.__base64_url_encode('{"alg":"ES256","typ":"JWT"}')

        payload = f'{{"iss":"{did}","claimData":{{"blockNumber":999999999999}}}}'
        encoded_payload: str = self.__base64_url_encode(payload)

        message: str = "".join([encoded_header, '.', encoded_payload])
        signer = keys.PrivateKey(binascii.unhexlify(self.ensure_not_0x(private_key)))
        signature = signer.sign_msg(message.encode())
        encoded_signature: str = self.__base64_url_encode(str(signature))

        jwt_token: str = "".join([encoded_header, '.', encoded_payload, '.', encoded_signature])
        return jwt_token
