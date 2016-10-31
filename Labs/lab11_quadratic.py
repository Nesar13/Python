''' "I pledge my honor that I have abided by the Stevens Honor System." 


@author: Nesar Ahmed
Created on Apr 15, 2016
'''
class QuadraticEquation (object): #capitalize the name of the class
    def __init__(self, a,b,c): #constructor is init. For initializing field and any time writing a method in a class, write self
        
        a=float(a)
        b=float(b)
        c=float(c)
        
        self.__a=a                  #private means it is only available inside the class,  underscore is for private, __first is field
        self.__b=b
        self.__c=c
        
        if self.__a==0:
            raise ValueError('Coefficient \'a\' cannot be 0 in a quadratic equation.')
        
    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b
    
    @property
    def c(self):
        return self.__c
    
    def discriminant(self):
        '''computes the b^2-4ac'''
        return self.__b**2 - (4*self.__a *self.__c)
    
    def root1(self):
        '''computes the addition of the quadratic'''
        if self.discriminant() < 0: 
            return None
        return (-self.__b + self.discriminant()**(1/2)) / (2*self.__a)
    
    def root2(self):
        if self.discriminant() < 0: 
            return None
        return (-self.__b - self.discriminant()**(1/2)) / (2*self.__a)
    
#     def __str__(self):
#         signa=1
#         signb=1
#         signc=1
#         if self.__a < 0:
#             signa= -1
#             return signa
#         if self.__b < 0:
#             signb=-1
#             return signb
#         if self.__c < 0: 
#             signc=-1
#             return signc
#         if self.__b==0:
#             return str(str(signa*self.__a)+ '+ x^2 + ' + str(signc*self.__c)+ ' = 0')
#         if self.__c==0:
#             return str(str(signa*self.__a) + '+ x^2 + ' + str(signb*self.__b)+ 'x'+ ' = 0')
#         if self.__a==1:
#             return str('x^2 + ' + str(signb*self.__b)+ 'x + '+ str(signc*self.__c)+ ' = 0')
#         if self.__b==1:
#             return str(str(signa*self.__a)+ 'x^2 +' + 'x + ' + str(signc*self.__c)+ ' = 0')
#         if self.__c==0 and self.__b==0 and self.__a==1: 
#             return 'x^2 = 0'
#         return str(str(signa*self.__a)+ 'x^2 + ' + str(signb*self.__b)+ 'x + '+ str(signc*self.__c) + ' = 0')
        
    def __str__(self):
            s = ""
            if self.__a:
                if self.__a == 1:
                    s += 'x^2'
                elif self.__a == -1:
                    s += "-x^2"
                else:
                    s += str(self.__a) + 'x^2'
            if self.__b:
                if self.__b > 0:
                    s += " + "
                else:
                    s += " - "
                if abs(self.__b) == 1:
                    s += 'x'
                else:
                    s += str(abs(self.__b)) + 'x'
            if self.c:
                if self.__c > 0:
                    s += " + "
                else:
                    s += " - "
                s += str(abs(self.__c))
            return s + ' = 0'
    
if __name__=='__main__':
    f = QuadraticEquation(1,-1,5)
    print (f)
    
        
        