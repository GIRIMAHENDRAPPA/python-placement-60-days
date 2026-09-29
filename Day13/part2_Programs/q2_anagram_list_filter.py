word_list=["listen","silent","enlist","world","lpu","upl"]

anagram_groups={}

for word in word_list:
    key="".join(sorted(word))
    if key not in anagram_groups:
        anagram_groups[key]=[]
    anagram_groups[key].append(word)
    
print(anagram_groups)

for group in anagram_groups.values():
    if len(group)>1:
        print(f"Anagram group:{group}")