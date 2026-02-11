"""
Enterprise Request Module

This module provides the EnterpriseRequest class for representing
enterprise request data including CIF, phone, and enterprise name.

Author: Adam Kowalczyk Holtsova - 100525203
Date: 11/02/2026
Company: uc3m_consulting
"""
import json


class EnterpriseRequest:
    """
    Enterprise Request class for storing and managing enterprise information.

    This class encapsulates enterprise data including CIF (Tax ID), phone number,
    and enterprise name, along with a timestamp of creation.
    """

    def __init__(self, cif, phone, enterprise_name):
        """
        Initialize an EnterpriseRequest.
        """
        self.__enterprise_name = enterprise_name
        self.__cif = cif
        self.__phone = phone

    def __str__(self):
        """
        Return a string representation of the EnterpriseRequest.
        """
        return "Enterprise:" + json.dumps(self.__dict__)

    @property
    def enterprise_cif(self):
        """
        Get the enterprise CIF.
        """
        return self.__cif

    @enterprise_cif.setter
    def enterprise_cif(self, value):
        """
        Set the enterprise CIF.
        """
        self.__cif = value

    @property
    def phone_number(self):
        """
        Get the enterprise phone number.
        """
        return self.__phone

    @phone_number.setter
    def phone_number(self, value):
        """
        Set the enterprise phone number.
        """
        self.__phone = value

    @property
    def enterprise_name(self):
        """
        Get the enterprise name.
        """
        return self.__enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        """
        Set the enterprise name.
        """
        self.__enterprise_name = value
