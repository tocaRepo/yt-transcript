from youtube_transcript_api import YouTubeTranscriptApi
import scrapetube
from datetime import datetime, timedelta

class YoutubeVideoScraper:
    def __init__(self, channel_id, limit=10):
        self.channel_id = channel_id
        self.limit = limit
        self.current_datetime = datetime.now()

    def concatenate_text(self, data):
        concatenated_text = " ".join(item['text'] for item in data)
        return concatenated_text

    def publish_datetime_to_datetime(self, publishedTime):
        publishedTime_as_date = None

        time_ago = int(publishedTime.split()[0])
        if "hour" in publishedTime:
            publishedTime_as_date = self.current_datetime - timedelta(hours=time_ago)
        elif "minute" in publishedTime:
            publishedTime_as_date = self.current_datetime - timedelta(minutes=time_ago)
        elif "second" in publishedTime:
            publishedTime_as_date = self.current_datetime - timedelta(seconds=time_ago)
        elif "day" in publishedTime:
            publishedTime_as_date = self.current_datetime - timedelta(days=time_ago)
        elif "week" in publishedTime:
            publishedTime_as_date = self.current_datetime - timedelta(weeks=time_ago)
        return publishedTime_as_date

    def scrape_videos(self):
        video_objects = []

        videos = scrapetube.get_channel(self.channel_id, limit=self.limit)

        for video in videos:
            video_id = video['videoId']
            publishedTime = video['publishedTimeText']["simpleText"]
            title = video['title']["runs"][0]["text"]
            view_count = video['viewCountText']["simpleText"]

            publish_time_as_date = self.publish_datetime_to_datetime(publishedTime)

            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript = transcript_list.find_generated_transcript(['en'])
            text = transcript.fetch()
            video_text = self.concatenate_text(text)

            # Create an object to represent the video
            video_object = {
                "video_id": video_id,
                "published_time": publish_time_as_date,
                "title": title,
                "view_count": view_count,
                "transcript_text": video_text
            }
            video_objects.append(video_object)

        return video_objects

if __name__ == "__main__":
    channelid = "channelid"
    scraper = YoutubeVideoScraper(channelid, limit=10)
    videos = scraper.scrape_videos()
    
    # Now, you have a list of video objects. You can access and manipulate them as needed.
    for video in videos:
        print("Video ID:", video["video_id"])
        print("Published Time:", video["published_time"])
        print("Title:", video["title"])
        print("View Count:", video["view_count"])
        print("Transcript Text:", video["transcript_text"])
        print("\n")
