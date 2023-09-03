import matplotlib.pyplot as plt
import networkx as nx
from pgmpy.models import MarkovModel

model = MarkovModel([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])

# 使用`networkx`创建图形对象
graph = nx.Graph()
graph.add_edges_from(model.edges())

# 设置可视化的布局
pos = nx.spring_layout(graph, seed=42)

# 可视化马尔科夫网络
nx.draw(graph, pos, with_labels=True, node_size=2000, font_weight='bold', node_color='skyblue', edgecolors='black',
        alpha=0.8)
plt.savefig("logs/mark.png")
plt.show()
