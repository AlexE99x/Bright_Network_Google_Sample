"""A video player class."""
import random

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playing = ""
        self.status = "STOPPED"

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        vids = self._video_library.get_all_videos()
        vids.sort(key=lambda x: x.title, reverse=False)

        print("Here's a list of all available videos:")
        for i in range(num_videos):
            tags = len(vids[i].tags)
            if tags == 0:
                print("\t%s (%s) [" % (vids[i].title, vids[i].video_id) + "]")
            else:
                s = ""
                for j in range(tags):
                    if s == "":
                        s = s + vids[i].tags[j]
                    else:
                        s = s + " " + vids[i].tags[j]
                print("\t%s (%s) [" % (vids[i].title, vids[i].video_id) + s +"]")

    def play_video(self, video_id):
        try:
            new_vid = self._video_library.get_video(video_id).title
            if self.playing != "":
                print("Stopping video: %s" % self.playing)
            print("Playing video: %s" % new_vid)
            self.playing = new_vid
            self.status = "PLAYING"
        except AttributeError:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        if self.playing == "":
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: %s" % self.playing)
            self.playing = ""
            self.status = "STOPPED"

    def play_random_video(self):
        if len(self._video_library.get_all_videos()) == 0:
            print("No videos available")
            return
        num = random.randint(0, len(self._video_library.get_all_videos())-1)
        vids = self._video_library.get_all_videos()
        self.play_video(vids[num].video_id)

    def pause_video(self):
        if self.playing == "":
            print("Cannot pause video: No video is currently playing")
        elif self.status == "PAUSED":
            print("Video already paused: %s" % self.playing)
        else:
            print("Pausing video: %s" % self.playing)
            self.status = "PAUSED"

    def continue_video(self):
        if self.playing == "":
            print("Cannot continue video: No video is currently playing")
        elif self.status != "PAUSED":
            print("Cannot continue video: Video is not paused")
        else:
            print("Continuing video: %s" % self.playing)

    def show_playing(self):
        if self.playing == "":
            print("No video is currently playing")
        else:
            vids = self._video_library.get_all_videos()
            for i in range(len(vids)):
                if vids[i].title == self.playing:
                        tags = len(vids[i].tags)
                        if tags == 0:
                            if self.status == "PAUSED":
                                print("Currently playing: %s (%s) [" % (vids[i].title, vids[i].video_id) + "]" + " - %s" % self.status)
                            else:
                                print("Currently playing: %s (%s) [" % (vids[i].title, vids[i].video_id) + "]")
                        else:
                            s = ""
                            for j in range(tags):
                                if s == "":
                                    s = s + vids[i].tags[j]
                                else:
                                    s = s + " " + vids[i].tags[j]
                            if self.status == "PAUSED":
                                print("Currently playing: %s (%s) [" % (vids[i].title, vids[i].video_id) + s + "]" + " - %s" % self.status)
                            else:
                                print("Currently playing: %s (%s) [" % (vids[i].title, vids[i].video_id) + s + "]")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
