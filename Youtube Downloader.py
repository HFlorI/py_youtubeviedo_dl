from pytube import YouTube
from time import sleep

#Convert seconds to Minutes and prints the solution
def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 

#Ask for Link
link = input("Link eingeben! ")
yt = YouTube(link)

#ez accsess variabeln
title = yt.title
author = yt.author
thumbnail = yt.thumbnail_url
views = yt.views
length = yt.length

#Prints Title 
print("-------------------------------------")
print("Title: ",title)
print("Author: ",author)
print("-------------------------------------")

 #Print length     
print(convert(length)) 

#Print Views
views = str(views)
viewslen = len(views)

if viewslen == 1:
    print(views,"Views")
elif viewslen == 2:
    print(views,"Views")
elif viewslen == 3:
    print(views,"Views")
elif viewslen == 4:
    print(views[0],end=".")
    print(views[1:4],"Views")
elif viewslen == 5:
    print(views[:2],end=".")
    print(views[2:5],"Views")
elif viewslen == 6:
    print(views[:3],end=".")
    print(views[3:6],"Views")
elif viewslen == 7:
    print(views[0],end=".")
    print(views[1:4],end=".")
    print(views[4:7],"Views")
elif viewslen == 8:
    print(views[:2],end=".")
    print(views[2:5],end=".")
    print(views[5:8],"Views")
elif viewslen == 9:
    print(views[:3],end=".")
    print(views[3:6],end=".")
    print(views[6:9],"Views")
elif viewslen == 10:
    print(views[0],end=".")
    print(views[1:4],end=".")
    print(views[4:7],end=".")
    print(views[7:10],"Views")
elif viewslen == 11:
    print(views[:2],end=".")
    print(views[2:5],end=".")
    print(views[5:8],end=".")
    print(views[8:11],"Views")
#Print Thumbnail
print("Thumbnail:",thumbnail)
print("")

udq = input("Do you want to download the highest resolution? Y/N ")
if udq == "Y":
    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download()
    print("Download completed!!")
elif udq == "y":
    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download()
    print("Download completed!!")
elif udq == "N":
    print("----------Video----------")
    print(yt.streams.filter(only_video=True))
    print("----------Audio----------")
    print(yt.streams.filter(only_audio=True))
    uitag = input("Please enter the Itag of the Video or Audio! ")
    ys = yt.streams.get_by_itag(uitag)
    print("Downloading...")
    ys.download()
    print("Download completed!!")
elif udq == "n":
    print("----------Video----------")
    print(yt.streams.filter(only_video=True))
    print("----------Audio----------")
    print(yt.streams.filter(only_audio=True))
    uitag = input("Please enter the Itag of the Video or Audio! ")
    ys = yt.streams.get_by_itag(uitag)
    print("Downloading...")
    ys.download()
    print("Download completed!!")
else:
    quit()


