from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Firefox(executable_path="C:/Users/geckodriver.exe")
    context.browser.get('http://127.0.0.1:5000')

@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Firefox(executable_path="C:/Users/geckodriver.exe")
    context.browser.get('http://127.0.0.1:5000/blog')

@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.browser.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.browser.current_url == expected_url

# Estas funciones se llaman igual, pero no hay problema porque ambas tienen decoradores
