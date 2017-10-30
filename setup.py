"""A setuptools module for the Saliency library.

See:
https://packaging.python.org/en/latest/distributing.html
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

exec(open('hopsfacets/version.py').read())

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hopsfacets',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=__version__,

    description='PyPi Facets for Jupyter Notebook',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/hopshadoop/facets',

    # Author details
    author='Google Inc., Logical Clocks AB',
    author_email='jim@logicalclocks.com',

    # Choose your license
    license='Apache 2.0',

    download_url = 'http://snurran.sics.se/hops/hops-util-py/hopsfacets-' + __version__ + '.tar.gz',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='jupyter deep learning big data visualization wrangling',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['hopsfacets'],

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #py_modules=['hopsfacets'],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['jupyter', 'tensorflow', 'numpy', 'pandas', 'protobuf'],
)

