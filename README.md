# chillist
[work in progress-ish] An aesthetic productivity app for students who struggle with time management and motivation. AIF final project/output of learning.

Inspired by [StudyTogether](https://www.studytogether.com) and [Virtual Cottage](https://steamcommunity.com/app/1369320).

If you're here I'm assuming you're from the SACE board here to check that this is actually real. If so, look no further! There are installation instructions below and feature GIFs underneath that.

## Installation Instructions
_You can install the latest release by simply downloading the `Chillist.exe` file from the [Releases page](https://github.com/phthallo/chillist/releases), as long as you are a Windows user. It should work regardless of whether you have Python installed._

(I used [Pyinstaller](https://pyinstaller.org/en/stable/) on Windows, which is not a cross-compiler). 

Alternatively, you can download the source code and run `main.py` instead (this will require downloading all of Chillist's dependencies, which include:
- [pygame](https://www.pygame.org/wiki/GettingStarted)
- [pygame-text-input](https://www.pygame.org/project-Pygame+Text+Input-3013-.html) 
- [notify-py](https://pypi.org/project/notify-py/)

Your data is stored at `%userprofile%\Documents\Chillist`.
Settings are stored under `settings.json`, and music files (*.mp3, *.ogg, *.wav) can be added in the subfolder `mus`.

## Features
#### Pomodoro Timer 
- Visual Pomodoro timer with customisable study/break intervals.
- Notifcations sent to the user's device upon conclusion of intervals. 
- Pausable and restartable.

![pomotimer](https://github.com/phthallo/chillist/assets/84078890/7f895bbc-2fab-4c0e-8e78-068c814be4a8)

#### Music Player
- Minimalistic music player preloaded with a selection of lo-fi tracks (see ## Credits)
- Songs can be substutited with the user's choice of audio files (with a supported file format, though), and are played in shuffle.

![musicplayer](https://github.com/phthallo/chillist/assets/84078890/f8ca92e5-07a4-4316-824d-d280b7c8484e)

#### Task Matrix
- Inspired by the Eisenhower task priority matrix. 
- Contains 'stickers' that represent tasks, which can be placed anywhere on the matrix to delegate importance. 
- Tasks persist through app restarts, and are included alongside the Pomodoro timer's to-do list (where they can be 'completed' to be removed from the matrix)

![taskmatrix](https://github.com/phthallo/chillist/assets/84078890/fac3edcf-39c3-4185-8104-17b9a3b2a6a1)


## Credits
The font used is [Sysfont by Alina Sava](https://fontsarena.com/sysfont-by-alina-sava/), which is available under the [SIL Open Font License](https://scripts.sil.org/cms/scripts/page.php?item_id=OFL-FAQ_web). From my understanding, I can include the files within this program as long as I include the original unmodified license (under 1.2 and 1.3). Please inform me if I have misinterpreted this.

Lo-fi songs come from [Chosic](https://www.chosic.com/free-music/lofi/), and the tracks are:
```
And So It Begins by Artificial.Music | https://soundcloud.com/artificial-music/
Licensed under Creative Commons: Attribution 3.0 Unported (CC BY 3.0)
https://creativecommons.org/licenses/by/3.0/
Music promoted by https://www.chosic.com/free-music/all/

Embrace by Sappheiros | https://soundcloud.com/sappheirosmusic
Music promoted on https://www.chosic.com/free-music/all/
Creative Commons Attribution 3.0 Unported (CC BY 3.0)
https://creativecommons.org/licenses/by/3.0/

Journey’s End by Purrple Cat | https://purrplecat.com/
Music promoted by https://www.chosic.com/free-music/all/
Creative Commons CC BY-SA 3.0
https://creativecommons.org/licenses/by-sa/3.0/

Memories of Spring by Tokyo Music Walker | https://soundcloud.com/user-356546060
Music promoted by https://www.chosic.com/free-music/all/
Creative Commons CC BY 3.0
https://creativecommons.org/licenses/by/3.0/

Missing You by Purrple Cat | https://purrplecat.com/
Music promoted by https://www.chosic.com/free-music/all/
Creative Commons CC BY-SA 3.0
https://creativecommons.org/licenses/by-sa/3.0/

Stardust by JSH | https://soundcloud.com/thejshmsc/stardust
Music promoted by https://www.chosic.com/free-music/all/
Creative Commons CC0 Public Domain```
