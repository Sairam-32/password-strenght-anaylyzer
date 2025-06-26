import tkinter as tk
from analyzer import analyze_password
from wordlist_generator import generate_wordlist, export_wordlist

def evaluate():
    pwd = entry_pwd.get()
    result = analyze_password(pwd)
    lbl_result['text'] = f"Score: {result['score']}\nCrack Time: {result['crack_time']}"

def generate():
    keys = entry_keywords.get().split(',')
    words = generate_wordlist(keys)
    export_wordlist(words)
    lbl_export['text'] = f"Exported {len(words)} words!"

root = tk.Tk()
root.title("Password Tool")

tk.Label(root, text="Password:").pack()
entry_pwd = tk.Entry(root, show='*')
entry_pwd.pack()

tk.Button(root, text="Analyze", command=evaluate).pack()
lbl_result = tk.Label(root, text="")
lbl_result.pack()

tk.Label(root, text="Keywords (comma separated):").pack()
entry_keywords = tk.Entry(root)
entry_keywords.pack()

tk.Button(root, text="Generate Wordlist", command=generate).pack()
lbl_export = tk.Label(root, text="")
lbl_export.pack()

root.mainloop()