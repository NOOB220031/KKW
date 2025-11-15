# Use Apriori algorithm on groceries dataset to find which items are brought together. 
# Use minimum support =0.25

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Sample data (you can replace it with an actual grocery dataset)
# Each row is a transaction, and each column is an item (True means the item was bought, False means it was not)
data = {'milk': [1, 0, 1, 1, 0],
        'bread': [1, 1, 0, 1, 1],
        'butter': [0, 1, 1, 1, 0],
        'cheese': [1, 0, 0, 1, 1],
        'apples': [0, 1, 1, 0, 1]}

df = pd.DataFrame(data)

# Convert the dataset to boolean (True/False)
#Convert to Boolean:
#I used df = df.astype(bool) to convert the DataFrame to boolean(True for 1 and False for 0).
df = df.astype(bool)

# Minimum support
min_support = 0.25

# Apply the apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)

# Display frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)

# Generate the association rules based on lift
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Display the association rules
print("\nAssociation Rules:")
print(rules)
