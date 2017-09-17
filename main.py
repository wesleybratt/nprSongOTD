import urllib.request
import re
import os

#### SETTINGS ####
url = 'http://feeds.kexp.org/kexp/songoftheday'
basedir = 'songs/'
pattern = re.compile(r'^\d{4}$')

all_ids = []
id_to_add = []


def savefile(url, filename):
    if filename not in all_ids:
        if not os.path.isfile(basedir + filename):
            id_to_add.append(filename)
            urllib.request.urlretrieve(url, basedir + filename)


if __name__ == '__main__':
    if not os.path.exists(basedir):
        os.makedirs(basedir)

    if os.path.isfile('data.txt'):
        with open('data.txt', 'r') as file:
            for line in file:
                if line:
                    all_ids.append(line)

    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    urllist = re.findall(r'<media:content url="(.*?)" fileSize=', str(respData))

    for url in urllist:
        filename = url.split("/")[-1]
        date = filename.split("_")[0]
        postid = filename.split("_")[1]
        if pattern.match(postid):
            prefix = date + "_" + postid + "_"
            mp3name = filename.replace(prefix, "")
            savefile(url, mp3name)
        else:
            date2 = filename.split("_")[1]
            postid = filename.split("_")[2]
            if pattern.match(postid):
                prefix = date + "_" + date2 + "_" + postid + "_"
                mp3name = filename.replace(prefix, "")
                savefile(url, mp3name)
            else:
                savefile(url, filename)

    with open('data.txt', 'a') as outfile:
        for item in id_to_add:
            outfile.write("%s\n" % item)
