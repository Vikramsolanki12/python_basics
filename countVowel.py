text="The quick brown fox jumps over the lazy dog"
count=0
for i in text:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        k=print(i,end=" ")
        count += 1
print(count)