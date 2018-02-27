### Flask, SQLAlchemy, SQLlite, Bootstrap app

### Install Dependancies:
```pip install -r requirements.txt```

### Start python virtual environment:
```source venv/bin/activate```


### Set Flask env variable & server restart on code change:
 - ```export FLASK_APP=server.py```
 - ```export FLASK_DEBUG=1```
 - Run server: ```flask run```

### Create DB Migration Repo:
 ```flask db init``` 
 - will create a new migrations directory
 - Application uses SQLlite, can integrate postgres if needed

### Initialize migration:
```flask db migrate -m "table name"``` 
 - flag descriptive text to migration
 - will compare models to actual db and generate script to handle changes to models

### Apply changes to db:
```flask db upgrade```
 - Creates new DB with models applied, will generate new file app.db
 - Note: If using Postgres, will need to create db first before running command.

### Remove changes to db:
 ```flask db downgrade```

### Start flask shell:
```flask shell``` 

### Add test user to db:
 ``` flask shell```
 ```new_user = User(username='whatever', email='test@example.com')```
 ```new_user.set_password('whatever')```
 ```db.session.add(new_user)```
 ```db.session.commit()```
