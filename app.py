import tkinter as tk

# Main Window
root = tk.Tk()
root.title("BhavPath - Python")
root.geometry("900x600")
root.configure(bg="#f0f2f5")

# FIX 1: Blue bg meeda White text - Clear ga kanipistadi
top_bar = tk.Label(
    root,
    text="BhavPath | Rise | 81 percent | 820 XP | Python",
    bg="#1d4ed8",
    fg="#ffffff",  # WHITE TEXT FIXED
    font=("Arial", 12, "bold"),
    padx=20, pady=15, anchor="w"
)
top_bar.pack(fill="x", padx=20, pady=(20,10))

# Black Line
line = tk.Frame(root, bg="black", height=5)
line.pack(fill="x", padx=20, pady=10)

# Top Buttons Frame
top_btn_frame = tk.Frame(root, bg="#f0f2f5")
top_btn_frame.pack(fill="x", padx=20, pady=10)

# FIX 2: Blue button + White text visible
btn1 = tk.Button(
    top_btn_frame,
    text="Back Change percent",
    bg="#1d4ed8",
    fg="#ffffff",  # WHITE TEXT FIXED
    activebackground="#1e40af",
    activeforeground="white",
    relief="flat", padx=20, pady=10, font=("Arial", 10)
)
btn1.pack(side="left", fill="x", expand=True, padx=(0,10))

btn2 = tk.Button(
    top_btn_frame,
    text="Back to All Topics List Malli",
    bg="#1d4ed8",
    fg="#ffffff",  # WHITE TEXT FIXED
    activebackground="#1e40af",
    activeforeground="white",
    relief="flat", padx=20, pady=10, font=("Arial", 10)
)
btn2.pack(side="left", fill="x", expand=True)

# Main Content Frame
main_frame = tk.Frame(root, bg="#f0f2f5")
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Left Panel
left = tk.Frame(main_frame, bg="#f0f2f5", width=200)
left.pack(side="left", fill="y", padx=(0,10))

# FIX 3: White bg meeda Black text - Clear ga kanipistadi
info_card = tk.Label(
    left,
    text="List Page varake -\nIkkada matrame\nOpen buttons",
    bg="#ffffff",
    fg="#000000",  # BLACK TEXT FIXED - White lo white kadu
    font=("Arial", 10, "bold"),
    justify="left",
    padx=15, pady=15,
    wraplength=180, relief="solid", bd=1
)
info_card.pack(fill="x", pady=(0,15))

python_frame = tk.Frame(left, bg="white", relief="solid", bd=1)
python_frame.pack(fill="x")

python_header = tk.Frame(python_frame, bg="#2563eb")
python_header.pack(fill="x")

tk.Label(python_header, text="Python SELECTED", bg="#2563eb", fg="white", font=("Arial", 10, "bold"), anchor="w").pack(fill="x", padx=15, pady=(15,2))
tk.Label(python_header, text="Easy plus Data Science", bg="#2563eb", fg="#dbeafe", font=("Arial", 9), anchor="w").pack(fill="x", padx=15, pady=(0,10))

open_py = tk.Button(python_frame, text="Open Python", bg="#2563eb", fg="white", activebackground="#1d4ed8", relief="flat", pady=10)
open_py.pack(fill="x")

# Right Panel
right = tk.Frame(main_frame, bg="#f0f2f5")
right.pack(side="left", fill="both", expand=True)

topics = ["1. Introduction", "2. Variables", "3. Operators", "4. Loops", "5. Identifiers"]

for t in topics:
    btn = tk.Button(
        right,
        text=f"• {t}  →  Open Detail",
        bg="#2563eb",
        fg="#ffffff", # WHITE TEXT FIXED
        activebackground="#1d4ed8",
        activeforeground="white",
        relief="flat",
        font=("Arial", 10),
        pady=14
    )
    btn.pack(fill="x", pady=5)

root.mainloop()
