class InputMock:
    def __init__(self, inputs):
        self.__inputs = inputs
        self.__pos = 0
        self.call_count = 0

    def __call__(self, message):
        self.call_count += 1
        if self.__pos > len(self.__inputs):
            raise RuntimeError('No more inputs available')
        ret = self.__inputs[self.__pos]
        self.__pos += 1
        return ret
