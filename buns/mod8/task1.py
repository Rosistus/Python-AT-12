
class Transport():
    def __init__(self, *args, **kwargs):
        # Значения координат записываются в виде списка из двух значений, где первое - координата x, вторая - y
        if args:
            self.coordinates = [args[0], args[1]]
            self.speed = args[2]
            self.brand = args[3]
            self.year = args[4]
            self.number = args[5]
        else:
            self.coordinates = kwargs.get('coordinates')
            self.speed = kwargs.get('speed')
            self.brand = kwargs.get('brand')
            self.year = kwargs.get('year')
            self.number = kwargs.get('number')

    def __str__(self):
        string = ""
        for key, value in self.__dict__.items():
            string += f"{key[1:]}: {value}\n"
        return string

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        if self.coordinates[0] in range(pos_x, pos_x + length+1) and self.coordinates[1] in range(pos_y, pos_y + width+1):
            return True
        else:
            return False

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value, **kwargs):
        if value:
            self._coordinates = value
        elif kwargs:
            self._coordinates = kwargs.get('coordinates')
        else:
            raise ValueError("Ошибка - неправильно введенное значение координат")

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value >= 0 and isinstance(value, int):
            self._speed = value
        else:
            raise ValueError("Ошибка - неправильно введенное значение скорости")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            raise ValueError("Ошибка - неправильно введенное значение брэнда")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if isinstance(value, int):
            self._year = value
        else:
            raise ValueError("Ошибка - неправильно введенное значение года")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if isinstance(value, int):
            self._number = value
        else:
            raise ValueError("Ошибка - неправильно введенное значение номера")


class Passenger():

    def __init__(self, *args, **kwargs):
        if args:
            self.passengers_capacity = args[0]
            self.number_of_passengers = args[1]
        else:
            self.passengers_capacity = kwargs.get('passengers_capacity')
            self.number_of_passengers = kwargs.get('number_of_passengers')

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, value):
        if isinstance(value, int):
            self._passengers_capacity = value
        else:
            raise ValueError("Ошибка - неправильно введенное значение вместимости пассажиров")

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, value):
        if isinstance(value, int):
            self._number_of_passengers = value
        else:
            raise ValueError("Ошибка - неправильно введенное значение количества пассажиров")

    def __str__(self):
        string = ""
        for key, value in self.__dict__.items():
            string += f"{key[1:]}: {value}\n"
        return string


class Cargo:
    def __init__(self, value):
        self._carrying = value

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, new_value):
        if isinstance(new_value, int):
            self._carrying = new_value
        else:
            raise ValueError("Ошибка - неправильно введенное значение грузоподъемности")


class Plane(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if args:
            self._height = args[6]
        else:
            self._height = kwargs.get('height')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            self._height = value
        else:
            raise ValueError("Ошибка - неправильно введенное значение высоты")


class Auto(Transport):
    # В исходном файле не было отличительных полей у этого класса, поэтому я добавил поле color
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if args:
            self._color = args[6]
        else:
            self._color = kwargs.get('color')

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str):
            self._color = value
        else:
            raise ValueError("Ошибка - неправильно введенно значение цвета")


class Ship(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if args:
            self._name = args[6]
            self._port = args[7]
        else:
            self._name = kwargs.get('name')
            self._port = kwargs.get('port')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Ошибка - неправильно введенное значение высоты")

    @property
    def port(self):
        return self._port

    @name.setter
    def port(self, value):
        if isinstance(value, str):
            self._port = value
        else:
            raise ValueError("Ошибка - неправильно введенное значение высоты")


class Car(Auto):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Bus(Passenger, Auto):
    def __init__(self, *args, **kwargs):
        Auto.__init__(self, *args, **kwargs)
        Passenger.__init__(self, *args[7:], **kwargs)


class CargoAuto(Cargo, Auto):
    def __init__(self, *args, **kwargs):
        Auto.__init__(self, *args, **kwargs)
        Cargo.__init__(self, args[7])


class Boat(Ship):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PassengerShip(Ship, Passenger):
    def __init__(self, *args, **kwargs):
        Ship.__init__(self, *args, **kwargs)
        Passenger.__init__(self, *args[8:], **kwargs)


class CargoShip(Ship, Cargo):
    def __init__(self, *args, **kwargs):
        Ship.__init__(self, *args, **kwargs)
        Cargo.__init__(self, args[8])


class AirPlane(Plane):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PassengerPlane(Plane, Passenger):
    def __init__(self, *args, **kwargs):
        Plane.__init__(self, *args, **kwargs)
        Passenger.__init__(self, *args[7:], **kwargs)


class CargoPlane(Plane, Cargo):
    def __init__(self, *args, **kwargs):
        Plane.__init__(self, *args, **kwargs)
        Cargo.__init__(self, args[7])


class SeaPlane(Plane, Ship):
    def __init__(self, *args, **kwargs):
        Plane.__init__(self, *args, **kwargs)
        ship_args = [i for i in args]
        ship_args.pop(6)
        ship_args = tuple(ship_args)
        Ship.__init__(self, *ship_args, **kwargs)
