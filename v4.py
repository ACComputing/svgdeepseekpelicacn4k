import tkinter as tk

class PelicanBikeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pelican Riding a Bike")
        self.root.geometry("600x450")
        
        # Create canvas with light blue background
        self.canvas = tk.Canvas(root, width=600, height=400, bg='lightblue')
        self.canvas.pack(pady=10)
        
        # Create buttons frame
        button_frame = tk.Frame(root)
        button_frame.pack()
        
        # Draw button
        self.draw_btn = tk.Button(button_frame, text="Draw Pelican on Bike", 
                                  command=self.draw_pelican_bike, bg='lightgreen', padx=10)
        self.draw_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        self.clear_btn = tk.Button(button_frame, text="Clear Canvas", 
                                   command=self.clear_canvas, bg='lightcoral', padx=10)
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Initial draw
        self.draw_pelican_bike()
    
    def clear_canvas(self):
        """Clear everything from the canvas"""
        self.canvas.delete("all")
        # Restore light blue background
        self.canvas.create_rectangle(0, 0, 600, 400, fill='lightblue', outline='')
    
    def draw_pelican_bike(self):
        """Draw a pelican riding a bicycle"""
        self.clear_canvas()
        
        # --- Bicycle ---
        # Rear wheel
        self.canvas.create_oval(110, 260, 190, 340, outline='gray', width=3, fill='black')
        self.canvas.create_oval(115, 265, 185, 335, outline='darkgray', width=2, fill='lightgray')
        
        # Front wheel
        self.canvas.create_oval(410, 260, 490, 340, outline='gray', width=3, fill='black')
        self.canvas.create_oval(415, 265, 485, 335, outline='darkgray', width=2, fill='lightgray')
        
        # Bike frame (main triangle)
        self.canvas.create_line(150, 290, 300, 180, width=8, fill='red')  # Rear to seat
        self.canvas.create_line(300, 180, 450, 290, width=8, fill='red')  # Seat to front
        self.canvas.create_line(150, 290, 450, 290, width=8, fill='red')  # Bottom tube
        
        # Seat post and seat - FIXED: changed 'darkbrown' to 'brown'
        self.canvas.create_line(300, 180, 300, 130, width=6, fill='red')  # Seat post
        self.canvas.create_rectangle(270, 110, 330, 130, fill='brown', outline='saddlebrown', width=2)  # Seat
        
        # Handlebars
        self.canvas.create_line(150, 290, 110, 220, width=6, fill='red')  # Handlebar stem
        self.canvas.create_line(110, 220, 90, 210, width=6, fill='red')  # Left grip
        self.canvas.create_line(110, 220, 130, 210, width=6, fill='red')  # Right grip
        
        # Pedals (simplified)
        self.canvas.create_oval(290, 280, 310, 300, fill='silver', outline='gray')  # Left pedal
        self.canvas.create_oval(330, 280, 350, 300, fill='silver', outline='gray')  # Right pedal
        
        # --- Pelican ---
        # Body (large oval)
        self.canvas.create_oval(260, 160, 340, 240, fill='white', outline='black', width=2)
        
        # Head (small circle)
        self.canvas.create_oval(330, 140, 360, 170, fill='white', outline='black', width=2)
        
        # Eye
        self.canvas.create_oval(345, 150, 350, 155, fill='black')
        
        # Beak (long and curved)
        # Lower beak
        self.canvas.create_polygon(355, 155, 370, 150, 380, 160, 355, 165, 
                                   fill='orange', outline='darkorange', width=2)
        # Upper beak (smaller)
        self.canvas.create_polygon(355, 150, 368, 145, 375, 150, 355, 155,
                                   fill='darkorange', outline='orange', width=1)
        
        # Wing (simple arc shape)
        points = [280, 170, 260, 150, 270, 130, 295, 135, 300, 150]
        self.canvas.create_polygon(points, fill='gray', outline='black', width=1)
        
        # Legs
        self.canvas.create_line(295, 240, 300, 280, width=4, fill='brown')  # Left leg
        self.canvas.create_line(315, 240, 320, 280, width=4, fill='brown')  # Right leg
        
        # Feet (on pedals)
        self.canvas.create_oval(295, 275, 305, 285, fill='orange', outline='brown')  # Left foot
        self.canvas.create_oval(335, 275, 345, 285, fill='orange', outline='brown')  # Right foot
        
        # --- Details ---
        # Ground line
        self.canvas.create_line(0, 340, 600, 340, fill='green', width=3)
        
        # Sun
        self.canvas.create_oval(500, 20, 550, 70, fill='yellow', outline='orange', width=2)
        
        # Sun rays - FIXED: Check if numpy is available, otherwise use simplified version
        try:
            import numpy as np
            for angle in range(0, 360, 45):
                x1 = 525 + 35 * np.cos(np.radians(angle))
                y1 = 45 + 35 * np.sin(np.radians(angle))
                x2 = 525 + 45 * np.cos(np.radians(angle))
                y2 = 45 + 45 * np.sin(np.radians(angle))
                self.canvas.create_line(x1, y1, x2, y2, fill='yellow', width=2)
        except ImportError:
            # Simplified sun rays without numpy
            import math
            for angle in range(0, 360, 45):
                rad = math.radians(angle)
                x1 = 525 + 35 * math.cos(rad)
                y1 = 45 + 35 * math.sin(rad)
                x2 = 525 + 45 * math.cos(rad)
                y2 = 45 + 45 * math.sin(rad)
                self.canvas.create_line(x1, y1, x2, y2, fill='yellow', width=2)
        
        # Add some clouds
        self.create_cloud(80, 60, 30)
        self.create_cloud(200, 40, 25)
    
    def create_cloud(self, x, y, size):
        """Helper function to draw a simple cloud"""
        self.canvas.create_oval(x, y, x+size*2, y+size, fill='white', outline='lightgray')
        self.canvas.create_oval(x+size, y-size//2, x+size*3, y+size//2, fill='white', outline='lightgray')
        self.canvas.create_oval(x+size*2, y, x+size*4, y+size, fill='white', outline='lightgray')

def main():
    root = tk.Tk()
    app = PelicanBikeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
