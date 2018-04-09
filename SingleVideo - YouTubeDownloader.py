while True:
    import pytube
    import os

    if not os.path.exists('D:/Download-YouTube Videos'):
        os.makedirs('D:/Download-YouTube Videos')
        os.chdir('D:/Download-YouTube Videos')
    else:
        os.chdir('D:/Download-YouTube Videos')

    try:
        myurl = input("Please Enter Youtube Video Link to Download : ")
        print("Fetching Video Formats .. ")
        print()
        yt = pytube.YouTube(myurl)
        videos = yt.streams.filter(
            progressive=True, file_extension='mp4').all()

        s = 1
        print("Please Choose a number from the below list : ")
        print()
        for v in videos:
            print(str(s) + '. ' + str(v))
            s += 1

        while True:
            print()
            videoChoice = input("Please Enter the Number of Video : ")
            try:
                if videoChoice != "":
                    videoChoice = int(videoChoice)
                    vid = videos[videoChoice - 1]
                    print()
                    print("Video Downloading Started......")
                    vid.download()
                    print("Video Downloading Ended........")
                    break
                else:
                    continue
            except:
                print("Please Choose the Correct Number from Above list")
    except:
        print("Please Check Your URL")

    print()

    MoreVideo = input("Do You Wants to Download More Video? (Yes/No) ").lower()
    if MoreVideo == 'yes':
        print()
        continue
    else:
        break
