def circuit_output(A, B, C):
    AND1_out = A and B
  
    AND2_out = C and AND1_out
  
    OR_out = AND2_out or AND1_out
  
    NOT_out = not OR_out

    return NOT_out

# Example usage with input values
A = 1
B = 0
C = 1

output = circuit_output(A, B, C)

print("Output:", output)
