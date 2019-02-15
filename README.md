# Webmail-Domains

This is a Python package containing a single module `webmail_domains.py`, 
itself containing a list of webmail domains.

Feel free to make pull requests, and I'll add them in.


# Installation

    pip install webmail-domains


# Usage

    import webmail_domains

    if <some_email>.split('@')[1] in webmail_domains.WEBMAIL_DOMAINS:
        # do something (reject signup, don't add the domain to a CRM, etc.)
