#### _Speech Processing 2020: PHON_

# Tutorial B: Week 1 - PHON

1. With the aid of an IPA chart, fill in the following table: 


| Phonetic description        	| IPA Symbol 	|
|:-----------------------------	|:------------:	|
| Voiceless bilabial stop     	|            	|
|                             	| ɣ          	|
| Voiceless dental fricative  	|            	|
| Close front rounded vowel   	|            	|
|                             	| j          	|
|                             	| ɯ          	|
| Open-mid back rounded vowel 	|            	|

2. Using IPA symbols, write out your pronunciation of the following words on paper: 

    a. Hello  <br/>
    b. World <br/>
    c. Screech <br/>
    d. And <br/>
    e. Languish <br/>
    f. Protesting <br/>
    g. Language<br/>

3. How do your IPA transcriptions differ from those in the Cambridge dictionary? 
    * Search here: https://dictionary.cambridge.org/dictionary/english/  
  
    Why do they differ? 

 

4. Transliterate your IPA transcriptions with the following phonesets (use the mapping in the appendix): 

    a. ARPAbet<br/>
    b. Unisyn 

5. We will use ARPAbet and Unisyn in Festival. Familiarise yourself with the [unilex_phones.scm](https://laic.github.io/uoe_speech_processing_course/phon/tutorial1/unilex_phones.scm) file. You will need to open this in a text editor such as Atom (or view it [here on github](https://github.com/laic/uoe_speech_processing_course/blob/master/phon/tutorial1/unilex_phones.scm)).  Uni**lex** is a lexicon based on the uni**syn** database. Can you tell how the `defPhoneSet` function encodes phonetic dimensions? 

 

6. Download (or find in your repository) the following English wav  files:

    * [hvd_001.wav](https://laic.github.io/uoe_speech_processing_course/phon/tutorial1/eng_wavs/hvd_001.wav)
    * [hvd_002.wav](https://laic.github.io/uoe_speech_processing_course/phon/tutorial1/eng_wavs/hvd_002.wav)
    * [LJ027-0094.wav](https://laic.github.io/uoe_speech_processing_course/phon/tutorial1/eng_wavs/LJ027-0094.wav)
    * [sa1.wav](https://laic.github.io/uoe_speech_processing_course/phon/tutorial1/eng_wavs/sa1.wav)

    Then, use this automatic IPA transcriber:
    https://www.dictate.app/phone - Choose the appropriate language from the list on the left, then drag and drop the audio file into the transcriber window. 

    a. Without listening to the English audio files, can you guess the words from the phones? 
  
    b. Can you find any errors in the IPA transcription? Write down the corrections. 



7. Download the following file: 

   * [japhug-clip.wav](https://laic.github.io/uoe_speech_processing_course/phon/tutorial1/Japhug_clip.wav)
   
   a. Transcribe the Japhug clip: Select Japhug from the list of languages, and then drag and drop the file into the transcriber window. 
  
   b. Compare the gold IPA transcription below to that produced by the automatic transcriber. 
   
      <blockquote>
         qale cʰo tɤŋe kɤ-ti ɲɯ-ŋu. kɯɕɯŋgɯ tɕe, iɕqʰa 
      </blockquote>

   c. Could you use this tool to create a lexicon (pronunciation dictionary) for an unseen language? What difficulties might you face? How would you measure transcription accuracy? 

----
### Appendix - Approximate mappings across phonesets: 

 

| IPA    | Keyword    | ARPAbet | Unilex | Combilex |
|--------|------------|---------|--------|----------|
| ə      | COMMA      |      ax |   @    |  @       |
|æ / a   |TRAP   | ae   | a   | a |
|ɑː    |PALM   | aa |   aa  |  A |
|aɪ  |  PRICE   | ay  |  ai  |  aI |
|b  |  BAT       | b  |  b  |  b |
|ʧ  |  CHAT    | ch   | ch  |  tS |
|d  |  DAB     |   d   | d |   d |
|ð  |  THAT |   dh  |  dh  |  D |
|ɛ  |  DRESS |   eh   | e   | E |
|ɛɪ   | WAIST |   ey  |  ei|    eI |
|f  |  FAT    |    f |   f|    f |
|g |   GAP |       g  |  g |   g |
|h  |  HAT   |     hh  |  h  |  h |
|ʍ   | WHACK   | w  |  hw |   W |
|ɪ  |  KIT   | ih   | i  |  I |
|iː  |  FLEECE  |  iy |   ii  |  i |
|ʤ  |  JAB      |  jh   | jh |   dZ |
|k  |  CAT   |     k   | k  |  k |
|l   | LAD    |    l |   l  |  l |
|l̩  |  CATTLE |  el   | l=   | l= |
|ɫ  |  FEEL  |  l |   lw  |  5 |
|m   | MAT     |   m |   m   | m |
|m̩  |  SPASM   | em   | m=  |  m= |
|n  |  NAP  |      n   | n |   n |
|n̩   | GARDEN   | en   | n= |   n= |
|ŋ  |  PANG    |ng |   ng   | N |
|ɔɪ   | CHOICE |   oy  |  oi |   OI |
|ɒ  |  LOT      |   oh|    Q |   Q |
|ɔː  |  THOUGHT   | ao  |  oo   | O |
|aʊ  |  MOUTH  |  aw   | ow |   aU |
|əʊ  |  GOAT  |  ow  |  ou |   @U |
|p  |  PAT     |   p  |  p  |  p |
|ɹ  |  RAT      |  r  |  r   | r |
|ə  |  LETTER   | axr   | @r |   |
|s  |  SAT      |  s  |  s |   s |
|ʃ  |  SHAM |   sh  |  sh |   S |
|t  |  TAT |      t  |  t  |  t |
|ɾ   | BUTTER   | t |   t^  |  4 |
|θ   | MATH   | th |   th |   T |
|ʊ   | FOOT  |  uh  |  u |   U |
|ʌ    |STRUT |  ah  |  uh |   V |
|uː  |  GOOSE |   uw  |  uu |   u |
|v   | VAT     |   v  |  v |   v |
|w   | WAG     |   w  |  w   | w |
|j   | YAP      |  y  |  y  |  j |
|z   | ZAP     |   z  | z  |  z |
|ʒ   | BEIGE  |  zh  |  zh |   Z |


```python

```
