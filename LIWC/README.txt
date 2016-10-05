#THESE ARE IMPORTANT STEPS BEFORE LIWC

Step 1: segmentation
* error somethimes happens - ChineseUtils.normalize warning: private use area codepoint U+e22a 
* preparation: copy the txt file into stanford-segmenter-2015-12-09/
$ cd stanford-segmenter-2015-12-09
$ ./segment.sh pku <inputfile> UTF-8 0 > <outputfile>

Step 2: remove (), tag, punctuations
* output file is empty if Simplified Chinese is used.
* preparation: copy the txt file into release_CKIP/input_dir/
* your output file is in output_dir

$ cd release_CKIP
$ ./ckip.sh input_dir output_dir
