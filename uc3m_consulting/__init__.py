"""
Initialization module for the uc3m_consulting package.

This module exposes the core classes of the package, allowing them to be
imported directly from the package level. It facilitates the access to
the EnterpriseRequest, EnterpriseManager, and the custom exception.

Author: Adam Kowalczyk Holtsova - 100525023
Date: 10/02/2026
Company: uc3m_consulting
"""

from .enterprise_request import EnterpriseRequest
from .enterprise_manager import EnterpriseManager
from .enterprise_management_exception import EnterpriseManagementException
