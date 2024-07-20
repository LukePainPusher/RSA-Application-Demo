# Install the pycryptodome package if it is not yet on the system by running the following command:
# py -m pip install pycryptodome
# !!! Please advise that you MUST run the above command from the Linux/Windows command line (either CMD, PowerShell or Bash terminal and not the Python terminal !!!)

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key_size = None
private_key = None
public_key = None
ciphertext = None

def rsa_key_size():

    global key_size

    key_size = int(input('Please enter in the size of the RSA key (e.g., 1024, 2048): '))
    print(f"The key size has been set to {key_size} bits.")

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

def message_encryption():

    global public_key, ciphertext

    # Encrypt a message
    message = input('Enter in your secret message: ')
    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    ciphertext = cipher.encrypt(message.encode('utf-8'))
    print("Encrypted:", ciphertext)

def message_decryption():

    global private_key, ciphertext

    # Decrypt the message
    cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    decrypted_message = cipher.decrypt(ciphertext)
    print("Decrypted:", decrypted_message.decode('utf-8'))

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