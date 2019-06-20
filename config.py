import web

db_host = 'z1ntn1zv0f1qbh8u.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'ewjs9gackau6q79q' # Database
db_user = 'r5b9tus43ikka4kz' # Username
db_pw = 'geujd68ew3btwya4' # Password

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )