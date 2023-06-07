from sqlalchemy import text
from app import db, app

sql = open("seed_data.sql", "r")
statement = sql.read()

with app.app_context():
    db.session.execute(text(statement))
    db.session.commit()
