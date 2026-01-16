from behave import given, step, when, then
#Importáld a number_checker modult a src mappából
from src import number_checker


#TODO: Implementáld a Given step-et
@given('the number is 4')
def step_given_number(context):
    context.number = 4


# TODO: Implementáld a When step-et
# Használd a check_number függvényt a src/number_checker.py fájlból!
@when('I check the number')
def step_when_check_number(context):
    context.result = number_checker.check_number(context.number)


# TODO: Implementáld a Then step-et
@then('I should be told "{expected}"')
def step_then_result(context, expected):
    assert context.result == expected
