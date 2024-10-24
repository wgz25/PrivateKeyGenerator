import private_key_generator_script
import string_encrypter
def main():
    #generate new private key, using either default or user given input.
    pem_file = input("Enter path to save the private key (default: 'my_private_key.pem'): ") or 'my_private_key.pem'
    output_dir = input("Enter directory to save the keys (default: current directory): ") or '.'
    private_key_generator_script.generate_new_private_key(pem_file, output_dir)

    #create instance of StringEncrypter
    encrypter = string_encrypter.StringEncrypter(pem_file)

    # take input from user, to encrypt message
    message = input("Enter message to encrypt: ")

    # encrypt the message
    encrypted_message = encrypter.encrypt_message(message)

    # specify the output path for saving the encrypted message.
    output_file = input("Enter output file path to save encrypted message: ") or 'encrypted_message.txt'
    encrypter.save_encrypted_message(encrypted_message, output_file)

if __name__ == "__main__":
    main()