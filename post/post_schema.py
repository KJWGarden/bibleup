from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum
from typing import List

class CreatePost(BaseModel):
    content: str
    category: List[int] | None = None

class CreationOrder(str, Enum):
    none = "None"
    latest = "latest"
    oldest = "oldest"
