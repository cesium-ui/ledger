
from database import Base, engine
from models import Account, Transaction

Base.metadata.create_all(bind=engine)
