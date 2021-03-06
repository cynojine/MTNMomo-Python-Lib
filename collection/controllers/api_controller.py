# -*- coding: utf-8 -*-

"""
    collection

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from collection.api_helper import APIHelper
from collection.configuration import Configuration
from collection.controllers.base_controller import BaseController
from collection.http.auth.custom_header_auth import CustomHeaderAuth
from collection.models.token_post_200_application_json_response import TokenPost200ApplicationJsonResponse
from collection.models.balance import Balance
from collection.models.request_to_pay_result import RequestToPayResult
from collection.exceptions.token_post_401_application_json_response_exception import TokenPost401ApplicationJsonResponseException
from collection.exceptions.api_exception import APIException
from collection.exceptions.error_reason_error_exception import ErrorReasonErrorException

class APIController(BaseController):

    """A Controller to access Endpoints in the collection API."""


    def create_token_post(self,
                          authorization):
        """Does a POST request to /token/.

        This operation is used to create an access token which can then be
        used to authorize and authenticate towards the other end-points of the
        API.

        Args:
            authorization (string): Basic authentication header containing API
                user ID and API key. Should be sent in as B64 encoded.

        Returns:
            TokenPost200ApplicationJsonResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/token/'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise TokenPost401ApplicationJsonResponseException('Unauthorized', _context)
        elif _context.response.status_code == 500:
            raise APIException('Error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, TokenPost200ApplicationJsonResponse.from_dictionary)

    def get_v_1_0_account_balance(self,
                                  x_target_environment,
                                  authorization=None):
        """Does a GET request to /v1_0/account/balance.

        Get the balance of the account.

        Args:
            x_target_environment (string): The identifier of the EWP system
                where the transaction shall be processed. This parameter is
                used to route the request to the EWP system that will initiate
                the transaction.
            authorization (string, optional): Authorization header used for
                Basic authentication and oauth. Format of the header parameter
                follows the standard for Basic and Bearer. Oauth uses Bearer
                authentication type where the credential is the received
                access token.

        Returns:
            Balance: Response from the API. Ok

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1_0/account/balance'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'X-Target-Environment': x_target_environment,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request, e.g. invalid data was sent in the request.', _context)
        elif _context.response.status_code == 500:
            raise ErrorReasonErrorException('Internal error. The returned response contains details.', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Balance.from_dictionary)

    def get_v_1_0_accountholder_accountholderidtype_accountholderid_active(self,
                                                                           account_holder_id,
                                                                           account_holder_id_type,
                                                                           x_target_environment,
                                                                           authorization=None):
        """Does a GET request to /v1_0/accountholder/{accountHolderIdType}/{accountHolderId}/active.

        Operation is used  to check if an account holder is registered and
        active in the system.

        Args:
            account_holder_id (string): The party number. Validated according
                to the party ID type (case Sensitive). <br> msisdn - Mobile
                Number validated according to ITU-T E.164. Validated with
                IsMSISDN<br> email - Validated to be a valid e-mail format.
                Validated with IsEmail<br> party_code - UUID of the party.
                Validated with IsUuid
            account_holder_id_type (string): Specifies the type of the party
                ID. Allowed values [msisdn, email, party_code].  <br>
                accountHolderId should explicitly be in small letters.
            x_target_environment (string): The identifier of the EWP system
                where the transaction shall be processed. This parameter is
                used to route the request to the EWP system that will initiate
                the transaction.
            authorization (string, optional): Authorization header used for
                Basic authentication and oauth. Format of the header parameter
                follows the standard for Basic and Bearer. Oauth uses Bearer
                authentication type where the credential is the received
                access token.

        Returns:
            mixed: Response from the API. Ok. True if account holder is
                registered and active, false if the account holder is not
                active or not found

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1_0/accountholder/{accountHolderIdType}/{accountHolderId}/active'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'accountHolderId': account_holder_id,
            'accountHolderIdType': account_holder_id_type
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'X-Target-Environment': x_target_environment,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request, e.g. invalid data was sent in the request.', _context)
        elif _context.response.status_code == 500:
            raise APIException('Internal error. The returned response contains details.', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def create_requesttopay_post(self,
                                 x_reference_id,
                                 x_target_environment,
                                 authorization=None,
                                 x_callback_url=None,
                                 body=None):
        """Does a POST request to /v1_0/requesttopay.

        This operation is used to request a payment from a consumer (Payer).
        The payer will be asked to authorize the payment. The transaction will
        be executed once the payer has authorized the payment. The
        requesttopay will be in status PENDING until the transaction is
        authorized or declined by the payer or it is timed out by the system.
                 Status of the transaction can be validated by using the GET
         /requesttopay/\<resourceId\>

        Args:
            x_reference_id (string): Format - UUID. Recource ID of the created
                request to pay transaction. This ID is used, for example,
                validating the status of the request. ‘Universal Unique ID’
                for the transaction generated using UUID version 4.
            x_target_environment (string): The identifier of the EWP system
                where the transaction shall be processed. This parameter is
                used to route the request to the EWP system that will initiate
                the transaction.
            authorization (string, optional): Authorization header used for
                Basic authentication and oauth. Format of the header parameter
                follows the standard for Basic and Bearer. Oauth uses Bearer
                authentication type where the credential is the received
                access token.
            x_callback_url (string, optional): URL to the server where the
                callback should be sent.
            body (RequestToPay, optional): TODO: type description here.
                Example: 

        Returns:
            void: Response from the API. Accepted

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1_0/requesttopay'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8',
            'X-Reference-Id': x_reference_id,
            'X-Target-Environment': x_target_environment,
            'Authorization': authorization,
            'X-Callback-Url': x_callback_url
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request, e.g. invalid data was sent in the request.', _context)
        elif _context.response.status_code == 409:
            raise ErrorReasonErrorException('Conflict, duplicated reference id', _context)
        elif _context.response.status_code == 500:
            raise ErrorReasonErrorException('Internal Error.', _context)
        self.validate_response(_context)

    def get_requesttopay_reference_id_get(self,
                                          reference_id,
                                          x_target_environment,
                                          authorization=None):
        """Does a GET request to /v1_0/requesttopay/{referenceId}.

        This operation is used to get the status of a request to pay.
        X-Reference-Id that was passed in the post is used as reference to the
        request.

        Args:
            reference_id (string): UUID of transaction to get result.
                Reference id  used when creating the request to pay.
            x_target_environment (string): The identifier of the EWP system
                where the transaction shall be processed. This parameter is
                used to route the request to the EWP system that will initiate
                the transaction.
            authorization (string, optional): Authorization header used for
                Basic authentication and oauth. Format of the header parameter
                follows the standard for Basic and Bearer. Oauth uses Bearer
                authentication type where the credential is the received
                access token.

        Returns:
            RequestToPayResult: Response from the API. OK. Note that a  failed
                request to pay will be returned with this status too. The
                'status' of the RequestToPayResult can be used to determine
                the outcome of the request. The 'reason' field can be used to
                retrieve a cause in case of failure.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1_0/requesttopay/{referenceId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'referenceId': reference_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'X-Target-Environment': x_target_environment,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Bad request, e.g. an incorrectly formatted reference id was provided.', _context)
        elif _context.response.status_code == 404:
            raise ErrorReasonErrorException('Resource not found.', _context)
        elif _context.response.status_code == 500:
            raise ErrorReasonErrorException('Internal Error. Note that if the retrieved request to pay has failed, it will not cause this status to be returned. This status is only returned if the GET request itself fails.', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, RequestToPayResult.from_dictionary)
