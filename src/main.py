import yt_dlp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime, re, random, time

# Get Full Description from YouTube video
def get_description(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        # Parse for timestamps in description
        return get_timestamps(info["description"])

# Parse for timestamps in the YouTube video's description
def get_timestamps(desc):
    lines = desc.split('\n')
    times = {}

    # for each line in description...
    for line in lines:
        # ... does the line have a timestamp? If so, add to 'times'
        found = search_line_for_stamp(line)
        if found is not None:
            times[line] = found

    if len(times) == 0:
        # This YouTube video does not have timestamps
        print("No timestamps were found in the description.")
        exit(2)

    return times

# Converts matched substrings into timedelta objects
def handle_timestamp(desc: str):

    # return time_stamps
    stamps = desc.split(":")
    stamps = [int(s) for s in stamps]

    t = None
    if len(stamps) == 3:       
        t = datetime.timedelta(hours=stamps[0], minutes=stamps[1], seconds=stamps[2])

    if len(stamps) == 2:
        t = datetime.timedelta(minutes=stamps[0], seconds=stamps[1])

    return t

# Given a line of text, see if a timestamp is written and matches HH:MM:SS format
def search_line_for_stamp(line:str):

    # I did not come up this regex on my own:
    # thanks: https://stackoverflow.com/questions/8318236/regex-pattern-for-hhmmss-time-string
    prog = re.compile("(?:(?:([01]?\d|2[0-3]):)?([0-5]?))?(\d:[0-5]\d)")

    m = prog.search(line)
    if m:
       return handle_timestamp(m.group(0))
    return None

def play_url(driver, url, times):
    driver.get(url)

    l = []

    for i, (k,v) in enumerate(times.items()):
        print(f'{i}. {k}')
        l.append(k)

    print('q - QUIT, s - SHUFFLE')


    while True:
        song = input(f'index of song [0:{len(times) - 1}]: ')
        if song == 'q':
            break

        else:
            my_list = [song]
            if song == 's':
                my_list = list(range(0,len(times) - 1))
                random.shuffle(my_list)
                print(f'playing {my_list}')

            for x in my_list:
                key = l[int(x)]
                second = times[key]
                new_url = f'{url}&t={int(second.total_seconds())}s'
                driver.get(new_url)
                #ignores ads
                time.sleep(int(second.total_seconds()))
        

def main():

    print('Welcome to Youtube Soundtrack Shuffler')

    options = Options()
    #options.add_argument("--headless=new")
    options.add_argument("--lang=en")
    driver = webdriver.Chrome(options=options)

    while True:
        url = input('Enter a url: ')
        if url == 'q':
            break

        times = get_description(url)
        if len(times) > 0:
            play_url(driver, url, times)

    driver.quit()


if __name__ == "__main__":
    main()