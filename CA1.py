
# Initialize memory
memory = {
    100: 12,
    104: 8
}

# Initialize registers
R1 = 0
R2 = 0
R3 = 0

print("Initial Memory:", memory)

# Instruction 1: LOAD R1, 100
print("\nExecuting: LOAD R1, 100")
R1 = memory[100]
print("R1 =", R1)

# Instruction 2: LOAD R2, 104
print("\nExecuting: LOAD R2, 104")
R2 = memory[104]
print("R2 =", R2)

# Instruction 3: ADD R3, R1, R2
print("\nExecuting: ADD R3, R1, R2")
R3 = R1 + R2
print("R3 =", R3)

# Instruction 4: STORE R3, 108
print("\nExecuting: STORE R3, 108")
memory[108] = R3
print("Memory[108] =", memory[108])

# Display final results
print("\nFinal Register Contents:")
print("R1 =", R1)
print("R2 =", R2)
print("R3 =", R3)

print("\nFinal Memory Contents:")
print(memory)
