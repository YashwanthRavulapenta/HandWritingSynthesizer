import os
import cv2
import numpy as np
import random
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import Conv2D, GlobalAveragePooling2D, Dense, Dropout, Input
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Constants
DATASET_PATH = r"C:\Users\Yashwanth\OneDrive\Desktop\practice\handwriting_dataset"
IMG_SIZE = (64, 64)
A4_SIZE = (2480, 3508)
LINE_SPACING = 80
WORD_SPACING = 65
PARAGRAPH_SPACING = 150
START_X, START_Y = 100, 100

def load_data():
    images, labels = [], []
    class_map = {}
    categories = ['lowercase', 'uppercase', 'numbers']
    label_index = 0
    
    for category in categories:
        category_path = os.path.join(DATASET_PATH, category)
        if not os.path.exists(category_path):
            continue
        
        for char in sorted(os.listdir(category_path)):
            char_path = os.path.join(category_path, char)
            if not os.path.isdir(char_path):  
                continue
            class_map[char] = label_index
            for img_name in os.listdir(char_path):
                img_path = os.path.join(char_path, img_name)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    img = cv2.resize(img, IMG_SIZE)
                    images.append(img)
                    labels.append(label_index)
            label_index += 1

    images = np.array(images).reshape(-1, 64, 64, 1) / 255.0
    labels = np.array(labels)
    return images, labels, class_map

# Load dataset
images, labels, class_map = load_data()

def generate_handwritten_text(input_text):
    output_img = Image.new('RGB', A4_SIZE, color='white')
    x, y = START_X, START_Y
    max_width = A4_SIZE[0] - 200  
    paragraphs = input_text.split('\n\n')  # Split by paragraph
    
    for paragraph in paragraphs:
        lines = paragraph.split('\n')
        for line in lines:
            words = line.split()
            for word in words:
                word_width = sum(IMG_SIZE[0] for _ in word)
                if x + word_width > max_width:
                    x = START_X
                    y += IMG_SIZE[1] + LINE_SPACING  

                for char in word:
                    category = ('lowercase' if char.islower() else
                                'uppercase' if char.isupper() else
                                'numbers' if char.isdigit() else None)
                    if category and char in class_map:
                        char_idx = class_map[char]
                        char_samples = np.array([img for i, img in enumerate(images) if labels[i] == char_idx])
                        if len(char_samples) > 0:
                            sample_img = char_samples[random.randint(0, len(char_samples) - 1)] * 255
                            char_img = Image.fromarray(sample_img.squeeze()).convert("RGB")
                            output_img.paste(char_img, (x, y))
                            x += char_img.width  
                x += WORD_SPACING  
            
            y += LINE_SPACING  
            x = START_X  
        
        y += PARAGRAPH_SPACING  # Extra spacing for new paragraph
        x = START_X  
    
    output_img_path = "generated_handwriting.png"
    output_img.save(output_img_path)
    return output_img_path

class HandwritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Handwriting Generator")
        self.root.geometry("700x550")
        self.root.configure(bg="#f0f0f0")
        
        self.label = tk.Label(root, text="Enter text or upload a file:", font=("Arial", 14), bg="#f0f0f0")
        self.label.pack(pady=5)
        
        self.text_entry = tk.Text(root, font=("Arial", 14), height=8, width=50)
        self.text_entry.pack(pady=5)
        
        self.upload_btn = ttk.Button(root, text="Upload File", command=self.upload_file)
        self.upload_btn.pack(pady=5)
        
        self.frame_buttons = tk.Frame(root, bg="#f0f0f0")
        self.frame_buttons.pack(pady=10)
        
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=10, relief="raised")
        
        self.generate_btn = ttk.Button(self.frame_buttons, text="📝 Generate", command=self.generate, style="TButton")
        self.generate_btn.grid(row=0, column=0, padx=10)
        
        self.save_btn = ttk.Button(self.frame_buttons, text="💾 Save & View", command=self.save_and_view, style="TButton")
        self.save_btn.grid(row=0, column=1, padx=10)
        
        self.clear_btn = ttk.Button(self.frame_buttons, text="🗑️ Clear", command=self.clear_text, style="TButton")
        self.clear_btn.grid(row=0, column=2, padx=10)
        
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white", relief="sunken")
        self.canvas.pack(pady=10)
        
        self.generated_image_path = None
    
    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_entry.delete("1.0", tk.END)
                self.text_entry.insert("1.0", content)
    
    def generate(self):
        input_text = self.text_entry.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("Warning", "Please enter some text or upload a file!")
            return
        
        self.generated_image_path = generate_handwritten_text(input_text)
        self.display_image()
        messagebox.showinfo("Success", "Handwritten image generated successfully!")
    
    def display_image(self):
        if self.generated_image_path:
            img = Image.open(self.generated_image_path)
            img.thumbnail((300, 300))
            self.tk_img = ImageTk.PhotoImage(img)
            self.canvas.create_image(150, 150, image=self.tk_img, anchor=tk.CENTER)
    
    def save_and_view(self):
        if self.generated_image_path:
            os.startfile(self.generated_image_path)
        else:
            messagebox.showwarning("Warning", "No image generated yet!")
    
    def clear_text(self):
        self.text_entry.delete("1.0", tk.END)
        self.canvas.delete("all")
        self.generated_image_path = None

if __name__ == "__main__":
    root = tk.Tk()
    app = HandwritingApp(root)
    root.mainloop()
