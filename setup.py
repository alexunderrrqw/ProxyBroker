import re
from setuptools import setup


# https://packaging.python.org/en/latest/distributing/

with open('proxybroker/__init__.py', 'r') as f:
    INFO = dict(re.findall(r"__(\w+)__ = '([^']+)'", f.read(), re.MULTILINE))

with open('README.rst', 'r') as f:
    INFO['long_description'] = f.read()

REQUIRES = ['aiodns', 'aiohttp', 'maxminddb']
PACKAGES = ['proxybroker', 'proxybroker.data']
PACKAGE_DATA = {'': ['LICENSE'], INFO['package']: ['data/*.gif', 'data/*.mmdb']}

setup(
    name=INFO['package'],
    version=INFO['version'],
    description=INFO['short_description'],
    long_description=INFO['long_description'],
    author=INFO['author'],
    author_email=INFO['author_email'],
    license=INFO['license'],
    url=INFO['url'],
    install_requires=REQUIRES,
    packages=PACKAGES,
    package_data=PACKAGE_DATA,
    platforms='any',
    entry_points={
        'console_scripts': [
            'proxybroker = proxybroker.cli:cli',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Internet :: Proxy Servers',
        'License :: OSI Approved :: Apache Software License',
    ],
    keywords='proxy finder grabber scraper parser graber scrapper checker broker async asynchronous http https connect socks socks4 socks5',
    zip_safe=False,
    test_suite='tests',
)
