# Overview

Convert CC-CEDICT into a pleasantly-formatted StarDict/GoldenDict dictionary.

# Dependencies

- Python 2 (3 won't work, sadly)
- Stuff in requirements.txt
- Optionally, `dictzip` (might be part of `dictd` on your OS)

# Usage

    python2 conv.py path/to/cc-cedict path/to/output.ifo

Output path *must* end with `.ifo`; the other files will be created as siblings
of the given path. The directory it's in should already exist.

You'll get some import errors if you don't have one or two other packages
installed; they are safe to ignore as long as the program continues to run.

There's no terminal output, and it takes a while to run - be patient.

