*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  Anna
    Set Password  testi1
    Set Password Confirmation  testi1
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  Mikko
    Set Password  testisalasana
    Set Password Confirmation  testisalasana
    Submit Credentials
    Register Should Fail With Message  Password can't only contain letters

Register With Nonmatching Password And Password Confirmation
    Set Username  Jaakko
    Set Password  ekasalasana1
    Set Password Confirmation  tokasalasana1
    Submit Credentials
    Register Should Fail With Message  Nonmatching password and password confirmation

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  testi321
    Set Password Confirmation  testi321
    Submit Credentials
    Register Should Fail With Message  User with username kalle already exists

Login After Successful Registration
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Click Link  Continue to main page
    Click Button  Logout
    Go To Login Page
    Set Username  ville
    Set Password  ville123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  Jaakko
    Set Password  ekasalasana1
    Set Password Confirmation  tokasalasana1
    Submit Credentials
    Go To Login Page
    Set Username  Jaakko
    Set Password  ekasalasana1
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page