def multiply(a, b):
    if a <= 0 or b <= 0:
        return "error"
    
    if a == 1:
        return b
    if b == 1:
        return a
    
    result = 0

    while b != 0:
        if b & 1: # if b is odd
            result += a
        a << 1 # left-shift 'a', this multiplies a by 2
        b >> 1 # right shift 'b'
        
print(multiply(2,3))