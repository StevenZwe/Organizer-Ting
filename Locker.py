class Locker:
    def __init__(self, adminno, date, location, size):
        self.__id = ''
        self.__adminno = adminno
        self.__date = date
        self.__location = location
        self.__size = size

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_adminno(self):
        return self.__adminno

    def set_adminno(self, adminno):
        self.__adminno = adminno

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size


#class Check:
#    def __init__(self, locationav, sizeav, lockerno):
#        self.__locationav = locationav
#        self.__sizeav = sizeav
#        self.__lockerno = lockerno
#
#    def get_locationav(self):
#        return self.__locationav
#
#    def set_locationav(self, locationav):
#        self.__locationav = locationav
#
#    def get_sizeav(self):
#        return self.__sizeav
#
#    def set_sizeav(self, sizeav):
#        self.__sizeav = sizeav
#
#    def get_lockerno(self):
#        return self.__lockerno
#
#    def set_lockerno(self, lockerno):
#        self.__lockerno = lockerno
#
#def availability():
#    lockers = ['A01', 'A02', 'A03', 'L01', 'L02', 'L03', 'S01', 'S02', 'S03']
#    locker1 = ['A01']
#    locker2 = ['A02']
#    locker3 = ['A03']
#    locker4 = ['L01']
#    locker5 = ['L02']
#    locker6 = ['L03']
#    locker7 = ['S01']
#    locker8 = ['S02']
#    locker9 = ['S03']
#
#    location = ['blka', 'blkl', 'blks']
#    size = ['small', 'medium', 'big']
#
#    blka = ['A01', 'A02', 'A03']
#    blkl = ['L01', 'L02', 'L03']
#    blks = ['S01', 'S02', 'S03']
#
#
#
#
#
#class LockerRental:
#    locker = []
#    date = []