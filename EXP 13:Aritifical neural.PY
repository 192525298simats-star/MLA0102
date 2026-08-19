# Simple Artificial Neural Network

inputs = [1, 0]
weights = [0.6, 0.4]
bias = -0.5

# Calculate weighted sum
s = 0
for i in range(len(inputs)):
    s += inputs[i] * weights[i]

s += bias

# Step activation function
if s >= 0:
    output = 1
else:
    output = 0

print("Output:", output)
