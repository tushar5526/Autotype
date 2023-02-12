# Autotype 🖊

A quick and small python script that helps you autotype on websites that have copy paste disabled like Moodle, HackerEarth contests etc as it is difficult to efficiently debug your code on an online compiler.

[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/codingid6)
[![GitHub issues](https://img.shields.io/github/issues/tushar5526/Autotype)](https://github.com/tushar5526/Autotype/issues)
[![GitHub forks](https://img.shields.io/github/forks/tushar5526/Autotype)](https://github.com/tushar5526/Autotype/network)
[![GitHub stars](https://img.shields.io/github/stars/tushar5526/Autotype)](https://github.com/tushar5526/Autotype/stargazers)
[![GitHub license](https://img.shields.io/github/license/tushar5526/Autotype)](https://github.com/tushar5526/Autotype/blob/main/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) ![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square) ![GitHub contributors](https://img.shields.io/github/contributors-anon/tushar5526/Autotype) 
<br>

**Works for windows, mac and linux**

<img src="./demo.gif?raw=true">

# Pre-requisites
`python3.9.x`   
`pip`

# Development Setup
- Create a new virtual environment using `pipenv`
```bash
pip install pipenv --user

# create venv and install dependencies from Pipfile
pipenv install
```
- Activate the environment
```bash
pipenv shell

# check if activated
pip -V
```


- Run it as CLI app

> Provide the path of the file to be autotyped and the delay time through teminal/shell.

```bash
python3 command_line_script --path filePath --delay delay_before_typing
```


### Run the GUI if you are not familiar with CLI apps.

- Run the script `python3 GUI_script.py`
<img src="demo_image/demo_script_gui.png">

- You can simply type your code in the textbox , enter the time delay and click the `Start Typing` button.The script will then type your code for you.
![](https://github.com/RyanWalker277/Autotype/blob/main/demo_image/type_code.gif)

- If your code is in a file , then leave the textbox blank , enter the time delay and click `Start Typing` button.A file exploror prompt will open asking you to select the file.Simply select your file and Done! Autotype will type your code for you.
![](https://github.com/RyanWalker277/Autotype/blob/main/demo_image/open_file.gif)

- There are two themes in the GUI Script: Dark and Light. By clicking the toggle in the bottom left corner of the window, you can switch between the two.
![](https://github.com/RyanWalker277/Autotype/blob/main/demo_image/themes.gif)

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
# Make sure to use triple quotes as it will preserve the code format.
```
- Run the script `python3 Simulator/simulate_keyboard.py`
- The script will start typing after 3s (wait or delay time can be tuned)
- After running the script click on the window to move your cursor wherever you want to auto-type.
<hr>

![32](https://user-images.githubusercontent.com/108119109/218298259-39330c4c-8703-42f4-80f4-dd2a1c3fe807.gif)
![deucj](https://user-images.githubusercontent.com/108119109/218298371-49a38dfa-45f8-4360-a72d-3cbe723b437f.gif)
![final-online-video-cuttercom](https://user-images.githubusercontent.com/108119109/218298400-ef5798ec-6f8b-4b05-9ba5-c60bf50fefcd.gif)


YT link 🔗 -  https://youtu.be/SftSe187Klc

## 💪 Thanks to all Wonderful Contributors

Thanks a lot for spending your time helping AutoType grow.   
Thanks a lot! Keep rocking 🍻

[![Contributors](https://contrib.rocks/image?repo=tushar5526/Autotype)](https://github.com/tushar5526/Autotype/graphs/contributors)

## 🙏 Support++

This project needs your shiny star ⭐.   
Don't forget to leave a star ⭐️

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)




