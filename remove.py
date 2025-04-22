import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import filedialog, messagebox
import os
from rembg import remove


ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")  

class BackgroundRemoverApp(TkinterDnD.Tk):  
    def __init__(self):
        super().__init__()
        self.title("CleanPic by SoyKhaler")
        self.geometry("400x300")
        self.configure(bg="#2b2b2b")  

 
        self.label = ctk.CTkLabel(self, text="CleanPic ", text_color="white")
        self.label.pack(pady=20)


        self.drop_area = ctk.CTkLabel(self, text="Drag and drop an image here", 
                                      width=300, height=100, 
                                      fg_color="#3b3b3b", 
                                      corner_radius=10, 
                                      text_color="white")
        self.drop_area.pack(pady=10)
        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind('<<Drop>>', self.on_drop)

        self.select_button = ctk.CTkButton(self, text="Select an image", command=self.select_image)
        self.select_button.pack(pady=20)

    def on_drop(self, event):
        file_path = event.data
        if file_path.endswith(('.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG', '.jfif', '.JFIF')):
            self.process_image(file_path)
        else:
            messagebox.showwarning("Warning", "Select a image with a valid extension.")

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.process_image(file_path)
        else:
            messagebox.showwarning("Warning", "No image was selected.")

    def process_image(self, input_path):
        try:
            output_path = os.path.splitext(input_path)[0] + "_no_background.png"
            
            with open(input_path, 'rb') as inp_file:
                input_data = inp_file.read()
                output_data = remove(input_data)
                
                with open(output_path, 'wb') as out_file:
                    out_file.write(output_data)

            messagebox.showinfo("Éxito", f"Saved image to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error Processing Image: {e}")

if __name__ == "__main__":
    app = BackgroundRemoverApp()
    app.mainloop()
