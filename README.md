# YouTube Comment Analyzer


**Access the project here:** [https://youtube-comment-analyzer-hemasri.streamlit.app/](https://youtube-comment-analyzer-hemasri.streamlit.app/)
## Overview

The **YouTube Comment Analyzer** is a powerful Python-based application designed to help content creators, marketers, and analysts gain valuable insights from YouTube video comments. By leveraging modern technologies such as the **YouTube Data API v3**, **OpenAI's GPT API**, **Streamlit**, and various NLP techniques, the application offers an interactive and easy-to-use platform to analyze and summarize YouTube comments at scale.

This tool allows users to input a YouTube video URL and retrieve the video’s comments. The comments are then analyzed using Natural Language Processing (NLP) to extract key insights such as sentiment analysis, keyword extraction, and comment summarization. The goal is to provide users with a clear, actionable understanding of how their audience feels and what they are discussing, which can be especially useful for content improvement, audience engagement, and marketing strategies.

## Features

### 1. **YouTube Comment Retrieval**
   - The YouTube Data API v3 is used to retrieve comments from a given video. Users can simply enter a YouTube video URL, and the application fetches all the comments related to that video. It supports fetching comments across multiple pages, ensuring that even videos with large numbers of comments are covered.

### 2. **Sentiment Analysis**
   - Sentiment analysis is performed on each individual comment to classify it into three categories: **Positive**, **Negative**, and **Neutral**. This feature helps users understand the emotional tone of their audience, enabling them to identify both praise and criticism effectively.
   - The sentiment score is calculated using NLP techniques, helping content creators and marketers get a clearer view of how the audience feels about a video.

### 3. **Comment Summarization**
   - Using the **OpenAI GPT API**, the application generates concise summaries of the comments. This summarization provides an overview of the most important themes discussed in the comment section without the user having to manually go through hundreds or thousands of individual comments.
   - The summaries are tailored to capture the essence of what the viewers are saying, offering valuable insights into common issues, praises, or questions that arise in the comment section.

### 4. **Keyword Extraction and Topic Modeling**
   - The app analyzes the text of the comments to extract important keywords and phrases that are mentioned frequently across the comment section. This allows users to quickly identify the topics being discussed most frequently by their audience.
   - In addition, the application can perform topic modeling to reveal deeper insights into the specific themes viewers are interested in or concerned about. This can be valuable for understanding audience interests and generating ideas for future content.

### 5. **Interactive Streamlit Interface**
   - The project is built using **Streamlit**, a framework that enables the creation of interactive web applications in Python. The interface is intuitive and user-friendly, allowing users to interact with the analysis results in real-time.
   - Users can visualize sentiment distribution in charts and graphs, view the summary of comments, and explore detailed insights into the keywords and topics discussed by viewers.
   - The application is optimized for ease of use, allowing even non-technical users to take advantage of advanced data analysis and sentiment modeling.

## Use Case and Benefits

- **Content Creators**: YouTube creators can leverage this tool to understand how their audience reacts to videos. By analyzing comment sentiment and identifying common themes, creators can better tailor their content to resonate with their viewers.
  
- **Marketers**: Marketers can use the application to gauge public perception of brands, products, or services discussed in YouTube videos. By analyzing viewer comments, marketers can gain insights into customer satisfaction, concerns, and areas for improvement.

- **Researchers and Analysts**: The tool can be used by researchers to analyze large volumes of unstructured YouTube data, helping them identify trends, conduct sentiment analysis, and summarize online discussions related to particular topics.

## How It Works

1. **Input**: Users enter the URL of any public YouTube video into the app’s input field.
   
2. **Fetch Comments**: The application uses the **YouTube Data API v3** to retrieve the comments associated with the video, ensuring that comments are fetched from the video in real-time.

3. **Analyze Comments**: The app processes the fetched comments using NLP techniques. It performs sentiment analysis to classify comments and generates a summary using OpenAI’s GPT API.

4. **Display Results**: The Streamlit interface displays the analyzed data, including sentiment charts, a summarization of the comments, and the most frequently mentioned keywords. Users can explore this data in an interactive format to better understand the audience's feedback.

## Example Use Cases

- **For YouTube Creators**: A creator might upload a new video and want to understand if the audience is responding positively or negatively to their content. The **YouTube Comment Analyzer** can analyze comments on that video, providing the creator with a sentiment breakdown and a concise summary of the key points discussed by viewers.
  
- **For Marketing Campaigns**: A marketer working on a campaign involving a product review video might want to see how people are reacting to the product based on comments in the video. This tool will help them analyze the tone of the comments and identify if viewers are excited, dissatisfied, or neutral about the product.

- **For Research Purposes**: A researcher examining public discourse on a particular topic might input YouTube videos related to that topic and analyze the trends and sentiments of comments to identify public opinion.

## Conclusion

The **YouTube Comment Analyzer** is a powerful tool for extracting actionable insights from YouTube video comments. By leveraging the YouTube Data API for comment retrieval and the OpenAI API for natural language processing, the application provides content creators, marketers, and researchers with valuable data that can inform decision-making and improve engagement strategies.

With its intuitive interface and powerful features like sentiment analysis, comment summarization, and keyword extraction, this tool is an essential resource for anyone looking to analyze YouTube comments at scale and gain meaningful insights from them.

## Technologies Used

- **YouTube Data API v3**: For fetching comments from YouTube videos.
- **OpenAI GPT API**: For generating comment summaries and performing NLP tasks like sentiment analysis.
- **Streamlit**: For creating an interactive, user-friendly web interface.
- **Natural Language Processing (NLP)**: Techniques used for sentiment analysis, keyword extraction, and summarization.
- **NLTK (Natural Language Toolkit)**: For various NLP operations such as tokenization and processing.
- **Transformers**: For leveraging pretrained transformer models for text analysis.
- **Pytube**: For downloading YouTube videos and comments.
- **Python-dotenv**: For managing environment variables and keeping sensitive data like API keys secure.
- **Google-API-Python-Client**: For interacting with Google APIs, especially the YouTube API.
- **Google-auth-httplib2** and **Google-auth-oauthlib**: For handling authentication and authorization for Google API services.
- **Matplotlib** and **Seaborn**: For visualizing sentiment analysis and other data in graphical format.
