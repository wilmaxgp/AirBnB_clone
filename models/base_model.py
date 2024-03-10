import uuid
from datetime import datetime

class BaseModel:
    """
    Base class for other classes with common attributes/methods.
    """

    def __init__(self):
        """
        Initializes BaseModel instance with unique id and current datetime.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates updated_at attribute with current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns dictionary representation of BaseModel instance.
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
