import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Hide the axes
ax.axis('off')

# Year, Month, Date input
rect_y_m_d = plt.Rectangle((50, 450), 700, 100, linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(rect_y_m_d)
plt.text(60, 470, "Year-Month-Date Input", fontsize=12, color='r')

# Calendar
rect_calendar = plt.Rectangle((150, 150), 500, 250, linewidth=1, edgecolor='g', facecolor='none')
ax.add_patch(rect_calendar)
plt.text(300, 250, "Calendar", fontsize=12, horizontalalignment='center', color='g')

# New Diary Button
rect_new_diary = plt.Rectangle((300, 50), 200, 50, linewidth=1, edgecolor='b', facecolor='none')
ax.add_patch(rect_new_diary)
plt.text(350, 65, "New Diary", fontsize=12, horizontalalignment='center', color='b')

# Close Button
rect_close = plt.Rectangle((720, 530), 30, 30, linewidth=1, edgecolor='purple', facecolor='none')
ax.add_patch(rect_close)
plt.text(735, 545, "X", fontsize=12, horizontalalignment='center', verticalalignment='center', color='purple')

# Show the plot
plt.imshow(np.ones((600, 800, 3)))

# Save the plot
plt.savefig("diary_startup_screen_layout_eng.png")
plt.show()
