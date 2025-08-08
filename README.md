# Word Cloud Generator App

## Overview
The Word Cloud Generator App allows users to create visually appealing word clouds from text files, PDFs, or Word documents. It processes the uploaded content, removes common stopwords, and generates a customizable word cloud based on user-defined parameters.

## **Features**
- **File Upload Support**: Upload text files, PDFs, or Word documents.
- **Text Processing**: Extracts and processes text while removing stopwords.
- **Customizable Word Cloud**: Adjust width, height, maximum words, background color, contour width, and contour color.
- **Real-Time Visualization**: View the generated word cloud instantly.
- **Download Options**: Save the word cloud in PNG, JPEG, SVG, or PDF formats and download a CSV file of word counts.
- **Word Count Table**: Displays a table of word frequencies.
- **User -Friendly Interface**: Built with Streamlit for an intuitive experience.
- **Interactive Sidebar**: Easily customize settings and view author information.
- **Educational Tool**: Learn about text analysis and visualization.

## **Installation**
To run this app, you need to have Python installed along with the required libraries. You can install the necessary libraries using pip:

```bash
pip install pandas matplotlib wordcloud python-docx PyPDF2 streamlit nltk
```

## Usage
1. Clone the repository or download the code files.
2. Run the app using Streamlit:
   ```bash
   streamlit run app.py
   ```
3. Open your web browser and navigate to the provided local URL.
4. Upload a text file, PDF, or Word document to generate a word cloud.
5. Customize the word cloud settings using the sidebar.
6. Download the generated word cloud or the word count table as needed.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web application framework.
