# Autotype 🖊

A quick and small python script that helps you autotype on websites that have copy paste disabled like Moodle, HackerEarth contests etc as it is difficult to efficiently debug your code on an online compiler.

[![GitHub issues](https://img.shields.io/github/issues/tushar5526/Autotype)](https://github.com/tushar5526/Autotype/issues)
[![GitHub forks](https://img.shields.io/github/forks/tushar5526/Autotype)](https://github.com/tushar5526/Autotype/network)
[![GitHub stars](https://img.shields.io/github/stars/tushar5526/Autotype)](https://github.com/tushar5526/Autotype/stargazers)
[![GitHub license](https://img.shields.io/github/license/tushar5526/Autotype)](https://github.com/tushar5526/Autotype/blob/main/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) ![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square) ![GitHub contributors](https://img.shields.io/github/contributors-anon/tushar5526/Autotype) 
<br>

**Works for windows, mac and linux**

<img src="./demo.gif?raw=true">

# Pre-requisites
Install python3.x, pip 

# Install the dependencies

`pip install -r requirements.txt`

### Run it as CLI app

Provide the path of the file to be autotyped and the delay time through teminal/shell.

`python3 command_line_script --path filePath --delay delay_before_typing`

### Run it Global Commandline Executable

If you are a Linux or a Macos user just add AutoType to Your .zshrc or .bashrc file

```console
~$ chmod +x Autotype
```

```console
~$ vim .zshrc # For zshrc default shell
```

```console
~$ vim .bashrc # For zshrc default shell
```

Add Autotype to your PATH in your .zshrc or .bashrc file 
```bash
export PATH="$PATH:path of autotype"
```

Restart the terminal
```console
~$ Autotype --help
```


### Run the GUI if you are not familiar with CLI apps.
- Run the script `python3 GUI_script.py`
<img src="demo_image/demo_script_gui.png">



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
<hr>

## 💪 Thanks to all Contributors

Thanks a lot for spending your time helping AutoType grow. Thanks a lot! Keep rocking 🍻

[![Contributors](https://contrib.rocks/image?repo=tushar5526/Autotype)](https://github.com/tushar5526/Autotype/graphs/contributors)

## 🙏 Support

This project needs a ⭐️ from you. Don't forget to leave a star ⭐️

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)




