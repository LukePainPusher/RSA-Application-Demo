# Install the pycryptodome package if it is not yet on the system by running the following command:
# py -m pip install pycryptodome
# !!! Please advise that you MUST run the above command from the Linux/Windows command line (either CMD, PowerShell or Bash terminal and not the Python terminal !!!)

# Import the RSA module from the Cyrpto.Publickey library, and the PKCS1_OAEP module from the Crypto.Cipher library.

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Create the following variables which will be called in the below functions as required.  We will store the value of 'None' in each variable so we can create them without storing any data in them:

key_size = None
private_key = None
public_key = None
ciphertext = None

# This function will allow the end user to type in the RSA key size and store it in the Global Variable, 'rsa_key_size':

def rsa_key_size():

    global key_size

    key_size = int(input('Please enter in the size of the RSA key (e.g., 1024, 2048): '))
    print(f"The key size has been set to {key_size} bits.")

# This function will generate the RSA key pairs required for encryption and decryption:

def generate_rsa_keys():

    global private_key, public_key
    try:

        # Generate RSA keys
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        print('The RSA keys have been successfully generated.')
    except NameError:
        print('Please set the RSA key size first in order to proceed further!')

# This function will encrypt the message using the public key generated:

def message_encryption():

    global public_key, ciphertext

    # Encrypt a message
    message = input('Enter in your secret message: ')
    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    ciphertext = cipher.encrypt(message.encode('utf-8'))
    print("Encrypted:", ciphertext)

# This function will decrypt the message using the private key generated:

def message_decryption():

    global private_key, ciphertext

    # Decrypt the message
    cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    decrypted_message = cipher.decrypt(ciphertext)
    print("Decrypted:", decrypted_message.decode('utf-8'))

# This function will repeatedly prompt the user to enter an option.  Based on the option selected, the program will call one of the functions created above:

def rsa_encryption_application_menu():

    while True:
        print('===============================================')
        print('=  Welcome to the RSA encryption application  =')
        print('===============================================')
        print('= Please enter one of the following options)  =')
        print('= Option 1. Enter RSA key size                =')
        print('= Option 2. Generate RSA keys                 =')
        print('= Option 3. Message encryption                =')
        print('= Option 4. Message decryption                =')
        print('= Option 5. Exit application                  =')
        print('===============================================')
        response = int(input('Please enter your option: '))
        if response == 1:
            rsa_key_size()
        elif response == 2:
            generate_rsa_keys()
        elif response == 3:
            message_encryption()
        elif response == 4:
            message_decryption()
        elif response ==5:
            exit()
        else:
            print('Invalid input, please try again!')

rsa_encryption_application_menu()
