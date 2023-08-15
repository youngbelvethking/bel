import tkinter as tk
from PIL import Image, ImageTk

class GameInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("League of Legends Item Viewer")
        self.attributes("-fullscreen", True)
        
        self.items = [
            {'name': 'dancadamorte', 'image': 'dancadamorte.png'},
            {'name': 'espadadorei', 'image': 'espadadorei.png'},
            {'name': 'lamina de guinsoo', 'image': 'laminadafuria.png'},
            {'name': 'limitedarazao', 'image': 'limitedarazao.png'},
            {'name': 'matacraquens', 'image': 'matacraquens.png'}
        ]
        self.current_item_index = 0
        
        self.label = tk.Label(self, text="belveth build", font=("Arial", 24))
        self.label.place(relx=0.5, rely=0.1, anchor="center")
        
        self.item_label = tk.Label(self, text=self.items[self.current_item_index]['name'], font=("Arial", 18))
        self.item_label.place(relx=0.5, rely=0.5, anchor="center")
        
        self.item_image_label = tk.Label(self)
        self.item_image_label.place(relx=0.5, rely=0.6, anchor="center")
        
        self.left_arrow = Image.open("seta.png")
        self.left_arrow = self.left_arrow.resize((50, 50))
        self.left_arrow = ImageTk.PhotoImage(self.left_arrow)
        self.left_button = tk.Button(self, image=self.left_arrow, command=self.previous_item)
        self.left_button.place(relx=0.3, rely=0.9, anchor="center")
        
        self.right_arrow = Image.open("setaa.png")
        self.right_arrow = self.right_arrow.resize((50, 50))
        self.right_arrow = ImageTk.PhotoImage(self.right_arrow)
        self.right_button = tk.Button(self, image=self.right_arrow, command=self.next_item)
        self.right_button.place(relx=0.7, rely=0.9, anchor="center")
        
        self.item_images = []
        for item in self.items:
            item_image = Image.open(item['image'])
            item_image = item_image.resize((150, 150))
            item_image = ImageTk.PhotoImage(item_image)
            self.item_images.append(item_image)
        
    def next_item(self):
        self.current_item_index = (self.current_item_index + 1) % len(self.items)
        self.item_label.config(text=self.items[self.current_item_index]['name'])
        self.show_item_image()
    
    def previous_item(self):
        self.current_item_index = (self.current_item_index - 1) % len(self.items)
        self.item_label.config(text=self.items[self.current_item_index]['name'])
        self.show_item_image()
        
    def show_item_image(self):
        item_image = self.item_images[self.current_item_index]
        self.item_image_label.config(image=item_image)
        self.item_image_label.image = item_image
    
if __name__ == '__main__':
    interface = GameInterface()
    interface.mainloop()