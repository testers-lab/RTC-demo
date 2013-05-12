from lettuce import step, world
from nose.tools import assert_equals


@step(u'Given I have welcomed the audience')
def given_i_have_welcomed_the_audience(step):
    print "Welcome RTC"


@step(u'When I choose the following products:')
def when_i_choose_the_following_products(step):
    world.items = step.hashes


@step(u'And I calculate the total price')
def and_i_calculate_the_total_price(step):
    world.total = 0
    for item in world.items:
        world.total += float(item['price'])


@step(u'Then I should see a total of "([^"]*)"')
def then_i_should_see_a_total_of_group1(step, expected_total):
    assert_equals(float(expected_total), world.total)
