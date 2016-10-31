'''
Created on 4/20/16
@author:   Nesar Ahmed
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
         as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
         whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day

    def tomorrow(self):
        '''takes day as self, and makes it the next day'''
        if self.day == DAYS_IN_MONTH[self.month]:
            if self.month == 12:
                self.day = 1
                self.month = 1
                self.year = self.year + 1
            elif self.isLeapYear() and self.month == 2:
                self.day = 29
            else: 
                self.day = 1
                self.month = self.month + 1
        elif self.day == 29 and self.month == 2:
            self.day = 1
            self.month = 3
        else:
            self.day = self.day + 1  
            
    def yesterday(self):
        '''takes day in as self, and makes it the day before'''
        if self.day == 1:
            if self.month == 1:
                self.month = 12
                self.day = 31
                self.year = self.year - 1
            elif self.isLeapYear() and self.month == 3:
                self.day = 29
                self.month = 2
            else:
                self.month = self.month - 1
                self.day = DAYS_IN_MONTH[self.month]
        else:
            self.day = self.day - 1
            
    def addNDays(self, N):
        '''takes day in as self, and makes it n days after given value'''
        print(self)
        while N > 0:
            self.tomorrow()
            print(self)
            N -= 1
            
    def subNDays(self, N):
        '''takes day in as self, and makes it n days before give value'''
        print(self)
        while N > 0:
            self.yesterday()
            print(self)
            N -= 1

    def isBefore(self, d2):
        '''checks to see if self is before d2'''
        if self.year < d2.year:
            return True
        elif self.year > d2.year:
            return False
        elif self.month < d2.month:
            return True
        elif self.month > d2.month:
            return False
        elif self.day < d2.day:
            return True
        else:
            return False
        
    def isAfter(self, d2):
        '''checks to see if self is after d2'''
        if self.equals(d2):
            return False
        return not self.isBefore(d2)
    
    def diff(self, d2):
        '''Returns number of days betwwn self and d2'''
        if self.equals(d2):
            return 0
        c1 = self.copy()
        c2 = d2.copy()
        count = 0
        while c1.isBefore(c2):
            c1.tomorrow()
            count -= 1
        while c1.isAfter(c2):
            c1.yesterday()
            count += 1
        return count

    def dow(self):
        '''tells what day of week self is'''
        d = Date(11, 9 ,2011)
        c = self.diff(d)
        if c % 7 == 0:
            return 'Wednesday'
        if c % 7 == 1:
            return 'Thursday'
        if c % 7 == 2:
            return 'Friday'
        if c % 7 == 3:
            return 'Saturday'
        if c % 7 == 4:
            return 'Sunday'
        if c % 7 == 5:
            return 'Monday'
        if c % 7 == 6:
            return 'Tuesday'
        
if __name__ == '__main__':
    d=Date(11,9,2011)
    print (d)
    d2= Date(11,9,2011)
    print (d==d2)
    print (id(d)) # id returns memory address 
    print (d2.isLeapYear()) 
    
