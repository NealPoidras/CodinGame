# Python code​​​​​​‌​​‌​​​​‌‌‌​‌‌​​‌​‌​‌‌‌​​ below
# Use print("messages...") to debug your solution.
import os

def locate_universe_formula():
    for root, dirs, files in os.walk("/tmp/documents"):
        if "universe-formula" in files:
            return os.path.join(root, "universe-formula")
    return None
