"""
Module for handling Enterprise Management Exceptions.

This module defines the custom exception classes used within the
Enterprise Management system to handle specific business logic errors
and validation failures.

Author: Adam Kowalczyk Holtsova - 100525203
Date: 10/02/2026
Company: UC3MConsulting
"""

class EnterpriseManagementException(Exception):
    """
    Exception raised for errors within the Enterprise Management module.

    This class provides a custom exception wrapper to handle specific failures
    related to enterprise management operations, encapsulating the error description.
    """
    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self,value):
        self.__message = value
