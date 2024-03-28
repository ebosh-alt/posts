import json


class Menu:
    def __init__(self, path):
        self.path = path

    def new_category(self, category):
        data = self.get()
        keyboard = data.get("keyboard")
        keyboard[category] = {}
        data["keyboard"] = keyboard
        self.save(data)

    def get(self) -> dict:
        with open(self.path, "r+", encoding="UTF-8") as f:
            obj: dict = json.load(f)
        return obj

    def save(self, obj) -> None:
        with open(self.path, "w+", encoding="UTF-8") as f:
            json.dump(obj, f, indent=4)

    def new_menu(self, caption: str, media: list):
        new_menu = {
            "caption": caption,
            "media": media,
            "keyboard": {}
        }

        self.save(new_menu)


if __name__ == "__main__":
    menu = Menu("../data/data.json")
    menu.new_menu("hello world", media=["photo1", "photo2", "photo3", "photo4"])
    menu.new_category("category1")
    menu.new_category("category2")
    menu.new_category("category3")