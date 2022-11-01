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
    -  Inside the folder create a folder to 


## Bugs

- Create defensive programming for add and edit category
- Redirect the edit task page to route to Tasks.html

## Deployment

1. Create dependencies
    -  to view our installed packages
```
pip3 list
```

2.  Create a requirements text file
```
pip3 freeze --local > requirements.txt
```
**REMEMBER** when you install new packages you must update your `requiremnets.txt` file

3. Create Procfile for `Heroku`
```
echo web: python run.py > Procfile
```
**When done correctly, you will see the file appear on your workspace and then you will be ready to move forward**

4. Add both `requirements.txt` and `Procfile` to our `repository`
```
git add requirements.txt
git commit -m "add requirements.txt"
```
Then add the Procfile to the staging area
```
git add Procfile
git commit -m "add Procfile"
```
Then push to your `repo`
```
git push
```

5. Then Log into your `Heroku account`
    - On the `Dashboard` navigate to `create new app`

6. Create New App
    -   App Name: **Must** be unique
    -   Region: Preferably Europe