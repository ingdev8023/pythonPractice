words = ["Food", "Clothing", "Auto"]

# 1. Find the length of the longest word
max_len = max(len(w) for w in words)

# 2. Pad each word with spaces so they all have the same length
padded_words = [w.ljust(max_len) for w in words]


print(padded_words)
# 3. Combine them row by row using a space as a separator
lines = []
for i in range(max_len):
    row = " ".join(word[i] for word in padded_words)
    lines.append(row)

print(lines)
# 4. Join all rows with a newline
result = "\n".join(lines)

print(result)
