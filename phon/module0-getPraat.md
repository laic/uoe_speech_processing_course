Preliminaries {#preliminaries .unnumbered}
=============

This document is intended as a guide for working with Praat for the
first time to open and annotate a sound file of recorded speech. In
upcoming modules we will learn how to decide which annotations to make
and where, but for now just focus on learning how to use the Praat
functionality.

Goals {#goals .unnumbered}
-----

At the end of this tutorial you should be able to:

-   Load sound files into Praat.

-   Record new sounds in Praat (and save the sound files).

-   Listen to and view sound files.

-   Toggle the analysis view to show or hide the spectrogram.

-   Create a TextGrid annotation for a sound file.

-   Add and delete boundaries in the TextGrid file.

-   Save the TextGrid for later use.

Video resources {#video-resources .unnumbered}
---------------

Sections [1](#section:getpraat){reference-type="ref"
reference="section:getpraat"}-[7](#section:TextGrid){reference-type="ref"
reference="section:TextGrid"} below walk you through each of these
tasks. You may find the following video resources from Professor Richard
Ogden at the University of York helpful as well (click on the link to
open):

-   [Praat 1: Opening a
    file](https://www.youtube.com/watch?v=a4Skes6WfS8&feature=youtu.be)

-   [Praat 2: Zooming in and
    out](https://www.youtube.com/watch?v=b77-wIo5aFU&feature=youtu.be)

-   [Praat 10: Labeling
    intervals](https://www.youtube.com/watch?v=VYc6uHgwpxc&feature=youtu.be)

-   [Praat 9: Saving your
    work](https://www.youtube.com/watch?v=izxtaMTkIpw&feature=youtu.be)

Get Praat {#section:getpraat}
=========

Praat is available for free from the Praat website,
<http://www.fon.hum.uva.nl/praat/>.

For your convenience, here are download links for the three most common
operating systems (click on the name to go to the download page):

-   [Mac](http://www.fon.hum.uva.nl/praat/download_mac.html)

-   [Windows](http://www.fon.hum.uva.nl/praat/download_win.html)

-   [Linux](http://www.fon.hum.uva.nl/praat/download_linux.html)

Save Praat in your Applications folder just like any other application.

Open Praat
==========

Open Praat as you would open any other application on your computer,
typically by double-clicking on the Praat icon, or by finding it under
the Start menu on Windows. The first time you open it, you may get a
warning about running programs you have downloaded from the internet. To
the best of my knowledge it is all safe.

Two windows will appear, the Praat Objects window on the left, and the
Praat Picture window on the right. For this exercise, you can close the
Praat Picture window.

Getting sounds into Praat
=========================

First we need to get some sound files to work with. There are two ways
to do this: open an existing sound file, or a record a new one.

**Note:** Praat is capable of handling most sound file formats,
including MP3 and other familiar file types. However, it is best
practice to use lossless, uncompressed formats such as WAV, AIFF, or
FLAC to ensure high quality sound and reliable analyses. For the
purposes of the PHON tutorials, we'll be using WAV files exclusively.

Record a new sound
------------------

If you're just starting out you might not have any sound files readily
available to work with, so you will need to record your own. You could
do this with any kind of recording software and equipment, but Praat
also provides this functionality.

1.  At the top of the Praat Objects window, click on 'New'.

2.  Select 'Record mono Sound\...' from the drop down menu that appears.

3.  A new SoundRecorder window will appear with a white window labeled
    'Meter' at the center and a few options for you to select. By
    default, the following options should be preselected:

    1.  Channels: Mono

    2.  Input source: Built-in Microph\[one\]

    3.  Sampling frequency: 44100 Hz

    In the bottom right corner of the SoundRecorder, there is also a
    field labeled 'Name:' where you can input a name for the sound. This
    name will appear in the Praat Objects window after you have saved
    your recording.

4.  The Meter window should show a message that reads 'Not recording.'
    Click on 'Record'. Now the Meter window in the center of the
    SoundRecorder should be monitoring the sound coming from your
    microphone. Clap your hands a few times to watch the levels spike
    and turn red. This is an indication that the sound you have recorded
    was too loud and will be distorted or clipped. Try to keep your
    recordings in the green or yellow range. Click on 'Stop' to stop
    recording.

5.  Now record yourself saying 'Hello, world!' (or anything else you'd
    like to say) and save the recording to the Praat Objects list.

    1.  Type a name into the 'Name:' field

    2.  Click on 'Record'

    3.  Wait for the Meter to register sound from your microphone

    4.  Say 'Hello, world!'

    5.  Click on 'Stop'

    6.  Click on 'Save to list' (which should be highlighted in blue).

    You should now see a new item in the Objects list with the name of
    the sound that you recorded.

    If you forgot to name your item, it will be called 'untitled' in the
    Objects list. Simply select the item and then click on 'Rename\...'
    at the bottom of the list to rename it.

6.  If you would like to revisit this file later, be sure to save it
    from the Objects window.

    1.  Select the sound file in the Objects list.

    2.  Click on 'Save', then 'Save as WAV file\...'

    3.  Rename and save your file wherever you'd like.

Open an existing sound file
---------------------------

Most of the time when we are doing acoustic analyses, we are using
pre-recorded data. For this exercise, the following four sound files are
available to you:

-   bit.wav

-   bought_uk.wav

-   bought_us.wav

-   sing.wav

Download these files and save them to a folder where you will be able to
find them easily.

### Open a sound file

Next, load a sound file into Praat with the following steps:

1.  Click on 'Open' at the top of the Praat Objects window.

2.  Click on 'Read from file\...' in the dropdown menu.

3.  In the window that opens, browse to the directory where you have
    previously saved the sound files above.

4.  Select one of the sound files and click on 'Open'.

Listen to the sound
===================

To hear the sound file that you have loaded, select it by clicking on it
and then click on the 'Play' button that will appear on the right hand
side of the Objects window.

Notice that if you deselect the sound by clicking away from it in the
Objects window, the buttons will disappear. This is because the buttons
are *dynamic*, meaning that they change depending on the type of object
you have selected. We'll see an example of such changes in section
[7](#section:TextGrid){reference-type="ref"
reference="section:TextGrid"}.

View the waveform (and spectrogram)
===================================

Make sure the sound is still selected, then click on the 'View and edit'
button. A new window will open that shows the waveform and spectrogram
of the sound you have loaded. For now, we are only interested in the
waveform, so hide the spectrogram and any other analyses by clicking on
'View', then selecting 'Show analyses\...'. In the window that pops up,
untick any boxes that are ticked, then click 'OK'.

Play around with the Sound editor window controls
=================================================

The signal editor, which is the window that now displays the waveform,
can be manipulated in various ways to investigate different parts of the
sound. Play around with the following functionalities:

-   Zoom: click on the 'in' and 'out' buttons at the bottom left corner
    of the window.

-   Scroll along backwards and forwards in the sound by using the scroll
    bar that appears after you zoom in.

-   Play the sound: click on the bars at the bottom of the window.

    -   The **top bar** will play a section of the sound that is visible
        in the window, starting or stopping at the point where the bar
        is split into sections;

    -   The **middle bar** ('Visible part') will play whatever is
        currently visible in the window;

    -   The **bottom bar** will play the entire sound from the
        beginning.

-   Measure the timepoint of a certain part of the waveform by clicking
    on it. A red vertical cursor will appear, with a time value
    displayed at the top of the line.

-   Select a portion of the waveform by clicking and dragging along in
    the view window. You will be able to see the beginning and ending
    times of the selection you have chosen, as well as the duration of
    the selection at the top of the window.

-   Zoom in on your selection by clicking 'sel' in the bottom left near
    the 'in' and 'out' buttons.

Now you know how to use the Sound editor! Zoom all the way out until you
can see the entire sound again. Highlight a section, zoom in on it, and
play it.

**Close the Sound editor window before moving on to the next part of the
exercise.**

Create a TextGrid {#section:TextGrid}
=================

Select the sound from the Objects list again, and then click on
'Annotate'. Click on 'To TextGrid\...' in the dropdown menu. A window
will pop up with fields labeled 'All tier names' and 'Which of these are
point tiers?'

1.  Delete any text that is in these fields.

2.  In the 'All tier names' field, enter *sounds*.

3.  Leave the field about point tiers blank.

4.  Click OK.

You should now see a new object in the Objects lists. This is a TextGrid
with the same name as the sound file. A TextGrid is just a plain text
file with some information that aligns the text with particular time
points in the waveform. Select the TextGrid, and notice how the buttons
in the dynamic window are different from those available when you
selected the Sound file.

In order to do anything useful with a TextGrid, we need to open it along
with the Sound it was made for. To do this, select **both** the Sound
and the TextGrid by clicking and dragging, then click on 'View and Edit'
from the buttons that appear. You should see a new window with the
waveform on top, and the TextGrid on the bottom. The TextGrid should
have just one tier, labeled *segment* on the righthand side.

Annotate the sound file
=======================

In this section you will use the TextGrid to *segment* the sound file
into individual speech sounds, and *label* the segments according to the
sound that appears there.

To segment the speech, you need to insert boundary markers in the
TextGrid between adjacent speech sounds. For the first and last speech
sounds in the file, you will also need to insert a boundary on either
side to show where the sound starts (for the first sound) or ends (for
the last sound).

-   **To insert a boundary** click on the place in waveform where you
    would like to place a boundary. Then click on the circle that
    appears at the top of the gray vertical bar in the TextGrid.

-   **To delete a boundary**, select it by clicking on it (it will turn
    red), then type Alt+Backspace.

-   **To label the interval** you have created, click between the
    boundaries to highlight that interval, then type in the label.

Don't worry if you're not sure where to place a boundary or what label
to give the segments you have created. We will return to this question
in future tutorials.

When you are done adding annotations to your TextGrid, save it by
clicking on 'File' in the Sound editor window, then click on 'Save
TextGrid as text file\...' in the dropdown menu. Save the TextGrid with
the same name as the .wav file it corresponds to, with the file
extension '.TextGrid'.

Reflect and consider
====================

Open the other sound files in the folder in the same way you did for the
first one. Listen to the sound files and examine their waveforms and
spectrograms. What are the similarities and differences among the sound
files? Are these similarities and differences apparent in the visual
representations of the sound?

Acknowledgments
===============

This tutorial was modified by Rebekka Puderbaugh in September 2020 from
previous versions developed by Dr James Kirby in October 2017. Portions
of this tutorial have been modified from Jen's Smith's [LING
520](https://users.castle.unc.edu/~jlsmith/ling520.html) Praat
resources.
