#!/bin/bash
# Developer Test Runner
#
PROJECT="filedepot"

echo "Cleaning .pyc files"
find . -type f -name "*.pyc" -print0 | xargs -r -0 rm
echo "Running PEP8 checks"
pep8 --exclude=settings.py,manage.py -r ${PROJECT} features/steps
if [ $? -ne 0 ]
then
    echo "PEP8 violations detected. Stopping run."
    exit 1
fi
echo "Running django-nose tests"
( cd ${PROJECT} ; python -Wall manage.py test --noinput --exe)
if [ $? -ne 0 ]
then
    echo "django-nose tests failed. Stopping run."
    exit 1
fi
echo "django-nose tests passed"

exit 0
