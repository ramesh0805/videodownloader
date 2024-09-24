import logging
from tkinter import *
from PIL import Image, ImageTk
from pytube import YouTube
import instaloader

# Enable logging
logging.basicConfig(level=logging.DEBUG)

class Downloader:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title("MM Downloads")
        self.root.minsize(500, 300)
        self.root.maxsize(500, 300)
        self.logo = Label(text="Video Downloader", font="TECKTON 25", bg="#f7f1de", pady=15, padx=5, borderwidth=2, relief=RAISED)
        self.logo.pack(fill=X)
        self.youtube_button = Button(text="Youtube", bg="#df130b", width=20, padx=5, pady=5, borderwidth=2, relief=RAISED, command=self.youtube_edit)
        self.youtube_button.pack()
        self.insta_button = Button(text="Instagram", bg="#f70b57", fg="white", width=20, padx=5, pady=5, borderwidth=2, relief=RAISED, command=self.instagram_edit)
        self.insta_button.pack()
        self.root.mainloop()

    # code for downloading Youtube Videos
    def youtube(self):
        try:
            self.url = self.input.get()
            self.yt = YouTube(self.url)
            
            streams = self.yt.streams.filter(progressive=True, file_extension='mp4')
            if not streams:
                raise Exception("No streams available for download.")
            
            self.save = streams.get_highest_resolution()
            self.save.download(filename="video1.mp4")
            success = Label(text="Download Complete", fg="green")
            success.pack()
        except Exception as e:
            error = Label(text=f"Something went wrong: {str(e)}", fg="red")
            error.pack()

    # Other methods remain unchanged...

    # code for downloading Instagram videos
    def instagram(self):
        self.loader = instaloader.Instaloader(
            download_comments=False,
            download_geotags=False,
            download_pictures=False,
            download_video_thumbnails=False,
            save_metadata=False
        )

        self.url = self.input.get()
        self.shortcode = self.url.split('/')[-2]

        try:
            self.post = instaloader.Post.from_shortcode(self.loader.context, self.shortcode)
            self.root.title("Downloading...")
            self.loader.download_post(self.post, target="ram")
            self.root.title("MM Downloads")
            success = Label(text="Download Complete", fg="green")
            success.pack()
        except Exception as e:
            error = Label(text=f"Something went wrong: {str(e)}", fg="red")
            error.pack()

    # To delete the old buttons and Label and to add new Instagram logo, entry and Download button
    def instagram_edit(self):
        self.clear_screen()
        self.photo = Image.open("instagram.png")
        self.resized_photo = self.photo.resize((100, 100))
        self.img = ImageTk.PhotoImage(self.resized_photo)
        self.label_img = Label(image=self.img)
        self.label_img.image = self.img  # Keep a reference
        self.label_img.pack()

        self.input = Entry(width=50)
        self.input.pack()
        self.download = Button(text="Download", command=self.instagram)
        self.download.pack()

    # To delete the old buttons and Label and to add new youtube logo, entry and Download button
    def youtube_edit(self):
        self.clear_screen()
        self.photo = Image.open("youtube.png")
        self.resized_photo = self.photo.resize((150, 100))
        self.img = ImageTk.PhotoImage(self.resized_photo)
        self.label_img = Label(image=self.img)
        self.label_img.image = self.img  # Keep a reference
        self.label_img.pack()

        self.input = Entry(width=50)
        self.input.pack()
        self.download = Button(text="Download", command=self.youtube)
        self.download.pack()

    # Method to clear the screen for new content
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

Downloader()
