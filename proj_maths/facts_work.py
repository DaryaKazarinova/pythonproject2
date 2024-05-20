'''functions for facts'''
import random
def get_facts_for_table():
    '''list of facts'''
    facts = []
    with open("./data/facts.csv", "r", encoding="utf-8") as f:
        cnt = 1
        num = random.randrange(2, 20)
        for line in f.readlines()[(num-1)::(num+1)]:
            country, fact, source = line.split(";")
            facts.append([country, fact])
            cnt += 1
        facts = facts[:1]
    return facts
