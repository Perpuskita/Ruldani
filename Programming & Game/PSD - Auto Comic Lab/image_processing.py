from PIL import Image, ImageTk
import numpy as np
import cv2

class image:
    def __init__(self, image: Image):
        self.pil_image = image
        # Convert PIL Image to numpy array for OpenCV compatibility
        self.image = np.array(image)
        # Convert RGB to BGR for OpenCV
        self.image_rgb = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)

    def show(self):
        
        x, y = 100, 100
        dot_radius = 5
        color = (0, 0, 255)  # BGR format (red in this case)
        thickness = -1  # -1 means filled circle

        # Draw the dot
        image_with_dot = cv2.circle(self.image_rgb, (x, y), dot_radius, color, thickness)
        # Display the image using OpenCV
        cv2.imshow('Image', image_with_dot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save(self, name):
        # Convert back to PIL Image for saving
        img = cv2.cvtColor(self.image_rgb, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img)
        pil_img.save(f'{name}.jpeg', 'JPEG', quality=90)

    # Return image TK
    def imageTK(self):
        return ImageTk.PhotoImage(self.pil_image)
    
    def plt_imageTK(self, coordinate):
        print("Hallo")