"""
Main Module

This module provides encoding/decoding utilities and demonstrates
the use of EnterpriseManager for validating and processing enterprise data.

Author: Adam Kowalczyk Holtsova - 100525023
Date: 11/02/2026
Company: uc3m_consulting
"""
import string
from uc3m_consulting import EnterpriseManager

# GLOBAL CONSTANTS
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3


def encode(word):
    """
    Encode a string using Caesar cipher with a fixed shift.
    """
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded


def decode(word):
    """
    Decode a string using Caesar cipher with a fixed shift.
    """
    decoded = ""
    for letter in word:
        if letter == ' ':
            decoded = decoded + ' '
        else:
            x = (LETTERS.index(letter) - SHIFT) % len(LETTERS)
            decoded = decoded + LETTERS[x]
    return decoded


def test_cif_validation():
    """
    Test CIF validation with valid and invalid examples.
    """
    mng = EnterpriseManager()

    # Valid CIF example
    valid_cif = "A58818501"
    print(f"\nTesting VALID CIF: {valid_cif}")
    print(f"Result: {'✓ VALID' if mng.validate_cif(valid_cif) else '✗ INVALID'}")

    # Invalid CIF example
    invalid_cif = "A58818502"  # Wrong control digit
    print(f"\nTesting INVALID CIF: {invalid_cif}")
    print(f"Result: {'✓ VALID' if mng.validate_cif(invalid_cif) else '✗ INVALID'}")


def main():
    """
    Main function to demonstrate enterprise data processing with encoding.

    1. Creates an EnterpriseManager instance
    2. Reads enterprise data from JSON file
    3. Encodes and decodes the data
    4. Prints the results
    """
    # Test CIF validation
    test_cif_validation()

    mng = EnterpriseManager()
    res = mng.read_product_code_from_json("test.json")
    str_res = str(res)
    print(str_res)
    encode_res = encode(str_res)
    print("Encoded Res " + encode_res)
    decode_res = decode(encode_res)
    print("Decoded Res: " + decode_res)
    print("cif: " + res.enterprise_cif)
    print("enterprise_name: " + res.enterprise_name)
    print("enterprise_phone: " + res.phone_number)


if __name__ == "__main__":
    main()
