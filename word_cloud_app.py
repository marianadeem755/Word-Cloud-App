# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from docx import Document
import base64
from io import BytesIO
import PyPDF2
import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

# Function for file reading
def read_txt(file):
    return file.getvalue().decode('utf8')

def read_docx(file):
    doc = Document(file)
    return " ".join([para.text for para in doc.paragraphs])

def read_pdf(file):
    pdf = PyPDF2.PdfReader(file)
    return " ".join([page.extract_text() for page in pdf.pages])

# Function to generate word cloud
def generate_word_cloud(text, stopwords, width, height, max_words, background_color, contour_width, contour_color):
    wordcloud = WordCloud(width=width, height=height, background_color=background_color, stopwords=stopwords,
                          max_words=max_words, contour_width=contour_width, contour_color=contour_color)
    wordcloud.generate(text)
    return wordcloud

# Function to generate download link for Plot
def get_image_download_link(buffered, format_):
    image_base64 = base64.b64encode(buffered.getvalue()).decode()
    return f'<a href="data:image/{format_};base64,{image_base64}" download="wordcloud.{format_}">Download Plot as {format_}</a>'

# Function to generate the Download link for DataFrame
def get_table_download_link(df, filename, file_label):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="{filename}">{file_label}</a>'

# Streamlit code
def main():
    st.title('Word Cloud Generator by Maria Nadeem')
    st.subheader('📂📁 Upload a pdf, docx, or text file to generate a word cloud')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Upload the pdf, txt, or docx file
    uploaded_file = st.file_uploader('Choose a file', type=['pdf', 'docx', 'txt'])

    if uploaded_file:
        file_details = {"fileName": uploaded_file.name, "file_type": uploaded_file.type, "fileSize": uploaded_file.size}
        st.write(file_details)

        # Check the File Type and Read the File
        if uploaded_file.type == 'text/plain':
            text = read_txt(uploaded_file)
        elif uploaded_file.type == 'application/pdf':
            text = read_pdf(uploaded_file)
        elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            text = read_docx(uploaded_file)
        else:
            st.error('File type not supported. Please upload a text, pdf, or docx file.')
            return

        # Word Tokenization and Stopword Removal
        filtered_text = ' '.join([word for word in word_tokenize(text.lower()) if word.isalnum() and word not in stopwords.words('english')])

        # Word Cloud Configuration
        st.subheader('Generated Word Cloud')
        width = st.sidebar.slider("Select Word Cloud Width", 400, 2000, 1200, 100)
        height = st.sidebar.slider("Select Word Cloud Height", 200, 400, 300, 100)
        max_words = st.sidebar.slider("Max Words", 50, 1000, 200, 50)
        background_color = st.sidebar.color_picker("Background Color", "#FFFFFF")
        contour_width = st.sidebar.slider("Contour Width", 0, 10, 3)
        contour_color = st.sidebar.color_picker("Contour Color", "#6495ED")
        font_family = st.sidebar.text_input("Font Family", "sans-serif")

        # Generate Word Cloud
        wordcloud = generate_word_cloud(filtered_text, STOPWORDS, width, height, max_words, background_color, contour_width, contour_color)
        plt.figure(figsize=(width/100, height/100))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title("Word Cloud", fontdict={'fontsize': 16, 'fontweight': 'bold', 'family': font_family})
        st.pyplot()

        # Save plot functionality
        format_ = st.sidebar.selectbox('Select the file format to save the Plot', ['png', 'jpeg', 'svg', 'pdf'])
        resolution = st.sidebar.slider('Select the resolution (dpi)', 100, 300, 100, 10)

        if st.button(f"Save as {format_}"):
            buffered = BytesIO()
            plt.savefig(buffered, format=format_, dpi=resolution)
            st.markdown(get_image_download_link(buffered, format_), unsafe_allow_html=True)

        # Word count table
        words = filtered_text.split()
        word_count = pd.DataFrame({'Word': words}).groupby(by='Word').size().reset_index(name='Count').sort_values('Count', ascending=False)
        st.subheader('Word Count Table')
        st.write(word_count)

        if st.button('Download CSV'):
            st.markdown(get_table_download_link(word_count, 'word_count.csv', 'Download Word Count CSV'), unsafe_allow_html=True)
# Add author name and info to the sidebar
st.sidebar.markdown("### Author: Maria Nadeem🎉🎊⚡")
st.sidebar.markdown("### GitHub: [GitHub](https://github.com/marianadeem755)")
st.sidebar.markdown("### LinkedIn: [LinkedIn Account](https://www.linkedin.com/in/maria-nadeem-4994122aa/)")
st.sidebar.markdown("### Contact: [Email](mailto:marianadeem755@gmail.com)")
st.sidebar.markdown("### Credit: [codanics](https://codanics.com/)")


# Background Image
st.markdown("""
<style>
.stApp {
background: url("https://images.unsplash.com/photo-1472289065668-ce650ac443d2?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTcwNzkzMzM0OQ&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080");
background-size: cover;
    }
</style>""", unsafe_allow_html=True)
# urls of the images
github_url = "https://img.icons8.com/fluent/48/000000/github.png"

# redirect urls
github_redirect_url = "https://github.com/marianadeem755"
# adding a footer
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0; 
    width: 100%;
    background-color: #f5f5f5;
    color: #000000;
    text-align: center;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f'<div class="footer">Made by Maria Nadeem<a href="{github_redirect_url}"><img src="{github_url}" width="30" height="30"></a>'
             f'<a href="https://codanics.com/">Credits: https://codanics.com/</a></div>',unsafe_allow_html=True
    )



if __name__ == '__main__':
    main()
