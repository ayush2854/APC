para = """ Hello friends. """
count = 0
for i in para:
    count += 1
print(count)

char_count = 0
for i in para:
    if(i=='a'):
        char_count +=1
print(char_count)

vowel_count = 0
for i in para:
    if(i=='a' or i=='e' or i=='i' or i=='o'or i=='u'):
        vowel_count +=1
print(vowel_count)