import base64 # import base64 module for encoding/decoding
from cryptography.hazmat.backends import default_backend # import the recommended framework/library used to generate keys/ what algorithms are used
from cryptography.hazmat.primitives.asymmetric import padding # padding is a way to add cryptographic problems in order to reduce the success of guessing the final states in encryption correctly.
from cryptography.hazmat.primitives import hashes, serialization # ways to convert asymmetric keys into bytes. hashing is converting data into a fixed-length string.


#enter path to generated private key file.

# function to load private key from inputted file path.
class StringEncrypter:
    def __init__(self, private_key_path='my_private_key.pem'):
        self.private_key_path = private_key_path
        self.private_key = self.load_private_key(self.private_key_path)

    def load_private_key(self, input_pem_file_path): 
        try:
            with open(input_pem_file_path, 'rb') as key_file: # 
                private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=None, #no password, not encrypted
                    backend=default_backend()
                )
            return private_key
        except FileNotFoundError: #
            print(f"Error: File {input_pem_file_path} not found")
            raise


# function to encrypt the message with the loaded private key
    def encrypt_message(self, message):
        encrypted = self.private_key.public_key().encrypt(
            message.encode('utf-8'), # this converts the message into bytes
            # padding.OAEP referes to Optimal Asymmetric Encryption Padding. padding is something used in cryptography to make data fulfill/conform to data size requirements.
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()), # this line specifies the MGF (mask generation function) used in OAEP. it generates a mask that is used to hide the plaintext. SHA256 means it uses the SHA-256 hash function.
                algorithm=hashes.SHA256(), # specifies hash algorithm used to hash the data. this is used for both padding as well as mask generation.
                label=None # no additional context to add to padding process
            )
        )
        return encrypted

# function to save the base64 encoded data to a file

    def save_encrypted_message(self, encrypted_message, output_file_path='encrypted_message.txt'):
        # convert the message to base64
        encrypted_base64 = base64.b64encode(encrypted_message).decode('utf-8')
        with open(output_file_path, 'w') as file:
            file.write(encrypted_base64)
        print(f"Encrypted message to {output_file_path}")

# testing
if __name__ == "__main__":
    pem_file = input("Enter path to the private key file (PEM) [default is 'my_private_key.pem']: ") or 'my_private_key.pem'
    output_file = input("Enter output file path to save encrypted message (txt) [default is 'encrypted_message.txt']: ") or 'encrypted_message.txt'
    message = input("Enter message to encrypt: ")

    string_encrypter = StringEncrypter(pem_file)

    encrypted_message = string_encrypter.encrypt_message(message)
    string_encrypter.save_encrypted_message(encrypted_message, output_file)