# Paragraph shuffle
Simple program to shuffle text paragraphs.

## What does program do?
The program shuffles paragraphs found in file. Paragraphs are separated by
line containing only newline character. Paragraphs are detected and shuffled 
randomly into new file.

First, program reads file line by line and builds index containing 
beginnings and lenghts of paragraphs. This is done by placing the 
seek position and delta from file into list of pairs. For file to 
be shuffled efficiently, only index is shuffled and after that, index
is read item by item and in second pass shufflex text is assembled. 
This way i suppose really big files can be shuffled too. 

## Usage
`$ python parshuffle/main.py --input_file <PARAGRAPHS> \[--output_file <SHUFFLED>\]`

Use -h to print help about usage.

## Package
The code is structured into package, so one can use:

`$ python setup.py install`

After this, one can run parshuffle/main.py script. Also module is 
available for importing in code. 

```python
from parshuffle import shuffle_file
shuffle_file(input_fname, output_fname)
```

Consider using virtual environment for testing though.

