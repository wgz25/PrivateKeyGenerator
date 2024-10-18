import base64 # import base64 module for encoding/decoding

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding #research what this does
from cryptography.hazmat.primitives import hashes, serialization # research what these do


#enter path to generated private key file.

# function to load private key from inputted file path.
def load_private_key(input_pem_file_path): #
    with open(input_pem_file_path, 'rb') as key_file: # 
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None, #no password, not encrypted
            backend=default_backend()
        )
    return private_key


# function to encrypt the message with the loaded private key
def encrypt_message(private_key, message):
    encrypted = private_key.public_key().encrypt(
        message.encode('utf-8'), # this converts the message into bytes
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# function to save the base64 encoded data to a file

def save_encrypted_message(encrypted_message, output_file_path):
    # convert the message to base64
    encrypted_base64 = base64.b64encode(encrypted_message).decode('utf-8')

    with open(output_file_path, 'w') as file:
        file.write(encrypted_base64)

    print(f"Encrypted message to {output_file_path}")

# set defaults, and for inputs
def main():
    default_input_pem_path = 'my_private_key.pem' #default pem file location
    default_output_path = 'encrypted_message.txt' #default output file location

    pem_file = input(f"Enter the path to private key file (PEM) [default: {default_input_pem_path}]: ") or default_input_pem_path
    output_file = input(f"Enter output path for encrypted message [default: {default_output_path}]: ") or default_output_path
    message = input("Enter the message to encrypt: ")

    private_key = load_private_key(pem_file)
    encrypted_message = encrypt_message(private_key, message)
    save_encrypted_message(encrypted_message, output_file)

# checks to see if the script is imported or being run directly
if __name__ == "__main__":
    main()