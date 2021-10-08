from nltk.corpus import wordnet
import tkinter as tk
window = tk.Tk()
window.geometry("500x500")

def work():

	syns = wordnet.synsets(ent_input.get())

	i = syns[0].lemmas() [0].name()
	j = syns[0].definition()
	k = syns[0].examples()

	lbl_value["text"] = f"SYNONYM: {i} || DEFINITION: {j} || EXAMPLES: {k}"

ent_input = tk.Entry(master=window, relief=tk.SUNKEN)
ent_input.pack(side=tk.TOP)

btn_go = tk.Button(master=window, relief=tk.RAISED, text="Go", command=work)
btn_go.pack(side=tk.TOP)

lbl_value = tk.Label(master=window, height=100, width=100, wraplength=150, text="Enter a word and I'll tell you all about it")
lbl_value.pack(side=tk.BOTTOM)

window.mainloop()