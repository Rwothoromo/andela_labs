class Car(object):
    def __init__(self,type=None,model='GM',name='General'):
        self.type = type
        self._model = model
        self._name  = name
        self._doors=4
        self._wheels=4
        self.speed = 0

    @property
    def name(self):
        return self._name
    @property
    def model(self):
        return self._model

    @property
    def num_of_doors(self):
        if self.type=='Porshe' or self.type == 'Koenigsegg':
            return 2
        else:
            return 4
    @property
    def num_of_wheels(self):
        if self._name=='trailer':
            return 8
        else:
            return 4 
    def is_saloon(self):
        if self._name !='trailer':
            return 'saloon'
        else:
            return 'trailer'
    def drive(self,speed):
        if self.name=='trailer':
            self.speed=77
        else:
            self.speed=1000
        return self