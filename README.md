# ReferralCandy Python API Client

## Installation

    pip install referral_candy

## Usage

### Initialization

Initialize a client with your ReferralCandy credentials

    >>> from referral_candy import ReferralCandy
    >>> # Default to API v2
    >>> rc = ReferralCandy(access_id="YOUR_ACCESS_ID", secret_key="YOUR_SECRET_KEY")
    >>>
    >>> # use API v1
    >>> rc_v1 = ReferralCandy(access_id="YOUR_ACCESS_ID", secret_key="YOUR_SECRET_KEY", api_version="v1")
    >>>
    >>> # Use API v2
    >>> rc_v2 = ReferralCandy(access_id="YOUR_ACCESS_ID", secret_key="YOUR_SECRET_KEY", api_version="v2")

### Verification

Verify your credentials.

    >>> response = rc.verify()
    >>> response.text
    u'{"message":"Verification Ok"}'
    >>> response.status_code
    200

### API Methods

The ReferralCandy Python API client will perform the [authentication](http://www.referralcandy.com/api#authentication) steps for you.
This means that you would not be required to pass in the 'timestamp', 'accessID', and 'signature' parameters.

[API endpoints](http://www.referralcandy.com/api) are available as methods in the ReferralCandy Python API client.

### API Responses

The ReferralCandy Python API client uses [requests](https://github.com/kennethreitz/requests). API responses are wrapped in `requests.models.Response` objects.

    >>> response = rc.verify()
    >>> response.__class__
    <class 'requests.models.Response'>
    >>> response.text
    u'{"message":"Verification Ok"}'
    >>> response.status_code
    200

## Documentation

[API documentation](http://www.referralcandy.com/api)

## Credits

Thank you for the inputs:

- [Jian Wei Gan](https://github.com/ganjianwei)
