from lettuce import *

from django.conf import settings
from django.core.management import call_command
from django.test import Client
from django.db import connection


@before.all
def initial_setup():
    world.browser = Client()
    world.testdb = connection.creation.create_test_db(
        verbosity=2,
        autoclobber=False,
    )


@after.all
def teardown_browser(total):
    connection.creation.destroy_test_db(world.testdb, verbosity=2)


@after.each_scenario
def before_each_feature(scenario):
    call_command('flush', **{
        'settings': settings.SETTINGS_MODULE,
        'interactive': False,
        'verbosity': 1
    })
