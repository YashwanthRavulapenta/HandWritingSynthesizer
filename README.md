# Handwriting Generator

## Overview
This project is a **Handwriting Generator** that converts typed text into handwritten-style images. It uses a dataset of character images to generate text in a natural handwritten format.

## Features
- **Text Input & File Upload**: Users can type text directly or upload a `.txt` file.
- **Handwritten Text Generation**: Converts the input text into a handwritten-style image.
- **Customizable Spacing**: Ensures proper word, line, and paragraph spacing.
- **Graphical User Interface (GUI)**: Built using Tkinter for easy interaction.
- **Save & View Generated Image**: Allows users to save and view the generated handwriting image.

## Technologies Used
- **Python 3.x**
- **OpenCV** (for image processing)
- **NumPy** (for array manipulation)
- **TensorFlow & Keras** (for model handling)
- **PIL (Pillow)** (for image generation and processing)
- **Tkinter** (for GUI implementation)

## Installation
### Prerequisites
Ensure you have Python 3.x installed. Then install the required dependencies:
```bash
pip install opencv-python numpy tensorflow pillow tkinter
```

## Usage
### Running the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/handwriting-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd handwriting-generator
   ```
3. Run the script:
   ```bash
   python handwriting_generator.py
   ```

### Using the GUI
1. **Enter Text**: Type text into the provided input box.
2. **Upload File (Optional)**: Upload a `.txt` file with text content.
3. **Generate Handwriting**: Click the "📝 Generate" button.
4. **View & Save**: Click "💾 Save & View" to open the generated handwriting image.
5. **Clear Input**: Use the "🗑️ Clear" button to reset the input area.

## Dataset Structure
The dataset should be stored in the following format:
```
handwriting_dataset/
│── lowercase/
│   │── a/
│   │   ├── img1.png
│   │   ├── img2.png
│   │── b/
│   │   ├── img1.png
│── uppercase/
│── numbers/
```
Ensure all character images are grayscale and 64x64 pixels.

## Customization
- Modify `IMG_SIZE` in the script to adjust character size.
- Change `LINE_SPACING`, `WORD_SPACING`, and `PARAGRAPH_SPACING` for different text formatting.

## Future Enhancements
- Improve character variation using a trained handwriting style model.
- Add more character styles for a natural handwritten effect.
- Support additional languages and symbols.

## Contributing
Feel free to fork this repository and submit pull requests for improvements.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contact
For any queries, reach out at: **yashuravulapenta@gmail.com**

