from setuptools import setup

setup(
    name = 'cylanceprotect',
    packages = ['cylanceprotect'], # this must be the same as the name above
    version = '0.1',
    description = 'Python library for interacting with the Cylance Protect API v2.0 rev9',
    author = 'Armando Quintana',
    author_email = 'armando.quintananieves@gmail.com',
    url = 'https://github.com/zer0Trac3/cylanceprotect',
    download_url = 'https://github.com/zer0Trac3/cylanceprotect/archive/0.1.tar.gz',
    install_requires=['requests>=2.18.4','PyJWT>=1.6.1'],
    requires='requests',
    keywords = ['cylance', 'CylanceProtect', 'Cylance Protect', 'Cylance Protect API'], # arbitrary keywords
    classifiers = ['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'Natural Language :: English',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: MacOS :: Linux'],
)