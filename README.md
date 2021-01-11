# SelteneWoerter
Finds the rarest words in the EasyGerman podcast. 

Build off of https://github.com/marcomzp/easygerman.

This script scans all transcipts of the [Easy German Podcast]('https://www.easygerman.org/podcast') in the current directory. It uses the frequency table produced by [marcomzp's script]('https://github.com/marcomzp/easygerman') to save all of the _n_ rare words of each transcipt to a text file under the file format of egp\<PodcastNum\>_selteneWörter.txt. 

Here is a sample of the output:
```
$ python3 ./rare_finder.py 2
Top 2 seltene Wörter in egp1: ['zusammengekommen', 'soak']

$ python3 ./rare_finder.py 10
Top 10 seltene Wörter in egp1: ['zusammengekommen', 'soak', 'weils', 'brain', 'abbiegen', 'umgebt', 'keniaoder', 'textilarbeiter', 'begleitest', 'fahrradunfällen']

$ python3 ./rare_finder.py
Top 20 seltene Wörter in egp1: ['zusammengekommen', 'soak', 'weils', 'brain', 'abbiegen', 'umgebt', 'keniaoder', 'textilarbeiter', 'begleitest', 'fahrradunfällen', 'verinnerlicht', 'aufschnappe', 'drauflos', 'anklicken', 'plappern', 'verlor', 'leonora', 'dokumentarfilmen', 'schulz', 'keks']
```