import re

import falcon

_FORWARDED_PROTO_RE = re.compile('proto=([A-Za-z]+)')


class RequireHTTPS(object):
    """Middleware to verify that each request is performed via HTTPS.

    While the web server is primarily responsibile for enforcing the
    HTTPS protocol, misconfiguration is still a leading cause of
    security vulnerabilities, and so it can be helpful to perform
    certain additional checks, such as this one, within the application
    layer itself.

    At least one of the following sources must indicate the use of
    HTTPS:

        * The requested URI
        * The X-Forwarded-Proto header
        * The Forwarded header

    Otherwise, an instance of falcon.HTTPBadRequest is raised.
    """

    def process_request(self, req, resp):
        if req.protocol.lower() == 'https':
            return

        xfp = req.get_header('X-FORWARDED-PROTO')
        if xfp and xfp.lower() == 'https':
            return

        forwarded = req.get_header('FORWARDED')
        if forwarded:
            # NOTE(kgriffs): The first hop must indicate HTTPS,
            #   otherwise the chain is already insecure.
            first, __, __ = forwarded.partition(',')

            match = _FORWARDED_PROTO_RE.search(first)
            if match and match.group(1).lower() == 'https':
                return

        raise falcon.HTTPBadRequest(
            title='HTTPS Required',
            description=(
                'All requests must be performed via the HTTPS protocol. '
                'Please switch to HTTPS and try again.'
            )
        )
