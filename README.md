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


# Updates

The list was last updated on [August 17, 2017](https://github.com/mbirtwell/Webmail-Domains/commit/d96c2acea95afec09a4447376242716ac8601f7f).
