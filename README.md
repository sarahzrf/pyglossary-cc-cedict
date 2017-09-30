# Overview

Convert CC-CEDICT into a pleasantly-formatted dictionary (no longer hardcoded
to output GoldenDict!)

# Dependencies

- Python 3
- Jinja2 (installed as a Python 3 library)
- [PyGlossary](https://github.com/ilius/pyglossary)
- Optionally, `dictzip` (might be part of `dictd` on your OS)

# Usage

This is a PyGlossary plugin. To use it, simply clone this repository as a
subdirectory of the PyGlossary plugins directory and use PyGlossary normally
with this plugin and an (unzipped) copy of CC-CEDICT as the input.

For StarDict/GoldenDict, at least, compressing the output dictionary seems to
take a long time, so be patient—PyGlossary hasn't crashed. It may take up to 10
minutes—I don't know whether my case is representative. This is probably an
issue with something in the output logic, not with this plugin.

