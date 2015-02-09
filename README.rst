python-recaptcha2
-----------------

A minimalist Python client for the Google reCAPTCHA 2.0 API.

Usage::

    >>> import recaptcha2

    >>> recaptcha2.verify(SECRET_KEY, INVALID_RESPONSE, REMOTE_IP)
    {u'error-codes': [u'invalid-input-response'], u'success': False}

    >>> recaptcha2.verify(SECRET_KEY, VALID_RESPONSE, REMOTE_IP)
    {u'success': True}
