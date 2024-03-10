from models.engine.file_storage import FileStorage
from .user import User

storage = FileStorage()
storage.reload()