# products-backend

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver


#Virtualenv Poetry

#Installation 
The installer script is available directly at install.python-poetry.org, and is developed in its own repository. The script can be executed directly (i.e. ‘curl python’) or downloaded and then executed from disk (e.g. in a CI environment).
Linux, macOS, Windows (WSL)
curl -sSL https://install.python-poetry.org | python3 -
Windows (Powershell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
#Activating the virtual environment 
The easiest way to activate the virtual environment is to create a nested shell with $poetry shell.

To deactivate the virtual environment and exit this new shell type $exit. To deactivate the virtual environment without leaving the shell use $deactivate.
