from lettuce import step, world
from lettuce.django import django_url

from django.core.urlresolvers import reverse
from nose.tools import assert_equals


@step(u'Given I go to the register page')
def given_i_go_to_the_register_page(step):
    world.response = world.browser.get(
        django_url(reverse('registration_register'))
    )


@step(u'When I fill the password field with "([^"]*)"')
def when_i_fill_the_password_field_with_group1(step, value):
    world.browser.find_element_by_name('password1').send_keys(value)


@step(u'Then I should see the correct password "([^"]*)"')
def then_i_should_see_the_correct_password_group1(step, expected_pass_str):
    pass_strength = world.browser.find_element_by_css_selector(
        'span.help-inline'
    ).text
    assert_equals(expected_pass_str, pass_strength)
