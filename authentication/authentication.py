from database.schema import Session, User, engine
from werkzeug.security import check_password_hash

def authenticate(username, password):
    
    session = Session(bind=engine)
    user = session.query(User).filter(User.username==username).first()
    if user: 
        password_check = check_password_hash(user.password, password)
        if password_check: return user
    
    return None

def verify_credentials(username, password):

    if not username or not password:
        return None, 'Please provide username and password fields'
    
    user = authenticate(username, password)
    if user: ret = user, 'Credentials have been verified'
    else: ret = None, 'Credentials could not be verified'
    return ret