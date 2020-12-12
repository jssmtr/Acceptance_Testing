Feature: Test that pages hace correct content
  Scenario: Blog page has a correct title
    Given I am on the blog page
    Then There is a title shown on the page
    And The title tag has content "This is the blog page"
    # Lo que hay entre "" es una variable, usaremos el re_matcher para mapearla.
    # And repite el paso anterior.