# -*- coding: utf-8 -*-

"""
    collection

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Balance(object):

    """Implementation of the 'Balance' model.

    The available balance of the account

    Attributes:
        available_balance (string): The available balance of the account
        currency (string): ISO4217 Currency

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "available_balance":'availableBalance',
        "currency":'currency'
    }

    def __init__(self,
                 available_balance=None,
                 currency=None):
        """Constructor for the Balance class"""

        # Initialize members of the class
        self.available_balance = available_balance
        self.currency = currency


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        available_balance = dictionary.get('availableBalance')
        currency = dictionary.get('currency')

        # Return an object of this model
        return cls(available_balance,
                   currency)


