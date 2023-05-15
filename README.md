# Description
### This code allows the user to select an image using the file manager and perform emotion and age analysis on this image, using the DeepFace library.

### For image selection, the tkinter library is used, which opens a file selection window and waits for the user to select an image. The image is read using the cv2.imread() function from the OpenCV library.

### Then, the ```DeepFace.analyze()``` function is used to perform emotion and age analysis on the image. This function takes as arguments the read image and the list of actions to be performed, in this case, "age" and "emotion".

### Finally, the result of the analysis is displayed in the standard output using the print() function.

# Used Libraries
### cv2: OpenCV library for image processing.
### tkinter: standard Python library for creating graphical user interfaces.
### DeepFace: library for facial analysis that uses convolutional neural networks.

# Code Flow
### Creates the file selection window using the tkinter library.
### Opens the file selection window and waits for the user to select an image.
### Reads the selected image using the cv2.imread() function.
### Performs emotion and age analysis on the image using the DeepFace.analyze() function.
### Displays the analysis result in the standard output using the print() function.