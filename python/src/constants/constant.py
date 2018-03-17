class Constant:
    STRING_LENGTH_SIX = 6

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise "Can't rebind const(%s)" % name