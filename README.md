# Task Manager Application

## How The App Was Built

1. Access the gitpod template provided by Code Institute [Full-Template](https://github.com/Code-Institute-Org/gitpod-full-template)

2. Install required packages

- Flask, SQLAlchemy and Psyocpg2
```
pip3 install 'Flask-SQLAlchemy<3' psycopg2
```

3. Create python environemnt file to store sensitive data that wont be shared on the final application

```
touch env.py
```

4. Create a Package folder named `taskmanager`
    -  Inside the folder creat a filder to 