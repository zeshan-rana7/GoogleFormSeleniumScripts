*** Settings ***
Documentation    Testing MercuryTours Website
Library          Selenium2Library
Library          BuiltIn

*** Variable ***
${URL}  http://newtours.demoaut.com/
${title}  Welcome: Mercury Tours
${timeout}  3s
*** Test Cases ***
TestCase1: Navigateing Mercury WebPage
    [Tags]    DEBUG
    [Setup]
        Open Mercury Website in Firefox and Maximize
        Verify the Home page title
        sleep  ${timeout}
        Click on Sign-On Link
    [Teardown]  Close Browser

*** Keywords ***
Open Mercury Website in Firefox and Maximize
    Open Browser  url=${URL}  browser=firefox
    Maximize Browser Window
    Log to console  Website Navigated successfully
Verify the Home page title
    Title Should Be  ${title}
    Log to console  Home page  Title Verified
Click on Sign-On Link
    Click Element  xpath=html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]
    Log to console  Clicked on Signon link successfully