# SpotiPiKids

A Spotify based music player for small children.

*Still in concept phase*

There exist some great devices which enable small children to select and play their music and audio plays independent of adults - e.g. Tonies Box.
However, those devices usually cost a lot per episode (10-15 €). At the same time, the same family often has a Spotify premium account 
which gives access to a nearly unlimited amount of audio play episodes.

This project aims at providing a simple method for children, to listen to Spotify audio plays.
The Spotify music, audio plays, playlists, ... are identified via a QR code, that can easily generated and printed on a piece of paper or cardboard (obviously the card is printed with nice descriptive colourful figures that identify the content - otherwise your kids won't like it).
The QR code is placed in front of a Raspberry with a camera that reads the QR code and starts playback.
For play/pause /next/previous some buttons can be connected via GPIO.

## Setup

 * pip3 install --upgrade spotify-cli
 * pip3 install opencv-contrib-python
 * pip3 install opencv-contrib-python==4.1.0.25
 * curl -sL https://dtcooper.github.io/raspotify/install.sh | sh
   - Add username/pwd to enable visibility of device
 * Start SpotiPiKids 
 

 
## Issues
 * Current implementation allows injecting shell commands via QR code - this is a horrible horrible security issue! I will think about a decent implementation if this project becomes relevant.
