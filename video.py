from pytube import YouTube

class Video:

    def __init__(self, link):
        self.link = link

    def vadlidate_link(self):
        if 'https://www.youtube.com/' not in self.link or self.link == 'https://www.youtube.com/':
            print('Nie działa')
            return False
        else:
            return True

    def download(self):
        yt = YouTube(self.link)
        yt.streams.filter(progressive = True, file_extension = 'mp4').order_by('resolution').first().download()
