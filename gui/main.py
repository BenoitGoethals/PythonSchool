import tkinter as tk



def main():
    def click_buttom():
        label.config(text=input.get())

    root = tk.Tk()
    root.title("Hello World")
    root.minsize(500,300)
    label = tk.Label(root, text="Hello World")
    label.pack()
    input = tk.Entry(root)
    input.pack()
    button = tk.Button(root, text="Click Me",command=click_buttom)
    button.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
