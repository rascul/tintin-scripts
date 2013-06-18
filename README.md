tintin-scripts
==============

This is my collection of tintin++ scripts for WoTMUD.

If you desire to use any of them, put them in your tintin++ script file. 
Pasting them into tintin++ manually won't have the desired effect. Awhile back
tintin++ changed the formatting of the script files to some multi line kinda
deal to make it nicer on the eyes. Unfortunately, we can only paste the single
line stuff into a running tintin++. So the best thing to do is to clone the repo,
then you can `#read` whichever scripts you want into your running tintin++, then
when you `#write` to save your script, they'll be saved with it.

If you're having issues with colors or `#highlight` then set packet patch to something: 
`#config {packet patch} {.17}` Mess around with it until you find the number you like.

`#line` has some issues with tintin-2.00.9, either use 2.00.8 or 2.01.0 beta 
for now if you need `#line` to function properly.
