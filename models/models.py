from typing import Optional

from pydantic import BaseModel


class Button(BaseModel):
    text: Optional[str] = None
    callback: Optional[str] = None


class Media(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    path: Optional[str] = None
