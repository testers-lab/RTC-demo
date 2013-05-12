Demo AUT for Romanian Testing Comunity
======================================

###### Install dependencies:
`pip install https://bitbucket.org/ubernostrum/django-registration/get/tip.tar.gz`

`pip install -r requirements.txt`

###### Run tests:

`python manage.py harvest tests/lettuce_djangoclient_tests --settings=rtc.settings`

`python manage.py harvest tests/lettuce_selenium_tests --settings=rtc.settings`
