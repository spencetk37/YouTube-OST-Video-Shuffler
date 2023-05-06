Name: YouTube OST Video Shuffler (YOVS)

Usage:
    python3 src/main.py

Desc:
    (This is a work in progress)

    Many OST/music mix videos on YouTube comprise of many songs that listeners play through in the same order. After many playthroughs of the same video, a listenener may get sick of certain songs or want to shuffle the order like in popular music applications such as Apple Music or Spotify. However, there is no such automated way to shuffle or restrict sections since it is all contained in a single video. Some of these videos do contain timestamps in their description but that still requires users to manually click on links to navigate the video. I solve this problem with the YouTube OST Video Shuffler (YOVS); this allows a user to shuffle, queue, or restrict songs in the video by interacting with a command line interface (would like to make a GUI or web app for this).

    To the best of my knowledge, YouTube does some automation already with timestamps to create a Chapter section (mainly for instructional videos or tutorials), but they only support repeating individual sections and simple navigation as it may not make logical sense to shuffle tutorial sections that are time-sensitive.

    ===IMPORTANT===
    UPON STARTING the program; the prompt will ask for the user to input a YouTube video's url. The program assumes that the url will be a music mix or OST video with a list of timestamps in its description. The program searchs each line of the description for a HH:MM:SS or MM:SS regular expression. A video without timestamps will not work and just play at beginning of video.

    ===YOUTUBE ADS===
    My initial idea for this project was a music bot for discord; however, I noticed some popular bots like Groovy were taken down by YouTube for its commercial uses. The only thing I intend to add is a way to click on SKIP AD when ready to click. No other ad-circumvention will be used.


Example:
    I'm pretty big on listening to video game soundtracks (and can easily predict song ordering). One album is Witcher 3 soundtrack 



Requirements:
    Python v3.9.7
    MacOS (only tested here so far...)

    Python Packages:
        yt-dlp   - accessing YouTube description (this can also be used for getting video/audio    streams but I wanted a solution that did not download anything to local machine)

        selenium - For automated control of Google Chrome; a to-do is using library to skip YouTube ads

        datetime - Need seconds conversion for timestamps

        re - Regex for extracting timestamps from YouTube description




    

    