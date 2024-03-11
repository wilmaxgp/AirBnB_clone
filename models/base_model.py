class BaseModel:
    """
    Base class for other classes with common attributes/methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes BaseModel instance with unique id and current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, 
                    datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                self.id, self.__dict__)

    def save(self, storage):
        """
        Updates updated_at attribute with 
        current datetime and saves to storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns dictionary representation of BaseModel instance.
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
