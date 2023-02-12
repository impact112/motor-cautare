
from modules.database.common import *
from modules.database.entities.post import Post
from modules.database.entities.tag import Tag

engine = create_engine( 'sqlite:///test.db', echo = True )
Base.metadata.create_all( engine )

