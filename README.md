# scrape_n_spell
A system to scrape words off a production website and spellcheck them all. Because your site is already in production, and we don't really spellcheck code, do we?

<h2>Setup (for Linux-type comamnd-line environment)</h2>

<h3>Install pyenchant (required)</h3>

pip install pyenchant 

<h3>Install Lynx (if not already pre-installed)</h3>

brew install lynx

<h2>Usage</h2>

python scrape_n_spell.py OUTPUTFILENAME.TXT

Where "OUTPUTFILENAME" is the name of the text file where you want the results to be recorded.

* Designed for use on Linux-type command line systems. 
* Requires "lynx" command to be available at the command line.
* Uses the "Enchant" spellchecker library. https://www.abisource.com/projects/enchant/
* Uses "pyenchant", a Python integration of Enchant. https://github.com/rfk/pyenchant
