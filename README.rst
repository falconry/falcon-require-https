Falcon Middleware: Require HTTPS |Build Status| |codecov.io|
============================================================

The ``falcon-require-https`` package provides a middleware component
for sanity-checking that the incoming request was received over
HTTPS. While the web server is primarily responsibile for enforcing the
HTTPS protocol, misconfiguration is still a leading cause of security
vulnerabilities, and so it can be helpful to perform certain additional
checks, such as this one, within the application layer itself.

Credits
-------

This middleware component is based on paul291's original
proof of concept, which was orginally submitted as a PR to the
`falconry/falcon` repo.

About Falcon
------------

Falcon is a `high-performance Python web
framework <http://falconframework.org/index.html>`__ for building cloud
APIs. It encourages the REST architectural style, and tries to do as
little as possible while remaining `highly
effective <http://falconframework.org/index.html#Benefits>`__.


.. |Build Status| image:: https://travis-ci.org/falconry/falcon-require-https.svg
   :target: https://travis-ci.org/falconry/falcon-require-https
.. |codecov.io| image:: https://codecov.io/gh/falconry/falcon-require-https/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/falconry/falcon-require-https
