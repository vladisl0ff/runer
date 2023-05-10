import json

class Table:
    def __init__(self, filename):
        with open(filename, "r") as f:
            self.filename = filename
            self.data = json.load(f)

    def get_person_data(self, name):
        for person in self.data["people"]:
            if person["name"] == name:
                return person
        return None

    def set_person_points(self, name, points):
        for person in self.data["people"]:
            if person["name"] == name:
                person["points"] = points
                with open(self.filename, "w") as f:
                    json.dump(self.data, f, indent=4)
                break

    def set_person_chat(self, name, chat):
        for person in self.data["people"]:
            if person["name"] == name:
                person["chat"] = chat
                with open(self.filename, "w") as f:
                    json.dump(self.data, f, indent=4)
                break

    def set_person_victories(self, name, victories):
        for person in self.data["people"]:
            if person["name"] == name:
                person["victories"] = victories
                with open(self.filename, "w") as f:
                    json.dump(self.data, f, indent=4)
                break

