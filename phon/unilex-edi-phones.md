
 ## Unilex Edinburgh phone features

This table is a summary of information from the file `unilex_phones.scm` which comes with the unilex Edinburgh dictionary in Festival and the actual Unisyn/Unilex documentation (see: https://speech.zone/forums/topic/dictionaries-used-by-festival/).  Also see the following paper for a description of Unilex. 

Fitt, S., Isard, S. (1999) Synthesis of regional English using a keyword lexicon. Proc. 6th European Conference on Speech Communication and Technology, 823-826, doi: 10.21437/Eurospeech.1999-213

The unilex keysymbol in the leftmost column is the general 'keysymbol' for the unilex dictionary.  These symbols are associated with specific keywords.  We then use rules to map accent specific pronunications.  So, in some cases different phones are merged in the Edinburgh pronunciation (e.g. several vowels get mapped to [a]) - see the "Edinburgh mapping" column.  

I've also given the equivalent IPA symbol for the Edinburgh phone as given in Unisyn/Unilex documentation. This varies between accents though, so you might see a different unilex phone symbol (and corresponding IPA symbol) for Welsh English, for example, for the keywords listed below.  


| unilex keysymbol | keyword | vowel(+) or consonant(-)? | vowel length | vowel height |  vowel frontness  |  vowel rounding |  consonant type |  consonant place  | consonant voicing | Edinburgh mapping | IPA | 
|-----------|----| ----|---|----|----|----|----|-----|---|---|---|
|p | **p**ea| - | 0 | 0 | 0 | 0 | stop | labial | - | p | p | 
| t | **t**ea | - | 0 | 0 | 0 | 0 | stop | alveolar | - | t | t |
| ? | ca**t**| - | 0 | 0 | 0 | 0 | stop | glottal | + | ? | ʔ |   
| t^ | me**rr**y | - | 0 | 0 | 0 | 0 | tap | alveolar | + | t^ | ɾ | 
| k | **k**ey | - | 0 | 0 | 0 | 0 | stop | velar | - | k | k| 
| x | lo**ch**| - | 0 | 0 | 0 | 0 | fricative | velar | - | x | x| 
| b | **b**ee | - | 0 | 0 | 0 | 0 | stop | labial | + | b | b| 
| d | **d**ye | - | 0 | 0 | 0 | 0 | stop | alveolar | + | d | d | 
| g | **g**uy | - | 0 | 0 | 0 | 0 | stop | velar | + | g | g | 
| ch | ea**ch** | - | 0 | 0 | 0 | 0 | affricate | palatal | - | ch | ʧ |
| jh | e**dg**e| - | 0 | 0 | 0 | 0 | affricate | palatal | + | jh | ʤ | 
| s | **s**ea | - | 0 | 0 | 0 | 0 | fricative | alveolar | - | s | s | 
| z | **z**oom |  - | 0 | 0 | 0 | 0 | fricative | alveolar | + | z | z | 
| sh | **sh**e  |  - | 0 | 0 | 0 | 0 | fricative | palatal | - | sh | ʃ |
| zh | bei**g**e| - | 0 | 0 | 0 | 0 | fricative | palatal | + | zh | ʒ | 
| f | **f**an | - | 0 | 0 | 0 | 0 | fricative | labio-dental | - | f | f| 
| v | **v**an | - | 0 | 0 | 0 | 0 | fricative | labio-dental | + | v | v | 
| th | **th**in |- | 0 | 0 | 0 | 0 | fricative | dental | - | th | θ |
| dh | **th**en |- | 0 | 0 | 0 | 0 | fricative | dental | + | dh | ð | 
| h | **h**at | - | 0 | 0 | 0 | 0 | fricative | 0 | - |  h | h | 
| m | **m**e | - | 0 | 0 | 0 | 0 | nasal | labial | + | m | m | 
| m! | chas**m** | - | 0 | 0 | 0 | 0 | nasal | labial | + | m! | m̩  |  
| n | **kn**ee | - | 0 | 0 | 0 | 0 | nasal | alveolar | + | n | n |  
| n! | missio**n** | - | 0 | 0 | 0 | 0 | nasal | alveolar | + | n! | n̩ |  
| ng | so**ng** | - | 0 | 0 | 0 | 0 | nasal | velar | + | ng | ŋ | 
| l | **l**ay | - | 0 | 0 | 0 | 0 | approximant | alveolar | + | l | ɫ  | 
| ll | **Ll**andudno | - | 0 | 0 | 0 | 0 | approximant | alveolar | + |l | ɫ  | 
| l! | catt**le** | - | 0 | 0 | 0 | 0 | approximant | alveolar | + | l! | l̩ | 
| r | **r**ay |  - | 0 | 0 | 0 | 0 | approximant | alveolar | + | r $\rightarrow$ t^ | ɹ $\rightarrow$ ɾ | 
| y | **y**es |         - | 0 | 0 | 0 | 0 | liquid | palatal | + | y | j | 
| w | **w**itch | - | 0 | 0 | 0 | 0 | liquid | labial | + | w | w | 
| hw | **wh**ich  | - | 0 | 0 | 0 | 0 | liquid | labial | + | hw | ʍ | 
| e | dr**e**ss | + | short | mid | front | -  | 0 | 0 | 0 | e | ɛ | 
| ao | M**a**zda | + | short | low | front | -  | 0 | 0 | 0 | a | a | 
| a | tr**a**p | + | short | low | front | -  | 0 | 0 | 0 | a  | a |
| ah | b**a**th | + | short | low | front | -  | 0 | 0 | 0 | a  | a |
| oa | ban**a**na | + | short | low | front | -  | 0 | 0 | 0 | a  | a |
| aa | p**a**lm | + | short | low | front | -  | 0 | 0 | 0 | a | a |
| ar | st**ar**t | + | short | low | front | -  | 0 | 0 | 0 | ar |  a<sup>ɹ</sup> |
| ou | g**oa**t | + | diphthong | mid | back | +  | 0 | 0 | 0 | ou | o | 
| ouw | kn**ow** | + | diphthong | mid | back | +  | 0 | 0 | 0 | ou | o | 
| oou | adi**o**s | + | long | low | back | +  | 0 | 0 | 0 |  oo | ɔ | 
| o | l**o**t | + | long | low | back | +  | 0 | 0 | 0 | oo | ɔ | 
| au | cl**o**th | + | long | low | back | +  | 0 | 0 | 0 | oo | ɔ |  
| oo | th**oug**ht | + | long | low | back | +  | 0 | 0 | 0 | oo | ɔ | 
| or | n**or**th |+ | long | low | back | +  | 0 | 0 | 0 | or | ɔɹ | 
| our | f**or**ce | + | diphthong | mid | back | +  | 0 | 0 | 0 | our | o<sup>ɹ</sup> |
| ii | fl**ee**ce | + | long | high | front | -  | 0 | 0 | 0 | ii | i | 
| iy | happ**y** | + | long | high | front | -  | 0 | 0 | 0 | iy | i | 
| i | k**i**t | + | short | high | front | -  | 0 | 0 | 0 | i | ɪ | 
| iii | agr**ee**d | + | short | high | front | -  | 0 | 0 | 0 | iii | i: | 
| @r | lett**e**r | + | schwa | mid | mid | -  | r | a | + | @r | ə<sup>ɹ</sup>  | 
| @ | comm**a** | + | schwa | mid | mid | -  | 0 | 0 | 0 | @ | ə | 
| uh | str**u**t | + | short | mid | mid | -  | 0 | 0 | 0 | uh | ʌ | 
| u | f**oo**t | + | long | high | back | +  | 0 | 0 | 0 | uu | ʉ | 
| uu | g**oo**se | + | long | high | back | +  | 0 | 0 | 0 | uu | ʉ | 
| iu | bl**ew** | + | long | high | back | +  | 0 | 0 | 0 | uu | ʉ |
| uuu | br**e**wed | + | long | high | back | +  | 0 | 0 | 0 | uuu | ʉ: |
| ei | w**ai**st | + | diphthong | mid | front | -  | 0 | 0 | 0 | ei | e |  
| ee | w**a**ste | + | diphthong | mid | front | -  | 0 | 0 | 0 | ei | e | 
| ai | pr**i**ce | + | diphthong | low | mid | -  | 0 | 0 | 0 | ai |  ʌi | 
| ae | t**ie**d | + | diphthong | low | mid | -  | 0 | 0 | 0 | ae | ae | 
| aer | f**i**re | + | diphthong | low | mid | -  | 0 | 0 | 0 |  aer | ae<sup>ɹ</sup>  |  
| oi | ch**oi**ce | + | diphthong | mid | back | +  | 0 | 0 | 0 | oi | ɔɪ| 
| oir | c**oi**r | + | diphthong | mid | back | +  | 0 | 0 | 0 | oir |  ɔɪ<sup>ɹ</sup>  | 
| ow | m**ou**th | + | diphthong | low | mid | -  | 0 | 0 | 0 | ow |  ʌʊ |
| owr | h**ou**r |  + | diphthong | low | mid | -  | 0 | 0 | 0 | owr |  ʌʊ<sup>ɹ</sup>  | 
| ir | z**e**ro | + | short | high | front | -  | 0 | 0 | 0 | ir | i<sup>ɹ</sup>  |
| irr | n**ea**r |  + | short | high | front | -  | 0 | 0 | 0 | irr | iː<sup>ɹ</sup>  | 
| @@r | n**u**rse | + | schwa | mid | mid | -  | 0 | 0 | 0 | @@r | ɜ<sup>ɹ</sup>  |
| er | p**e**rt | + | short | mid | front | -  | 0 | 0 | 0 | er | ɛ<sup>ɹ</sup>  | 
| eir | squ**a**ring | + | short | mid | front | -  | 0 | 0 | 0 | eir |  e<sup>ɹ</sup>  | 
| ur | j**u**ry |  + | short | high | back | +  | 0 | 0 | 0 |   ur | ʉ<sup>ɹ</sup>  | 
| urr | c**u**re |  + | short | high | back | +  | 0 | 0 | 0 |  urr |  ʉ:<sup>ɹ</sup>  | 

