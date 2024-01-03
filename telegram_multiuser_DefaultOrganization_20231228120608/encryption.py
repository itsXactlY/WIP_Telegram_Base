'''
This file contains functions for encrypting and decrypting the API key.
'''
import base64
import os
def encrypt_api_key(api_key):
    '''
    Encrypt the API key.
    '''
    # Implement encryption logic here
    encrypted_key = base64.b64encode(api_key.encode()).decode()
    return encrypted_key
def decrypt_api_key():
    '''
    Decrypt the API key.
    '''
    encrypted_key = os.getenv("ENCRYPTED_API_KEY")
    if encrypted_key is None:
        raise ValueError("ENCRYPTED_API_KEY environment variable is not set")
    api_key = base64.b64decode(encrypted_key.encode()).decode()
    return api_key