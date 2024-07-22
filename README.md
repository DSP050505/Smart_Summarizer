# CHROME EXTENSION - YOUTUBE VIDEO SUMMARIZER
# YouTube Video Summarizer

## Overview

YouTube Video Summarizer is a Chrome extension that provides concise summaries of YouTube video transcripts. By leveraging natural language processing and machine learning, the extension generates meaningful summaries, helping users quickly grasp the content of lengthy videos.

## Features

- Extracts and summarizes transcripts of YouTube videos.
- Allows users to specify the minimum and maximum length of the summaries.
- User-friendly interface for entering YouTube video URLs and receiving summaries.
- Black-themed popup for better user experience.

## Installation

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/your-username/yt-video-summarizer.git
    ```
2. Navigate to the project directory:
    ```sh
    cd yt-video-summarizer
    ```

## Setting Up the Backend

1. Ensure you have Python and pip installed. Create a virtual environment (recommended):
    ```sh
    python -m venv env
    venv\Scripts\activate or
    source venv/bin/activate


    ```
2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the Flask app:
    ```sh
    python app.py
    ```

## Adding the Chrome Extension

1. Open Chrome and navigate to `chrome://extensions/`.
2. Enable "Developer mode" using the toggle in the top-right corner.
3. Click on "Load unpacked" and select the `yt-video-summarizer` directory.

## Usage

1. Click on the YouTube Video Summarizer extension icon in the Chrome toolbar.
2. Enter the URL of the YouTube video you want to summarize.
3. Specify the minimum and maximum length for the summary (optional).
4. Click the "Summarize" button.
5. The summarized transcript will be displayed in the extension popup.

## Project Structure

- `app.py`: Backend Flask application for processing YouTube video transcripts and generating summaries.
- `popup.html`: HTML file for the Chrome extension popup interface.
- `popup.css`: CSS file for styling the popup.
- `popup.js`: JavaScript file for handling user interactions in the popup.
- `background.js`: Background script for handling extension events.
- `contentScript.js`: Content script for interacting with YouTube pages.
- `manifest.json`: Manifest file defining the extension's properties and permissions.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Contact

For any questions or suggestions, please open an issue or contact me at [doladevisriprasad050505@gmail.com].

