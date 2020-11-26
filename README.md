# InstaInteract
Instagram commenting and liking bot. Supports commenting/liking recent posts on Instagram account(s).  

Setup and usage:  
- download mozilla firefox if not already installed (https://www.mozilla.org/en-US/firefox/download/thanks/)
- install dependencies (pip install -r requirements.txt)  
- fill out paramaters in config.py file (mandatory: credentials, accounts, comments)  
- change config.py settings to preferred values (all have defaults)  
- OPTIONAL: use generator.py to create large comment list (every permutation) from a word/phrase text file and a unicode emoji text file (see "Using generator.py" below)  
- run main.py  

Using generator.py (optional):  
- make 1 text file of words/phrases newline separated  
- make 1 text file of unicode emojis newline separated  
- fill in settings in main() function (words_file, emojis_file, max_emojis)  
- settings parameters:  
		words_file: user created .txt file of words/phrases newline separated  
		emojis_file: user created .txt file of unicode emojis newline separated  
		max_emojis: create every permutation of comment with 0 to max_emojis amount of emojis for each word/phrase  
- run generator.py and copy the outputted comment list directly to config.comments in config.py  

Raspberry Pi Setup (only if running on a raspberry pi):  
- VPN setup (https://support.surfshark.com/hc/en-us/articles/360013425373-How-to-set-up-Surfshark-VPN-on-Raspberry-Pi)  
- InstaPy setup (https://github.com/InstaPy/instapy-docs/blob/master/How_Tos/How_to_Raspberry.md)  