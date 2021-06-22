# Autotype
A quick and small python script that helps you autotype on websites that have copy paste disabled like Moodle, HackerEarth contests etc as it is difficult to efficiently debug your code on an online compiler.

<img src="./demo.gif?raw=true">

# Pre-requisites
Install python3.x, pip 

# Install the dependencies
`pip install -r requirements.txt`

### Run it as CLI app

Provide the path of the file to be autotyped and the delay time through teminal/shell.

`python3 simulate_keyboard --path filePath --time delay_before_typing`

`python3 simulate_keyboard -p filePath -t delay_before_typing`


### Run it as follows if you are not familiar with CLI apps.
Put the text inside `code` in `simulate_keyboard.py` as follows

```
Line 14
code = """
    #include<bits/stdc++.h>
    {
        .
        .
        .
    }
"""
Make sure to use triple quotes as it will preserve the code format.
```
- Run the script `python3 simulate_keyboard.py`
- The script will start typing after 3s (you can change the wait time or delay)
- After running the script click on the window wherever you want to auto-type.
 
