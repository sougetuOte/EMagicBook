# coding: utf-8

# 画面遷移フローの図
import matplotlib.pyplot as plt
import matplotlib
import networkx as nx
import matplotlib.font_manager as fm
import os

# フォントのパスを指定
font_path = 'C:/Windows/Fonts/msgothic.ttc'  # 例: 'C:/Windows/Fonts/meiryo.ttc'
# フォントプロパティを作成
font_prop = fm.FontProperties(fname=font_path)
# matplotlibのデフォルトフォントを変更
plt.rcParams['font.family'] = font_prop.get_name()

# 画面遷移を示す有向グラフの作成
G = nx.DiGraph()

# ノードの追加 (画面)
screens = ["マスコット", "日記起動", "日記編集", "チャット", "ToDo編集"]
G.add_nodes_from(screens)

# エッジの追加 (遷移)
transitions = [("マスコット", "日記起動"), ("マスコット", "チャット"),
               ("日記起動", "日記編集"), ("日記編集", "ToDo編集"),
               ("ToDo編集", "日記編集"), ("日記編集", "日記起動"),
               ("日記起動", "マスコット"), ("チャット", "マスコット")]
G.add_edges_from(transitions)

# 有向グラフの描画
pos = nx.spring_layout(G, seed=42)  # レイアウトの設定
plt.figure(figsize=(10, 6))  # グラフのサイズを設定

# ノードとエッジの描画
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color="skyblue")
nx.draw_networkx_edges(G, pos, edge_color="gray")
nx.draw_networkx_labels(G, pos, font_size=15)

# グラフの表示
plt.title("画面遷移図", fontsize=20)
plt.axis("off")  # 軸の非表示
plt.tight_layout()
plt.show()

for label, (x, y) in pos.items():
    plt.text(x, y, label, fontsize=12, fontproperties=font_prop,
             horizontalalignment='center', verticalalignment='center')