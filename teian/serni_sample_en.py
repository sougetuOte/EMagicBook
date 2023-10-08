# Importing necessary libraries
import matplotlib.pyplot as plt
import networkx as nx

# Creating a new figure and setting the size
plt.figure(figsize=(12, 8))

# Creating a graph object
G = nx.DiGraph()

# Adding nodes (representing screens/pages in the application)
nodes = ['Mascot Icon', 'Chat Window', 'Diary Main Menu', 'New Entry', 'View Entry', 'Edit Entry', 'To-Do List', 'Edit To-Do']
G.add_nodes_from(nodes)

# Adding edges (representing transitions between screens/pages)
edges = [
    ('Mascot Icon', 'Chat Window'),
    ('Mascot Icon', 'Diary Main Menu'),
    ('Diary Main Menu', 'New Entry'),
    ('Diary Main Menu', 'View Entry'),
    ('View Entry', 'Edit Entry'),
    ('Edit Entry', 'To-Do List'),
    ('To-Do List', 'Edit To-Do'),
    ('Edit To-Do', 'To-Do List'),
    ('To-Do List', 'Edit Entry'),
    ('Edit Entry', 'View Entry'),
    ('View Entry', 'Diary Main Menu'),
    ('Diary Main Menu', 'Mascot Icon')
]
G.add_edges_from(edges)

# Plotting the graph
pos = nx.spring_layout(G)  # Setting the layout
nx.draw(G, pos, with_labels=True, node_size=5000, node_color="lightblue", font_size=10, font_weight="bold", alpha=0.8, width=2)

# Customizing and adding labels to the edges
edge_labels = {
    ('Mascot Icon', 'Chat Window'): 'Open Chat',
    ('Mascot Icon', 'Diary Main Menu'): 'Open Diary',
    ('Diary Main Menu', 'New Entry'): 'Create',
    ('Diary Main Menu', 'View Entry'): 'View',
    ('View Entry', 'Edit Entry'): 'Edit',
    ('Edit Entry', 'To-Do List'): 'View To-Do',
    ('To-Do List', 'Edit To-Do'): 'Edit',
    ('Edit To-Do', 'To-Do List'): 'Save',
    ('To-Do List', 'Edit Entry'): 'Back',
    ('Edit Entry', 'View Entry'): 'Save',
    ('View Entry', 'Diary Main Menu'): 'Back',
    ('Diary Main Menu', 'Mascot Icon'): 'Close Diary'
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green')

# Show the plot
plt.tight_layout()
plt.show()
