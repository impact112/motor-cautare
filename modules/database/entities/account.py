
from modules.database.common import *

class Account( Base ):
    __tablename__ = 'accounts'
    id = Column( Integer, primary_key = True )
    username = Column( String(64), unique = True )
    profile_name = Column( String(128), unique = True )
    description = Column( Text )

    auth_digest = Column( String )
    registration_ts = Column( Integer )
    power_level = Column( Integer, default = 0 )

