Goals<a name="goals"></a>
=====

At the end of this exercise you should be able to:

-   Segment a recording of speech based on the visual appearance of the
    waveform

-   Label your segmentations using IPA symbols

-   Measure the duration of various segments

-   Calculate the fundamental frequency of vowels

Note that although you will need to use simple arithmetic, you are
always welcome to use a calculator.

Materials<a name="materials"></a>
=========

-   scanit.wav

Waveform segmentation
=====================

In this section you will use the TextGrid to *segment* the sound file
into individual speech sounds based on the shape of the waveform, and
*label* the segments according to the sound that appears there. If you
need a refresher on how to complete any of the following steps, refer to
tutorial 0. Get Praat.

1.  Open the sound file scanit.wav into the Praat Objects window.

2.  Create a TextGrid with one interval tier named \"segments\".

3.  Show the waveform (hide the spectrogram)

4.  View and edit the waveform and TextGrid together.

5.  Use the visual appearance of the waveform to segment the sound file
    into the major classes of speech sound (plosive, fricative, sonorant
    (in this case nasal), and vowel). Refer to the video on waveforms
    and speech sounds if necessary.

6.  Label the segments using appropriate IPA symbols for the sound that
    occurs in each interval. You may do this in any of the following
    ways, listed in order of increasing complexity:

    1.  use an online [symbol picker](https://ilg.usc.es/ipa-chart/keyboard/)
	to select the
        IPA symbols you require, then copy & paste them into the
        relevant segment. (This is the simplest solution and the one I
        recommend if you are not feeling adventurous.)

    2.  use Praat
        [trigraphs](http://uvafon.hum.uva.nl/praat/manual/Phonetic_symbols.html)
        to enter phonetic symbols

    3.  install an IPA
        [keyboard](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=uniipakeyboard)

Once you have annotated and save your TextGrid, reflect on the following
questions and discuss your answers with your tutorial group:

1.  Which sounds were easy to annotate with boundaries? Why were they
    easy?

2.  Which sounds were hard to annotate with boundaries? Why were they
    hard?

Waveform measurements
=====================

Questions 1 and 2 refer to the first word of the phrase, *scan*.

1.  1.  What is the duration of the fricative?

    2.  What is the duration of the vowel?

    3.  What is the duration of the plosive?

2.  1.  What is the duration of the first 5 complete oscillations in the
        vowel? <a name="question:2"></a> <a name="question:2a"></a>

    2.  Divide the duration you measured in [question 2a](#question:2a)
        by 5 to give the average period
        (duration) of a single vibration cycle.

    3.  <a name="question:2c"></a> Now that you
        know the period of a single cycle, work out the frequency
        (number of cycles per second) at this part of the vowel.

3.  Repeat the measurements in [question 2](#question:2)
    for the vowel in *it*.

4.  Are the frequencies that you calculated in the two vowels the same
    or different? Do the vowels sound the same or different? How so?
