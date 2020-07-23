from model import model
class controller:

    # This is the logic
    def counter(self,name):
        count = len(name)

        modelObj = model()
        modelObj.insert(name,count)

        return count