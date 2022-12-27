import os
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if (" 2.md" in os.path.join(root, name)):
            os.remove(os.path.join(root, name));