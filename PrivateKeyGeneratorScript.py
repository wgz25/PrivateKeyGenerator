
# import the recommended framework/library used to generate keys/ what algorithms are used
from cryptography.hazmat.backends import default_backend

# generates the private RSA (public key cryptosystem). the secret key is divided into two parts, public and private. public key can be given to anyone, private key is the one that must be kept secret. RSA keys specifically are generated using the product of two large prime numbers 
from cryptography.hazmat.primitives.asymmetric import rsa

# used for key serialization. in this case, converts the generated RSA key and converts it into bytes.  
from cryptography.hazmat.primitives import serialization

# generate RSA private key. must define public exponent and key size. public exponent decides one of the two large primes used to generate the RSA. key_size describes how many bits the key should be. backend specifies which cryptographic backend to use. what this means is it chooses what framework or libraries to use to generate keys, or algorithms. generally can use default_backend() for cryptography.
def generate_new_private_key(filename='private_key.pem'):
    
    private_key  = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
)

# after you have a private key, can use private_bytes() to serialize the key- to save the private key to a pem file. pem stands for privacy enhanced mail. 
    pem = private_key.private_bytes( #this line changes the private key into bit form
        encoding=serialization.Encoding.PEM, # this line specifies what format is used for the key. in this case, it is PEM
        format = serialization.PrivateFormat.TraditionalOpenSSL, #this line specifies the structure of the bits. OpenSSL is commonly used.
        encryption_algorithm = serialization.NoEncryption() #this line specifies that the private key should not be encrypted when it is serialized. this means that they key will be easier to read/use. it is possible for a password to be needed in order to decrypt the key
 )

#creates a file named private_key.pem 

    with open('private_key.pem', 'wb') as pem_out:
        pem_out.write(pem) #this line writes out the previously defined "pem" into the file.  


print("Private key generated and saved as private_key.pem")

