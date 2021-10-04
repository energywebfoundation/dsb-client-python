import base64
import binascii
from eth_keys import keys


class Crypto:

    message_prefix = '\x19Ethereum Signed Message:\n'

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
        """Get a signed proof of your identity to sign into DSB

        Parameters
        ----------
        did : str
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

    def get_payload_signature(self, payload: str, private_key: str) -> str:
        """Sign a message payload with a private key

        Parameters
        ----------
        payload : str
        private_key : str

        Returns
        -------
        str
        """
        signer = keys.PrivateKey(binascii.unhexlify(self.ensure_not_0x(private_key)))
        message = f'{self.message_prefix}{len(payload)}{payload}'
        return signer.sign_msg(message.encode()).__str__()

    def verify_payload_signature(self, payload: str, signature: str, expected_did: str) -> bool:
        """Verifies a message payload was signed by the stated DID

        Parameters
        ----------
        payload : str
        signature : str
        expected_did : str

        Returns
        -------
        str
        """
        no_prefix_sig = self.ensure_not_0x(signature)
        v = int(no_prefix_sig[128:], 16)
        r = int(no_prefix_sig[:64], 16)
        s = int(no_prefix_sig[64:128], 16)
        # only support ethereum recovery param (27 or 28) for now
        vrs = (v if v <= 1 else v - 27,
               r,
               s)
        verifier = keys.Signature(vrs=vrs)
        message = f'{self.message_prefix}{len(payload)}{payload}'
        public_key = verifier.recover_public_key_from_msg(message.encode())
        # note: simplified for now
        # pubkey address might not equal did (e.g. delegated identity)
        # did might not necessarily use ethr method
        return f'did:ethr:{public_key.to_checksum_address()}' == expected_did
