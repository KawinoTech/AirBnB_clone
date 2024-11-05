from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    The BaseModel class provides a foundation for other classes in the project.
    It defines common attributes and methods that can be shared across all derived classes.
    Each instance of BaseModel is assigned a unique identifier and timestamps
    for creation and last update, along with utility methods for saving and
    converting instance data to a dictionary format.

    Attributes:
        id (str): A unique identifier for each instance, generated using uuid4.
        created_at (datetime): The timestamp when the instance was created.
        updated_at (datetime): The timestamp of the last update to the instance.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class. Each instance is
        assigned a unique ID and timestamped upon creation. The updated_at
        attribute is also initialized to the creation time.

        Attributes:
            id (str): The unique identifier generated with uuid4 for the instance.
            created_at (datetime): Timestamp for when the instance is created.
            updated_at (datetime): Timestamp initially set to creation time
                                   and updated on each save.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance,
        including the class name, ID, and all attribute values.

        Returns:
            str: A formatted string in the format "[ClassName] (id) {attributes}".
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime. This
        method is intended to be called whenever the instance is modified,
        providing an accurate timestamp of the last modification.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance attributes to a dictionary format, making it
        easier to serialize and save the instance data. This includes all
        instance attributes and an additional __class__ key to indicate
        the class name.

        Returns:
            dict: A dictionary containing all instance attributes, with
                  datetime attributes in ISO format, along with a __class__ key.
        """
        dict1 = {'__class__': type(self).__name__}
        for k, v in self.__dict__.copy().items():
            if k == 'created_at' or k == 'updated_at':
                v = v.isoformat()
            dict1[k] = v
        return dict1
