from arm.utils.utilFunc import twosComplement

#100000000000000000000000000000000
#01234567890123456789012345678901
#00000000001111111111222222222223

x = '1101'
print twosComplement(x,4)

#fffffffdL

y = str(hex(int('11111111111111111111111111111101',2)))
if(y[-1] == 'L'):
    y = y[0:len(y)-1]
print y

n=4
print 2**n