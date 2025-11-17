import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

data = {'milk': [1, 0, 1, 1, 0],
        'bread': [1, 1, 0, 1, 1],
        'butter': [0, 1, 1, 1, 0],
        'cheese': [1, 0, 0, 1, 1],
        'apples': [0, 1, 1, 0, 1]}

df = pd.DataFrame(data)

df = df.astype(bool)

min_support = 0.25

frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)

print("Frequent Itemsets:")
print(frequent_itemsets)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

print("\nAssociation Rules:")
print(rules)
