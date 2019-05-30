#!/bin/bash

set -e
echo "cleaning dist/*"
rm -rf dist/*

echo "Generating the binary package...."
python setup.py bdist_wheel --universal
python setup.py sdist

echo "Uploading the package to PyPi"
twine upload dist/*

scp dist/* glassfish@snurran.sics.se:/var/www/hops/hops-util-py/

