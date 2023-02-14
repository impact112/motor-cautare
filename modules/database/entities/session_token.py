
from modules.database.common import *

class SessionToken(Base):
    __tablename__ = 'session_tokens'
    id = Column( Integer, primary_key = True )
    user_id = Column( Integer, ForeignKey('accounts.id') )
    token = Column( String(64), unique = True )

