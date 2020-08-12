# Testing application from Arenadata (interview test task)


Before run tests you should run docker container with application which open on ```http://localhost:50000```

Project include api-tests and ui-tests. 
Test cases contains positive and negative scenarios.

**Technical stack:**
Python, pytest, requests, selenium, allure

Firstly, you need clone this repository to your host machine and open project in IDE (prefer PyCharm).

**For tests run:**
  - install virtual environment in you python project
    ```python -m venv env```
  - install necessary plugins 
    ```pip install -r requrements.txt```
  - run test cases
    ```pytest -v```
    
**If you want to get allure report -> use following command**
    ```pytest -v --alluredir=allure-report``` 
    
**Open allure report**
    ```allure serve allure-report```
