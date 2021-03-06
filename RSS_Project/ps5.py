import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
        #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
        #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret


class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


# ======================
# Triggers
# ======================
class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError


# PHRASE TRIGGERS
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def is_phrase_in(self, text):
        phrase = self.phrase
        text = text.lower()

        for char in string.punctuation:
            text = text.replace(char, ' ')

        split_text = text.split()

        clean_text = ' '.join(split_text)

        if re.findall('\\b' + phrase + '\\b', clean_text):
            found = True
        else:
            found = False
        return found

class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS
class TimeTrigger(Trigger):
    def __init__(self, pubtime):
        format = '%d %b %Y %H:%M:%S'
        pubtime = datetime.strptime(pubtime, format)
        pubtime = pubtime.replace(tzinfo=pytz.timezone("EST"))
        self.pubtime = pubtime

class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        return self.pubtime > story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        return self.pubtime < story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

# COMPOSITE TRIGGERS
class NotTrigger(Trigger):
    def __init__(self, other_trigger):
        self.other_trigger = other_trigger
    def evaluate(self, story):
        return not self.other_trigger.evaluate(story)

class AndTrigger(Trigger):
    def __init__(self, other_trigger1, other_trigger2):
        self.other_trigger1 = other_trigger1
        self.other_trigger2 = other_trigger2
    def evaluate(self, story):
        return self.other_trigger1.evaluate(story) and self.other_trigger2.evaluate(story)

class OrTrigger(Trigger):
    def __init__(self, other_trigger1, other_trigger2):
        self.other_trigger1 = other_trigger1
        self.other_trigger2 = other_trigger2
    def evaluate(self, story):
        return self.other_trigger1.evaluate(story) or self.other_trigger2.evaluate(story)


# ======================
# Filtering
# ======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    valid_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                valid_stories.append(story)

    return valid_stories


# ======================
# User-Specified Triggers
# ======================
# Problem 11
def create_trigger(trigger_type, phrase = None, time = None, trig1 = None, trig2 = None):
    if trigger_type.lower() == 'title':
        trigger = TitleTrigger(phrase)
    elif trigger_type.lower() == 'description':
        trigger = DescriptionTrigger(phrase)
    elif trigger_type.lower() == 'after':
        trigger = AfterTrigger(time)
    elif trigger_type.lower() == 'before':
        trigger = BeforeTrigger(time)
    elif trigger_type.lower() == 'andtrig':
        trigger = AndTrigger(trig1, trig2)
    elif trigger_type.lower() == 'ortrig':
        OrTrigger(trig1, trig2)
    elif trigger_type.lower() == 'nottrig':
        trigger = NotTrigger(trig1)

    return trigger


def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    trigger_file = open(filename, 'r')

    lines = []
    TriggerList = []
    TriggerDict = {}

    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    for line in lines:
        line = line.split(',')
        print(line)
        print(line[0])
        x = line[0]
        if line[0].lower() == 'add':
            for i in range(1, len(line)):
                print('add:', line[i])
                TriggerList.append(TriggerDict[line[i]])
        elif line[1].lower() == 'title':
            print('create title trigger')
            TriggerDict[x] = create_trigger('title', line[2])
        elif line[1].lower() == 'description':
            print('create description trigger')
            TriggerDict[x] = create_trigger('description', line[2])
        elif line[1].lower() == 'after':
            print('create after trigger')
            TriggerDict[x] = create_trigger('after', None, line[2])
        elif line[1].lower() == 'before':
            print('create before trigger')
            TriggerDict[x] = create_trigger('before', None, line[2])
        elif line[1].lower() == 'and':
            print('create and trigger')
            TriggerDict[x] = create_trigger('andTrig', None, None, line[2], line[3])
        elif line[1].lower() == 'or':
            print('create or trigger')
            TriggerDict[x] = create_trigger('orTrig', None, None, line[2], line[3])
        elif line[1].lower() == 'not':
            print('create not trigger')
            TriggerDict[x] = create_trigger('notTrig', None, None, line[2])
    print(TriggerList)
    return TriggerList



SLEEPTIME = 120  # seconds -- how often we poll


def main_thread(master):
    try:
        # Problem 11
        triggerlist = read_trigger_config('triggers.txt')

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica", 14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title() + "\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:
            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            #BELOW
            stories = filter_stories(stories, triggerlist)
            ######

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()