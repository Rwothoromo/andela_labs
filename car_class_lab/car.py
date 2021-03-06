class Car(object):
    def __init__(self,name='General',model='GM',type=None):
        self.type = type
        self._model = model
        self._name  = name
        self._num_of_doors = 4
        self._num_of_wheels = 4
        self.speed = 0

    @property
    def name(self):
        return self._name

    @property
    def model(self):
        return self._model

    @property
    def num_of_doors(self):
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            return 2
        else:
            return 4

    @property
    def num_of_wheels(self):
        if self.type == 'trailer':
            return 8
        else:
            return 4

    def is_saloon(self):
        if self.type != 'trailer':
            return 'saloon'
        else:
            return 'trailer'

    def drive(self,speed):
        if self.type == 'trailer':
            self.speed = 77
        else:
            self.speed = 1000
        return self
