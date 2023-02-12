
from modules.database.common import *
from modules.database.entities.tag_relationship import tag_relationships

class Post( Base ):
    __tablename__ = 'posts'
    id = Column( Integer, primary_key = True )
    parent_id = Column( Integer, ForeignKey('posts.id') )
    
    title = Column( String(256), nullable = False )
    description = Column( Text )
    #uploader_id = Column( Integer, ForeignKey('users.id') )
    views = Column( Integer, default = 0 )

    upload_ts = Column( Integer )
    edit_ts = Column( Integer )

    child_posts = relationship(
        'Post'
    )
    
    tags = relationship(
        'Tag',
        secondary = tag_relationships,
        back_populates = 'posts'
    )
