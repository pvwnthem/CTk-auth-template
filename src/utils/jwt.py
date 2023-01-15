import jwt
import tinydb
class Jwt:
    def __init__(self, instances):
        self.instances = instances

    
    def jwt_decode(self):
        """Decode a JWT token."""
        User = tinydb.Query()
        return jwt.decode(self.instances["db"].search(User.token.exists())[0]["token"], "NATEHIGGERS", algorithms=["HS256"])