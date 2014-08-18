def twosComplement(x, N):
    return addSub('0' * N, x, '1', N, '0')


def addSub(op1, op2, sub_op, N, setFlags):
    c_in = '0'
    if(sub_op == '1'):
        op2 = negate(op2)
        c_in = '1'
    unsigned_sum = uInt(op1) + uInt(op2) + uInt(c_in)
    signed_sum = sInt(op1, N) + sInt(op2, N) + uInt(c_in)
    result = ("{0:b}".format(unsigned_sum))
    if(len(result) > N):
        result = result[1:N + 1]
    if(len(result) < N):
        result = result.zfill(N)    
    
    return result.zfill(N)

def uInt(x):
    return int(x, 2)

def sInt(x, N):
    result = int(x, 2)
    if(x[0] == '1'):
        result = result - 2 ** N
    return result


# return not(x)
def negate(x):
    to_ret = ''
    for c in x:
        if(c == '1'):
            to_ret = to_ret + '0'
        else:
            to_ret = to_ret + '1'
    return to_ret





def test(num,N):
    return str(bin(num))[2:].zfill(N)

def testa(num,N):
    return str(bin(num))[2:]

def test2(num,N):
    

def testa2(num,N):
    return "{0:b}".format(num)

num = -2
N = 8

print test(num,N)

print testa(num,N)

print test2(num,N)

print testa2(num,N)