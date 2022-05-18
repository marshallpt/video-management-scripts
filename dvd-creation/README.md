# DVD Creation
This directory is dedicated to all the scripts I use to create and burn DVDs on Windows.

## `avisynth_dvd_writer.py`
This script was written to burn home videos to DVD. We want the DVD to have a chapter for each day. 
So, this script generates a DVD-ready video for each day. It uses AviSynth and ffmpeg to condense 
videos in its running directory into a video for each day, encoded in the proper format for DVD. 

As currently implemented, it combs the directory for `.MOD` and `.mpg` files (the `extensions` list 
in `main()` can easily be appended), sorts them by date modified to ensure chronological order, 
splits them into sub-lists by date, generates a `.avs` file for each day, and generates 
`encode_me.bat` file to encode them all.

### Output files
* `MM-DD-YYYY.avs`: the AviSynth script which concatenates videos recorded on MM-DD-YYYY
* `encode_me.bat`: contains the ffmpeg command to encode all `.avs` files in the correct format
for DVD burning

### Pre-requisites
1. [AviSynth+](https://avs-plus.net/) (Can also use the original [AviSynth](http://www.avisynth.org/),
but not advised. 
[Excellent summary](https://video.stackexchange.com/questions/28548/avisynth-vs-avisynth-vs-vapoursynth-which-one-should-i-choose)
of the differences.)
2. [ffmpeg](https://ffmpeg.org/)
3. [FFMS2](https://github.com/FFMS/ffms2/): ffmpeg plugin for AviSynth

### Usage
1. Drop the script into the directory of videos to condense.
2. Run the script.
3. Run `encode_me.bat` file.

### Example
In a directory named `video_example` with the following contents:
```
NAME       | DATE MODIFIED
-------------------------- 
MOV004.MOD | 9-28-2013
MOV005.MOD | 9-28-2013
MOV006.MOD | 9-28-2013
MOV007.MOD | 9-28-2013
MOV008.MOD | 10-22-2013
MOV009.MOD | 11-2-2013
MOV00A.MOD | 11-2-2013
MOV00B.MOD | 11-2-2013
MOV00C.MOD | 11-2-2013
```
Placing `avisynth_dvd_writer.py` into `video_example` and running it with the command
`python3 avisynth_dvd_writer.py` will create the following files:
```bash
9-28-2013.avs
10-22-2013.avs
11-2-2013.avs
encode_me.bat
```
Running `encode_me.bat` will execute ffmpeg to encode all the `.avs` files, and will pause the 
terminal window on completion so the output can be read.