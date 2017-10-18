# nprSongOTD
This script will download all the songs of the day released by KEXP

More Info on the KEXP song of the day podcast. 
http://kexp.org/podcasts#song


## Table of Contents

1. Overview
2. Installation
3. Usage

## Overview

This is a scripts to aid in downloading songs from the KEXP song of the day. The script logs the songs it has downloaded to a text file (data.txt) to insure it doesnt download duplicates. Songs will be downloaded into a 'songs' subfolder. 

## Installation

*Please note these scripts have only been tested on Windows 10 running Python 3.6*

### Prerequisites

You will require:
* Python 3 https://www.python.org/downloads/
* urllib
* Re
* Os

These modules come preinstalled with Python 3.

## Usage

1. Copy the script files into the folder you wish for the music to be downloaded into.
2. Ensure you have write permission in that folder.
3. Run 'nprsongotd.py', this will create a list of songs and download them.
4. Use scheduled task or chrontab to schedule this to run daily to keep up to date.
