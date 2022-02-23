class Script:
    def __init__(self, name, content, id, features):
        self.name = name
        self.content = content
        self.id = id
        self.features = features

    def get_name(self):
        return self.name
    def get_content(self):
        return self.content
    def get_id(self):
        return self.id
    def get_features(self):
        return self.features

    def set_name(self, name):
        self.name = name
    def set_content(self, content):
        self.content = content
    def set_id(self, id):
        self.id = id
    def set_features(self, features):
        self.features = features
