# Teacher's Day Card Generator

This project is a Streamlit application that allows users to generate personalized greeting cards for Teacher's Day. Users can input the name of their teacher, and the application will create a card using a predefined template and a custom font.

## Project Structure

```
teachers-day-card-generator
├── app.py                     # Streamlit application code
├── requirements.txt           # Project dependencies
├── GreatVibes-Regular.ttf     # Custom font for card styling
├── teachers-day-template.png   # Template image for the greeting card
└── README.md                  # Project documentation
```

## Requirements

To run this application, you need to have the following Python packages installed:

- Streamlit
- Pillow

You can install the required packages using the following command:

```
pip install -r requirements.txt
```

## Running the Application

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the Streamlit application using the command:

```
streamlit run app.py
```

4. Open the provided URL in your web browser to access the application.
5. Enter the teacher's name in the input field and click on "Generate Card" to create a personalized greeting card.
6. You can download the generated card using the download button.

## Customization

- You can replace `teachers-day-template.png` with your own template image if desired.
- To change the font style, replace `GreatVibes-Regular.ttf` with a different font file, ensuring it is compatible with the Pillow library.

## License

This project is open-source and available for anyone to use and modify.