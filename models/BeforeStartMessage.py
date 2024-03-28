import json
from typing import Optional

from pydantic import BaseModel
from data.config import path_to_before_start_message as path
from models.models import Media, Button


class BeforeStartMessage(BaseModel):
    text: Optional[str] = None
    media: Optional[list[Media]] = None
    buttons: Optional[list[Button]] = None
    visibility: bool = True

    def __call__(self):
        return self.get()

    def get(self):
        message = self.load()
        return BeforeStartMessage(**message)

    def get_media(self):
        return self.media

    def change_visibility(self):
        self.visibility = not self.visibility
        self.save()

    def new_media(self, el: Media):
        self.media.append(el)
        self.save()

    def del_media(self, name: str) -> bool:
        for ind in range(len(self.media)):
            el = self.media[ind]
            if el.name == name:
                del self.media[ind]
                self.save()
                return True
        return False

    def new_keyboard(self, el: Button):
        self.keyboard.append(el)
        self.save()

    def del_keyboard(self, callback: str) -> bool:
        for ind in range(len(self.buttons)):
            el = self.buttons[ind]
            if el.callback == callback:
                del self.buttons[ind]
                self.save()
                return True
        return False

    @staticmethod
    def load() -> dict:
        with open(path, "r+", encoding="UTF-8") as f:
            obj: dict = json.load(f)
        return obj

    def save(self, data: dict = None) -> None:
        if data is None:
            data = self.parse_message()
        with open(path, "w+", encoding="UTF-8") as f:
            json.dump(data, f, indent=4)

    def new(self):
        message = {
            "text": "new message",
            "media": [{"name": "name_1", "type": "type_1", "path": "path_1"},
                      {"name": "name_2", "type": "type_2", "path": "path_2"}],
            "buttons": [{"text": "text_1", "callback": "callback_1"}, {"text": "text_2", "callback": "callback_2"}],
            "visibility": True
        }
        self.save(message)
        return BeforeStartMessage(**message)

    def parse_message(self) -> dict:
        data = self.__dict__
        data["media"] = list(el.__dict__ for el in self.media)
        data["buttons"] = list(el.__dict__ for el in self.buttons)
        return data
