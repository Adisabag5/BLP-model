class State:
    def __init__(self, userName, classification, classificationValue, world):
        self.userName = userName
        self.classification = classification
        self.classificationValue = classificationValue
        self.world = world


    def update_current_state(self):
        self.userName = userName
        self.classification = classification
        self.classificationValue = classificationValue
        self.world = world


    def toString(self):
        print("userName:                " + self.userName)
        print("classification:          " + self.classification)
        print("classificationValue:     " + str(self.classificationValue))
        print("Belong to the world:     " + self.world)
