class Number:
    def __init__(self,num):
        self.num=num
    def get_nuber(self):
        return self.num
    def is_even(self):
        return self.num%2==0
    def is_odd(self):
        return self.num%2!=0
    def is_prime(self):
        x=self.num
        for i in range(2,x//2+2):
            if x%i!=0:
                return False
        return True
    def get_divisors(self):
        a=[]
        for i in range(1,self.num+1):
            if self.num%i==0:
                a.append(i):
        return a 
    def get_lenth(self):
        return len(str(self.num))
    def get_sum(self):
        x=str(self.num)
        s=0
        for i in range(len(x)):
            s+=int(x[i])
        return s 
    def get_product(self):
        x=self.num
        s=1
        while x!=0:
            s*=x%10
            x//=10
        return s 
    def get_reverse(self):
        return int(str(self.num)[::-1])
    def get_digits(self):
        a=[]
        x=self.num
        while x!=0:
            a.append(x%10)
            x//=10
        return a 
    def get_max(self):
        a=[]
        x=self.num
        while x!=0:
            a.append(x%10)
            x//=10
        return max(a)
    def get_min(self):
        a=[]
        x=self.num
        while x!=0:
            a.append(x%10)
            x//=10
        return min(a)
    def get_everage(self):
        x=self.num
        a=0
        while x!=0:
            a+=x%10
            x//=10
        return a/len(str(x))
    def get_median(self):
        x=len(str(self.num))
        a=str(self.num)
        if x%2==0:
            return f'{int(a[x//2])} and {int(a[x//2-1])}'
        return int(a[x//2])
    def get_mode():
        m=0
        a=list(str(self.num))
        for i in a:
            if a.count(i)>m:
                k=i 
                
                m=a.count(i)
        return k
        

    def get_range(self):
        return list(range(1,self.num+1))
