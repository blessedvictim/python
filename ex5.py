a = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty ','thirty ','fourty ','fifty ','sixty ','seventy ','eighty ','ninty ']
def ex11(number):
  
    if number>=1 and number<=1000:
        if number<=20:
            if number%10==0: return a[number]
            else: return a[number]
        elif number<100:
            b=number-20
            r=b%10
            b//=10
            return a[20+b]+a[r]
        elif number<1000:
            if number%100==0:
                b=number//100
                return a[b]+' hundred'
            else:
                r=number%100
                b=number//100
                if r<=20:
                    return a[b]+' hundred'+' '+a[r]
                else:
                    r=r-20
                    d=r//10
                    r%=10
                    return a[b]+' hundred'+' '+a[20+d]+a[r]
        elif number==1000:
            return 'one thousand'
        else:
            return -1

print(ex11(112))

def ex12():
  pass
