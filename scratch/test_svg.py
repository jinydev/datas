import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

sns.countplot(data=df, x='sex', hue='survived', ax=axes[0], palette=['#e74c3c', '#2ecc71'])
sns.barplot(data=df, x='pclass', y='survived', ax=axes[1], palette='Blues_d')
plt.tight_layout()

plt.savefig('test_plot.svg', format='svg', bbox_inches='tight')
plt.clf()
