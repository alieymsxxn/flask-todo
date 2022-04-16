from werkzeug.security import generate_password_hash
from .schema import User, engine, Base, Session

def init_db():
    '''
    This function is reponsible for setting up the database
    '''
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    
    admin = session.query(User).filter(User.username=='root').first()
    if admin: 
        return 
    admin = User(username='root', email='admin@admin.com', password=generate_password_hash('root'))
    session.add(admin)
    session.commit()

