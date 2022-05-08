# DVD Creation
This directory is dedicated to all the scripts I use to create and burn DVDs on Windows.

## `avisynth_dvd_writer.py`
This script was written to burn home videos to DVD. The camera used to record the videos created a 
new directory for each calendar day. We want the DVD to have a chapter for each day. So, this script
generates a DVD-ready video for each day. It uses AviSynth and ffmpeg to condense every video in its
running directory into a single, new video file, encoded in the proper format for DVD. 

As currently implemented, it combs the directory for `.MOD` and `.mpg` files (the `extensions` list 
in `main()` can easily be appended), sorts them by date modified to ensure chronological order in 
the final video, and generates a `.avs` and `.bat` file.

### Output files
* `directory_name.avs`: the AviSynth script which concatenates all videos in the directory
* `directory_name.bat`: contains the ffmpeg command to encode the `.avs` file in the correct format
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
3. Run the generated `.bat` file.

### Example
In a directory named `video_example` with the following contents:
```
MOV041.MOD
MOV042.MOD
MOV043.MOD
MOV044.MOD
MOV045.MOD
```
Placing `avisynth_dvd_writer.py` into the directory and running it with the command
`python3 avisynth_dvd_writer.py` will create two new files:
```bash
video_example.avs
video_example.bat
```
Running `video_example.bat` will execute ffmpeg to encode `video_example.avs`, and will pause the 
terminal window on completion so the output can be read.