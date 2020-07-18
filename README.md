# glossary
python script that solves your task   (glossaries)

the script connects to wikipedia and downloads the meanings or definitions of the words you want to search for, allows you to choose the language and the number of paragraphs to use.

## dependencies

**python2.X**

    pip install wikipedia

**python3.X**

    pip3 install wikipedia

## Use

In this section of the script add the words to search following the pattern of single quotes and commas at the end of each

    vocabulario = [
		'Palabra1',
		'Palabra2',
		'Palabra3'
	]

in case you put words like `'disc'` which has a lot of definitions you'll make a error...
this error is fixed by defining the type of disk you need 
E.g. 'Hard Drive', 'Disk Music'.

everything will be saved in a plain text file which will contain the word with its respective definition.
