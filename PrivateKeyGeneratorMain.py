import PrivateKeyGeneratorScript
import StringEncrypter

def main():
    PrivateKeyGeneratorScript.generate_new_private_key('my_private_key.pem')

    StringEncrypter.main()

if __name__ == "__main__":
    main()