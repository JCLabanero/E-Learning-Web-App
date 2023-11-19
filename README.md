# E-Learning-Web-App

## Python Project 2023

## Table of Contents

- [Installation](#installation)

1.  Create a virtual environment

        python -m venv EnvironmentName

2.  Activate the environment to install dependencies and run the server

    2.1. Activate the environment outside/inside (2.1/2.2) EnvironmentName directory.

    - Outside EnvironmentName directory.

      ```
      EnvironmentName/scripts/activate
      ```

    - inside EnvironmentName directory.

      2.1.1. Change directory into EnvironmentName.

                cd EnvironmentName

      2.1.2. Run the active in EnvironmentName.

                scripts/activate

      2.2. if error says: filepath + cannot be loaded because running scripts is disabled on this system.

      2.2.1 Resolve by setting Execution Policy

              Set-ExecutionPolicy remotesigned -scope process

      2.2.2 Proceed to step 2.1

3.  Git Clone This Project
    - Make sure to cd into EnviromentName directory
    - After cloning cd into E-Learning-Web-App and install apps and dependencies
      ```
         pip install -r requirements.txt
      ```
      ```
         pip install --upgrade -r requirements.txt
      ```
4.  Fourt

- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![Version](https://img.shields.io/badge/Version-1.0-blue)
![License](https://img.shields.io/badge/License-MIT-red)

##Developer commands
\*save data from database

```
python Learn_Reactjs/manage.py dumpdata main --output Learn_ReactJS/main/fixtures/data.json
```

\*load data from database

```
python manage.py loaddata Learn_Reactjs/main/fixtures/data.json
```

##Start

```
Set-ExecutionPolicy remotesigned -scope process
```

```
../scripts/activate
```
