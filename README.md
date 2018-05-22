# scrape_n_spell
A system to scrape words off a production website and spellcheck them all.

<h2>Usage</h2>

python scrape_n_spell.py OUTPUTFILENAME

Where "OUTPUTFILENAME" is the name of the text file where you want the results to be recorded.

* Designed for use on Linux-type systems. 
* Requires "lynx" command to be available at the command line.
* Uses the "Enchant" spellcheck library. https://www.abisource.com/projects/enchant/
* Also uses "pyenchant", python integration of Enchant. https://github.com/rfk/pyenchant
