import requests
import json
import Queue, threading
import urllib
import os
import argparse
import progressbar

def get_picture_urls(user):
    max_id = ''
    lam = []
    info = []
    while True:
        r = requests.get('https://www.instagram.com/%s/media/?max_id=%s' % (user, max_id))
        media = r.json()
        items =  media['items']
        if items:
            for item in items:
                url = item['images']['standard_resolution']['url']
                created_time = item['created_time']
                lam.append(url)
                lam.append(created_time)
                info.append(lam)
                lam = []

        else:
            return info
            break
        max_id = items[-1]['id']

def run(q, user, done):
    url_and_time = q.get_nowait()
    urllib.urlretrieve(url_and_time[0], "../photos/" + user + '/' + url_and_time[1] + ".jpg")
    done.append(url_and_time)
    bar.update(len(done))
    q.task_done()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help = "Your Instagram Username", type = str)
    args = parser.parse_args()
    print "Making Directory..."
    if not os.path.exists("../photos/" + args.username):
      os.makedirs("../photos/" + args.username)
    print "Getting Necessary Data..."
    info = get_picture_urls(args.username)
    print "Now Downloading!"
    done = []
    bar = progressbar.ProgressBar(len(info))
    bar.start()
    q = Queue.Queue()
    for url_and_time in info:
        q.put(url_and_time)
        thread = threading.Thread(target = run, args = (q,args.username, done))
        thread.start()
    q.join()
    print "Done!"