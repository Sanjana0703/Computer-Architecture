
# Initialize cache with 8 empty lines
cache = [-1] * 8

# Memory block access sequence
blocks = [3, 11, 3, 19, 11, 27, 3]

hits = 0
misses = 0

print("Block\tCache Line\tStatus\tCache Contents")

# Access each memory block
for block in blocks:

    # Calculate cache line
    line = block % 8

    # Check HIT or MISS
    if cache[line] == block:
        status = "HIT"
        hits += 1

    else:
        status = "MISS"
        misses += 1

        # Load block into cache
        cache[line] = block

    # Display cache contents
    print(block, "\t", line, "\t\t", status, "\t", cache)

# Calculate hit ratio and miss ratio
total = len(blocks)

hit_ratio = hits / total
miss_ratio = misses / total

# Display final results
print("\nTotal Accesses:", total)
print("Total Hits:", hits)
print("Total Misses:", misses)
print("Hit Ratio:", hit_ratio)
print("Miss Ratio:", miss_ratio)
