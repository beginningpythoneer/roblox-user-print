# Roblox User Print
![demo](https://github.com/beginningpythoneer/roblox-user-print/blob/main/demo1.png?raw=true)
This tool prints key Roblox user details right into your terminal:
- Display name
- Username
- Registration date
- Description

It also displays whether they are banned or verified.
### Tool usage
0. I prefer to create a venv (virtual enviroment) for each project:

    ```shell
    python -m venv venv
    ```
    Activate it with the correct script for your OS (Windows/Linux) and shell (bash/fish)
1. Install the requirements:
    ```shell
    pip install -r requirements.txt
    ```
2. Launch it!
    ```shell
    python main.py -u 1
    ```
    Where 1 is target`s UserID

### AI Usage
AI Was used to clean up the code (catching specific exceptions, dataclasses). Main logic, the API interact part and everything else was writted by me with the help of Google and StackOverflow.