import imp
import io
from os import path

from setuptools import find_packages, setup

VERSION = imp.load_source('version', path.join('.', 'falcon_require_https', 'version.py'))
VERSION = VERSION.__version__


setup(
    name='falcon-require-https',
    version=VERSION,
    description='Falcon middleware for sanity-checking that HTTPS was used for the request.',
    long_description=io.open('README.rst', 'r', encoding='utf-8').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='wsgi web api framework rest http https tls cloud security',
    author='paul291',
    url='https://github.com/falconry/falcon-require-https',
    license='Apache 2.0',
    packages=find_packages(exclude=['tests']),
    install_requires=['falcon'],
    setup_requires=['pytest-runner'],
    tests_require=['falcon', 'pytest'],
)
