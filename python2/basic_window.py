from tkinter import *
def get_selection():
    selection = lb_of_stones.curselection()  # function takes current selection from listbox
    print(lb_of_stones.get(selection))



root = Tk()
root.title("Gibby the enemy of humanity")
root.configure(background="blue")
root.minsize(200, 200)
root.maxsize(1000, 1000)
root.geometry("500x500+50+20")
text = Label(root, width=67 , text=" When I'm done, half of humanity will still exist. Perfectly balanced, as all things should be.")
text.pack()

var1 = "kaas" 
text2 = Label(root, text=var1)
text2.pack()


text3 = Label(root, text="What was the first infinity stone that thanos had", wraplength=200)
text3.place(x=100, y=400)

lb_of_stones = Listbox(root, selectmode=BROWSE, width = 32)  # width is equal to number of characters
lb_of_stones.place(x=400, y=800 ,)


stones = ["Power stone", "Reality stone", "Mind stone", "Time stone", "Soul stone" , "Space stone"]
for  c  in  stones:
    lb_of_stones.insert(END, c)

lb_of_stones.bind("&lt;&lt;ListboxSelect&gt;&gt;", lambda event:  get_selection())

end_button = Button(root, text="End", command=quit)
end_button.place(x=300, y=400)

root.mainloop()

