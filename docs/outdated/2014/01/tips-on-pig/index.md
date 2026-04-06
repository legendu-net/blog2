---
title: Tips on Pig
created: 2014-01-09 23:40:44
date: 2026-04-05 19:42:39.270001
authors:
- bendu
label: tips-on-pig
license: CC-BY-4.0
tags:
- programming
- big data
- Pig
- Hadoop
- tips
---
**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

 
## Tips

1. Pig uses `--` (at the beginning of lines) to comment out lines.
	It also support C-style comment, i.e., using `/* ... */`

2. Filter out records that you don't want before you do expensive transformations 
	such as joining, crossing, etc.

3. Pig uses single quotes instead of double quotes for strings.

4. prefer filtering and then joining rather than joining and then filtering

5. Use dot/period to access fields when use aggregation functions,
	otherwise, use double colons (::) to access fileds/columns.
	but this is wierd

6. -p or -param

## Common Mistakes

1. forget to assign relation to a name

2. use lower case of functions

3. use double quotes for strings
