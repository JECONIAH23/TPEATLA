import tkinter
import cv2

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.window.mainloop()
# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")


class MyVideoCapture:
    def __init__(self, video_source=0):
           # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
  
          # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
     # Release the video source when the object is destroyed
    def __del__(self):
         if self.vid.isOpened():
             self.vid.release()
         self.window.mainloop()