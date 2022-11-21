class Time:
    # The init method runs when we create a new object of type Time.
    # Time objects can be created with any number of hours, minutes,
    # and seconds.
    def __init__(self, hour=0, minute=0, second=0):
        self.second = second
        self.minute = minute
        self.hour = hour

        if self.second >= 60:
            self.minute += self.second // 60
            self.second = self.second % 60

        if self.minute >= 60:
            self.hour += self.minute // 60
            self.minute = self.minute % 60

    # __str__ special method: Convert a Time object to a string
    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)

    # Operator overloads for relational operators with type-based dispatch
    # =========================================
    def __gt__(self, other):
        self_seconds = self.time_to_seconds()
    
        if isinstance(other, Time):
            other_seconds = other.time_to_seconds()
        else:
            other_seconds = other

        return self_seconds > other_seconds

    def __lt__(self, other):
        self_seconds = self.time_to_seconds()
    
        if isinstance(other, Time):
            other_seconds = other.time_to_seconds()
        else:
            other_seconds = other

        return self_seconds < other_seconds

    def __ge__(self, other):
        self_seconds = self.time_to_seconds()
    
        if isinstance(other, Time):
            other_seconds = other.time_to_seconds()
        else:
            other_seconds = other

        return self_seconds >= other_seconds

    def __le__(self, other):
        self_seconds = self.time_to_seconds()
    
        if isinstance(other, Time):
            other_seconds = other.time_to_seconds()
        else:
            other_seconds = other

        return self_seconds <= other_seconds

    def __eq__(self, other):
        self_seconds = self.time_to_seconds()
    
        if isinstance(other, Time):
            other_seconds = other.time_to_seconds()
        else:
            other_seconds = other

        return self_seconds == other_seconds

    # Right-side relational operator overloads
    # Note we can just pass through a call to the non-right-side variants
    # since they both do the same thing.

    # Operator overloads for math operators with type-based dispatch
    # =========================================
    def __rgt__(self, other):
        return self.__gt__(other)

    def __rge__(self, other):
        return self.__ge__(other)

    def __rlt__(self, other):
        return self.__lt__(other)

    def __rle__(self, other):
        return self.__le__(other)

    def __req__(self, other):
        return self.__eq__(other)



    # Operator overloads for math operators with type-based dispatch
    # =========================================
    def __add__(self, other):
        if isinstance(other, Time):
            s1 = self.time_to_seconds()
            s2 = other.time_to_seconds()
            return Time(second=s1 + s2)
        else:
            s1 = self.time_to_seconds()
            return Time(second=s1 + other)

    def __sub__(self, other):
        if isinstance(other, Time):
            s1 = self.time_to_seconds()
            s2 = other.time_to_seconds()
            return Time(second=s1 - s2)
        else:
            s1 = self.time_to_seconds()
            return Time(second=s1 - other)

    # Right-side add/subtract operator overloads
    # Note we can just pass through a call to the non-right-side variants
    # since they both do the same thing.
    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)
        
    # Other methods
    # =========================================
    def time_to_seconds(self):
        seconds = self.hour * 60 * 60
        seconds += self.minute * 60
        seconds += self.second

        return seconds

    def increment(self, duration):
        s = self.time_to_seconds()
        s = s + duration

        t2 = Time(second=s)
        self.second = t2.second
        self.minute = t2.minute
        self.hour = t2.hour


time1 = Time(hour=11, minute=59, second=30)
time2 = Time(second=12449)

print("str(time1)", str(time1))
print("str(time2)", str(time2))
print()
print("time1 < time2 with __lt__():", time1 < time2)
print("time1 <= time2 with __le__():", time1 <= time2)
print("time1 > time2 with __gt__():", time1 > time2)
print("time1 >= time2 with __ge__():", time1 >= time2)
print("time1 == time2 with __eq__():", time1 == time2)
print("time1 != time2 with __eq__():", time1 != time2)
print()
print("time1 < 6000 with __lt__() and type dispatch:", time1 < 6000)
print("time1 <= 6000 with __le__() and type dispatch:", time1 <= 6000)
print("time1 > 6000 with __gt__() and type dispatch:", time1 > 6000)
print("time1 >= 6000 with __ge__() and type dispatch:", time1 >= 6000)
print("time1 == 6000 with __eq__() and type dispatch:", time1 == 6000)
print("time1 != 6000 with __eq__() and type dispatch:", time1 != 6000)
print()
print("6000 < time1 with __rlt__() and type dispatch:", 6000 < time1)
print("6000 <= time1 with __rle__() and type dispatch:", 6000 <= time1)
print("6000 > time1 with __rgt__() and type dispatch:", 6000 > time1)
print("6000 >= time1 with __rge__() and type dispatch:", 6000 >= time1)
print("6000 == time1 with __req__() and type dispatch:", 6000 == time1)
print("6000 != time1 with __req__() and type dispatch:", 6000 != time1)
print()
print("time1 + time2 with __add__():", time1 + time2)
print("time1 + 30 with __add__() and type dispatch:", time1 + 30)
print("30 + time1 with __radd__() and type dispatch:", 30 + time1)
print()
print("time1 - time2 with __sub__():", time1 - time2)
print("time1 - 30 with __sub__() and type dispatch:", time1 - 30)
print("30 - time1 with __rsub__() and type dispatch:", 30 - time1)

print()
time1.increment(300)
print("time1 after incrementing by 300: ", time1)