class APIController:
    list = ["a", "b", "c", "d", "e"]
    def fetchNames(self):
        return "Hello world {list}".format(list=self.list)