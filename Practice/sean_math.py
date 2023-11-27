class SeanMath:

    


    def multiply_bf(a,b):
        
        product = temp_b = b if b > 0 else -b;

        if a == 0 or b == 0:
            product = 0
        else:
            # ensure both a and b are positive
            temp_a = a if a > 0 else -a
            for i in range(temp_a - 1):
                product += temp_b
            if a < 0 or b < 0:
                product = -product

        return product

    def multiply(a, b):
          # Check for error conditions
          if a <= 0 or b <= 0:
              return "error"
          
          if a == 1:
              return b
          if b == 1:
              return a
          
          result = 0

        # Multiplication with bit shifting
          a_bin = '{0:08b}'.format(a)
          b_bin = '{0:08b}'.format(b)

          while b != 0:
            if b & 1:  # Bitwise & of the value of b with 1, if true then b is odd
                result += a # add a to the result
            a <<= 1  # Left-shift 'a', Multiplies a by 2 for each loop
            a_bin = '{0:08b}'.format(a)
            b >>= 1  # Right shifting the value contained in 'b' by 1. (remove the least significant bit)
            b_bin = '{0:08b}'.format(b)
            
          return result

# print(SeanMath.multiply_bf(2,3))
# print(SeanMath.multiply_bf(-2,3))
# print(SeanMath.multiply_bf(2,-3))
# print(SeanMath.multiply_bf(2,0))

print(SeanMath.multiply(7,3))
# print(SeanMath.multiply(7,3))
# print(SeanMath.multiply(-2,3))
# print(SeanMath.multiply(2,-3))
# print(SeanMath.multiply(2,0))