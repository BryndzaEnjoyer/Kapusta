import tkinter as tk
import random
memory = []
root = tk.Tk()
root.title("U01_Kapusta")
root.geometry("400x500") 
def enter():
    memory.append(INPUT.get("1.0", "end-1c"))
    print(memory)

def mix():
    global pos
    for i in range(1,len(memory)-1):
        memory[i+1], memory[i] = memory[i], memory[i+1]
        memory[0], memory[i-1] = memory[i-1], memory[0]
    print(memory)
    pos = random.randint(0,len(memory)-1)
    label2.config(text=f"What word is on the position: {pos}")

def guess():
    if memory[pos]==GUESS.get("1.0", "end-1c"):
        label2.config(text="Correct")
    else:  
        label2.config(text='Incorect')
 

label = tk.Label(root, text="Enter data", font=("Arial", 16))
label.pack(pady=20)

INPUT = tk.Text(root, height=2, width=30)
INPUT.pack()

button = tk.Button(root, text="Enter",command=enter)
button.pack(pady=10)

button2 = tk.Button(root, text="shuffle",command=mix)
button2.pack(pady=10)

GUESS = tk.Text(root, height=2, width=30)
GUESS.pack()

button3 = tk.Button(root, text="guess",command=guess)
button3.pack(pady=10)
label2 = tk.Label(root, text="", font=("Arial", 16))
label2.pack(pady=20)

root.mainloop()