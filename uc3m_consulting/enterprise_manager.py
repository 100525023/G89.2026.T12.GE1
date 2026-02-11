"""
Module for handling Enterprise operations

This module provides the EnterpriseManager class for managing enterprise operations
including CIF validation and JSON data processing.

Author: Adam Kowalczyk Holtsova - 100525203
Date: 11/02/2026
Company: uc3m_consulting
"""
import json
from .enterprise_management_exception import EnterpriseManagementException
from .enterprise_request import EnterpriseRequest


class EnterpriseManager:
    """
    Enterprise Manager class for handling enterprise-related operations.

    This class provides functionality to validate CIF codes and process
    enterprise requests from JSON files.
    """

    # Control character mapping table for CIF validation
    CONTROL_CHAR_MAP = {
        0: 'J',
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'F',
        7: 'G',
        8: 'H',
        9: 'I'
    }

    # Organization letter types that require numeric control character
    NUMERIC_CONTROL_LETTERS = {'A', 'B', 'E', 'H'}

    # Organization letter types that require alphabetic control character
    ALPHA_CONTROL_LETTERS = {'K', 'P', 'Q', 'S'}

    def validate_cif(self, cif):
        """
        Validate a CIF (Tax Identification Number)

        The CIF format is: [Letter - 7 Numbers - Control Character]

        1. Check format and length (9 characters)
        2. Validate organization letter
        3. Extract and validate 7-digit central body
        4. Calculate control character
        5. Verify control character matches
        """
        # Check basic format
        if not cif or not isinstance(cif, str):
            return False

        if len(cif) != 9:
            return False

        # Extract components
        org_letter = cif[0].upper()
        central_body = cif[1:8]
        control_char = cif[8]

        # Validate organization letter
        valid_letters = self.NUMERIC_CONTROL_LETTERS | self.ALPHA_CONTROL_LETTERS
        if org_letter not in valid_letters:
            return False

        # Validate central body (must be 7 digits)
        if not central_body.isdigit():
            return False

        # Calculate the expected control character
        expected_control = self._calculate_control_character(central_body)

        # Verify control character
        if org_letter in self.NUMERIC_CONTROL_LETTERS:
            # Control must be numeric
            return control_char == str(expected_control)

        # Control must be alphabetic (from mapping table)
        return control_char.upper() == self.CONTROL_CHAR_MAP[expected_control]

    def _calculate_control_character(self, central_body):
        """
        Calculate the control character for a CIF.

        1. Sum digits in even positions (2nd, 4th, 6th)
        2. For odd positions (1st, 3rd, 5th, 7th):
           - Multiply by 2
           - If result has 2 digits, sum them
           - Accumulate
        3. Add even sum + odd sum
        4. Get unit digit and subtract from 10 (if unit is 0, base digit is 0)
        """
        # Sum even position digits (indices 1, 3, 5)
        even_sum = sum(int(central_body[i]) for i in [1, 3, 5])

        # Process odd position digits (indices 0, 2, 4, 6)
        odd_sum = 0
        for i in [0, 2, 4, 6]:
            digit = int(central_body[i])
            doubled = digit * 2

            # If doubled result has 2 digits, sum them
            if doubled >= 10:
                doubled = doubled // 10 + doubled % 10

            odd_sum += doubled

        # Total sum
        total_sum = even_sum + odd_sum

        # Calculate base digit
        unit = total_sum % 10

        if unit == 0:
            base_digit = 0
        else:
            base_digit = 10 - unit

        return base_digit

    def read_product_code_from_json(self, file_path):
        """
        Read and process enterprise request data from a JSON file.
        """
        try:
            with open(file_path, encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError as e:
            raise EnterpriseManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise EnterpriseManagementException(
                "JSON Decode Error - Wrong JSON Format"
            ) from e

        try:
            temp_cif = data["cif"]
            temp_phone = data["phone"]
            enterprise_name = data["enterprise_name"]
            req = EnterpriseRequest(temp_cif, temp_phone, enterprise_name)
        except KeyError as e:
            raise EnterpriseManagementException(
                "JSON Decode Error - Invalid JSON Key"
            ) from e

        if not self.validate_cif(temp_cif):
            raise EnterpriseManagementException("Invalid CIF")

        return req
