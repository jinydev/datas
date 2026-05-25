import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

env_globals = {
    'pd': pd,
    'sns': sns,
    'plt': plt,
}

code1 = """
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
"""

code2 = """
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
sns.countplot(data=df, x='sex', hue='survived', ax=axes[0], palette=['#e74c3c', '#2ecc71'])
sns.barplot(data=df, x='pclass', y='survived', ax=axes[1], palette='Blues_d')
plt.tight_layout()
plt.show()
"""

def mock_show(*args, **kwargs):
    if plt.get_fignums():
        plt.savefig('test_exec.svg', format='svg', bbox_inches='tight')
        plt.clf()

plt.show = mock_show

exec(code1, env_globals)
exec(code2, env_globals)

