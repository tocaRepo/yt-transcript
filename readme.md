# YoutubeVideoScraper

YoutubeVideoScraper is a Python class that allows you to scrape information from YouTube videos, including video details, published time, and transcript text.

## Table of Contents

- [YoutubeVideoScraper](#youtubevideoscraper)
  - [Description](#description)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)


## Description

YoutubeVideoScraper is a Python class designed to simplify the process of scraping information from YouTube videos. It provides methods to retrieve video details, such as video ID, published time, title, view count, and transcript text.

## Prerequisites

Before using YoutubeVideoScraper, ensure you have the following prerequisites:

- Python 3.x
- Required Python packages: `youtube_transcript_api`, `scrapetube`

You can install these packages using pip:


pip install youtube-transcript-api scrapetube

## Installation
Clone the repository to your local machine or download the YoutubeVideoScraper.py file.

git clone https://github.com/yourusername/YoutubeVideoScraper.git

Import the YoutubeVideoScraper class into your Python script.

Create an instance of YoutubeVideoScraper and use its methods to scrape YouTube video information.
## Usage
Here's how you can use the YoutubeVideoScraper class:

Create an instance of YoutubeVideoScraper by providing the YouTube channel ID and an optional limit (default is 10).

Call the scrape_videos method to scrape video information. This method returns a list of video objects, each containing the following attributes:
video_id: Video ID.
published_time: Published time as a datetime object.
title: Video title.
view_count: View count.
transcript_text: Transcript text.
