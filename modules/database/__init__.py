
from modules.database.common import *
from modules.database.entities.post import Post
from modules.database.entities.tag import Tag
from modules.database.entities.account import Account, SessionToken
#from modules.database.entities.session_token import SessionToken

engine = create_engine( 'sqlite:///test.db', echo = True )
Base.metadata.create_all( engine )

Session = sessionmaker( bind = engine )
session = Session()
