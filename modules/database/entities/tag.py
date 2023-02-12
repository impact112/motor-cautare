
from modules.database.common import *
from modules.database.entities.tag_relationship import tag_relationships

class Tag( Base ):
    __tablename__ = 'tags'
    id = Column( Integer, primary_key = True )
    parent_id = Column( Integer, ForeignKey('tags.id') )
    
    name = Column( String(256), unique = True )
    description = Column( Text )

    parent_tag = relationship( 'Tag' )
    posts = relationship(
        'Post',
        secondary = tag_relationships,
        back_populates = 'tags'
    )
