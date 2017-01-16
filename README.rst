Falcon Middleware: Require HTTPS |Build Status| |codecov.io|
============================================================

The ``falcon-require-https`` package provides a middleware component
for sanity-checking that the incoming request was received over
HTTPS. While the web server is primarily responsibile for enforcing the
HTTPS protocol, misconfiguration is still a leading cause of security
vulnerabilities, and so it can be helpful to perform certain additional
checks, such as this one, within the application layer itself.

Quick Links
-----------

* `View the code <https://github.com/falconry/falcon-require-https>`__.
* `Join the discussion group <https://groups.google.com/forum/#!forum/falconframework>`__.
* `Hang out in #falconframework on freenode <https://kiwiirc.com/client/irc.freenode.net/?#falconframework>`__.

Installation
------------

.. code:: bash

    $ pip install falcon-require-https

Usage
-----

The ``RequireHTTPS`` middleware class verifies each incoming request. To use
it, simply pass an instance to the ``falcon.API()`` initializer:

.. code:: python

    from falcon_require_https import RequireHTTPS

    app = falcon.API(middleware=[RequireHTTPS()])

At least one of the following sources must indicate the use of HTTPS:

* The schema of the requested URL
* The X-Forwarded-Proto header
* The Forwarded header (only the first hop is checked)

Otherwise, an instance of ``falcon.HTTPBadRequest`` is raised.

Caution
-------

This middleware is not meant to replace proper security controls in your
web server or load balancer. It is simply meant as a final backstop to
guard against inadvertent misconfiguration at the networking layer.

Credits
-------

This middleware component is based on paul291's original
proof of concept, which was originally submitted as a PR to the
`falconry/falcon` repo.

About Falcon
------------

Falcon is a `bare-metal Python web
framework <http://falconframework.org/index.html>`__ for building lean and
mean cloud APIs and app backends. It encourages the REST architectural style,
and tries to do as little as possible while remaining `highly
effective <http://falconframework.org/index.html#Benefits>`__.


.. |Build Status| image:: https://travis-ci.org/falconry/falcon-require-https.svg
   :target: https://travis-ci.org/falconry/falcon-require-https
.. |codecov.io| image:: https://codecov.io/gh/falconry/falcon-require-https/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/falconry/falcon-require-https
