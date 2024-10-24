
from cryptography.hazmat.backends import default_backend # import the recommended framework/library used to generate keys/ what algorithms are used
from cryptography.hazmat.primitives.asymmetric import rsa # generates the private RSA (public key cryptosystem). the secret key is divided into two parts, public and private. public key can be given to anyone, private key is the one that must be kept secret. RSA keys specifically are generated using the product of two large prime numbers 
from cryptography.hazmat.primitives import serialization # used for key serialization. in this case, converts the generated RSA key and converts it into bytes.  
from cryptography.hazmat.primitives import hashes # ways to convert asymmetric keys into bytes. hashing is converting data into a fixed-length string.
import hashlib # import hashlib module, which helps in working with hash files or hashing files.
import os # os module is for creating/removing folders, or other things related to interacting with the OS. (changing directories, fetching content from folders, etc)


# generate RSA private key. must define public exponent and key size. public exponent decides one of the two large primes used to generate the RSA. key_size describes how many bits the key should be. backend specifies which cryptographic backend to use. what this means is it chooses what framework or libraries to use to generate keys, or algorithms. generally can use default_backend() for cryptography.
def generate_new_private_key(filename_prefix, output_dir='.'):
    #generate new RSA private key
    private_key  = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
)
    #extract public key
    public_key = private_key.public_key()

    #serialize public key to bytes to use for hashing
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    #create hash of the public key, which will be used as part of filename.
    public_key_hash = hashlib.sha256(public_key_bytes).hexdigest()
    # this method is a function that joins two path components, to create the filenames.
    filename = os.path.join(output_dir, f"{filename_prefix}_{public_key_hash[:8]}.pem")

    # after you have a private key, can use private_bytes() to serialize the key- to save the private key to a pem file. pem stands for privacy enhanced mail. 
    pem = private_key.private_bytes( #this line changes the private key into bit form
        encoding=serialization.Encoding.PEM, # this line specifies what format is used for the key. in this case, it is PEM
        format = serialization.PrivateFormat.TraditionalOpenSSL, #this line specifies the structure of the bits. OpenSSL is commonly used.
        encryption_algorithm = serialization.NoEncryption() #this line specifies that the private key should not be encrypted when it is serialized. this means that they key will be easier to read/use. it is possible for a password to be needed in order to decrypt the key
    )

    #creates a file named private_key.pem 
    with open(filename, 'wb') as pem_out:
        pem_out.write(pem) #this line writes out the previously defined "pem" into the file.  

    print(f"Private key generated and saved as {filename}")

# function to generate set number of private keys
def generate_multiple_private_keys(count=10, filename_prefix='private_key', output_dir='.'):
    #repeat count many times
    for i in range(count):
        generate_new_private_key(filename_prefix, output_dir)

# testing
if __name__ == "__main__":
    generate_multiple_private_keys(10)

