import streamlit as st
from pytube import YouTube
import os

def download_youtube_video(url, output_path):
    try:
        # Create a YouTube object by passing the URL of the video
        video = YouTube(url)

        # Select the highest resolution available for download
        stream = video.streams.get_highest_resolution()

        # Download the video to the specified output path
        stream.download(output_path)

        st.success("Video downloaded successfully!")
    except Exception as e:
        st.error("An error occurred while downloading the video: " + str(e))

# Streamlit app
def main():
    st.title("YouTube Video Downloader")

    # Get video URL from user input
    video_url = st.text_input("Enter YouTube video URL")

    # Define output directory for downloaded video
    output_directory = st.text_input("Select output directory", type="folder")

    # Download button
    if st.button("Download"):
        if video_url:
            if output_directory:
                download_youtube_video(video_url, output_directory)
            else:
                st.warning("Please select an output directory.")
        else:
            st.warning("Please enter a valid YouTube video URL.")

if __name__ == '__main__':
    main()
