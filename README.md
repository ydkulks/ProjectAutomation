### Project Automation
  This code will help you to reduce the time taken to start coding before that creative ideas slip-out of you're brain while starting a new project.This uses Selenium interact with the browser and Bash script to run and use the code like a command rather than the conventional way of execution of code.
### Installation
```bash
git clone "https://github.com/ydkulks/ProjectAutomation.git"
```
### Requirements:
1)Linux/WSL terminal <br />
2)Python<br /> 
```bash 
sudo apt-get install python3 
```
3)Pip package management <br />
```bash
sudo apt-get Install python3-pip 
```
4)Selenium <br /> 
```bash 
pip3 install selenium 
```
5)Git in terminal <br />
```bash
sudo apt-get install git
```

### Set up(Linux/WSL):
1)Install webdriver for you're GoogleChrome web browser and copy past the address of that file in "create.py" at 10th line. <br />
2)Copy past the "create.py" python file and ".mycommand.sh" file in " ~/ "(home) directory.<br />
3)Go to ".bashrc" file and add "source <file-path>" to let bash know where the file resides.<br />
4)Custom changes required in "create.py" at 12th,20th,22nd line.<br />
5)Modify the user name and password for you're github account.<br />
6)Change the file path accordingly in ".mycommand.sh" file.<br />

### Usage:
 Open terminal and run:
```bash
newproject <project-name>
```
### Output:
 This is how it might look like when you run the code.
![Output after running the code](https://github.com/ydkulks/ProjectAutomation/blob/master/PA.png?raw=true)
