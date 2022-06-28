# Autotype
A quick and small python script that helps you autotype on websites that have copy paste disabled like Moodle, HackerEarth contests etc as it is difficult to efficiently debug your code on an online compiler.

**Works for both windows and linux**

<img src="./demo.gif?raw=true">

# Pre-requisites
Install python3.x, pip 

# Install the dependencies
`pip install -r requirements.txt`

### Run it as CLI app

Provide the path of the file to be autotyped and the delay time through teminal/shell.

`python3 command_line_script --path filePath --time delay_before_typing`

`python3 command_line_script -p filePath -t delay_before_typing`


### Run the GUI if you are not familiar with CLI apps.
- Run the script `python3 GUI_script.py`
<img src="demo_image/demo_gui.png">



### Run it as follows if you are not familiar with CLI apps.
Put the text inside `code` in `Simulator/simulate_keyboard.py` as follows

```
Line 13
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
- Run the script `python3 Simulator/simulate_keyboard.py`
- The script will start typing after 3s (you can change the wait time or delay)
- After running the script click on the window wherever you want to auto-type.

