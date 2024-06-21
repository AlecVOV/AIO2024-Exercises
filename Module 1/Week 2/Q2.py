#trong python: string là 1 cái list chứa các kí tự
# Frequency dictionary: sử dụng cho ML trong NLP => sentiment analysis

#Character counting
name = "baby"
name = name.lower() #pre j đó của NLP
character_statistic = {}
for char in name:
    if char in character_statistic:
        character_statistic[char] += 1
    else:
        character_statistic[char] = 1

print(character_statistic)




