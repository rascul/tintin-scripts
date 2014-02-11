rent
====

With this stuff you can keep track of what you have in rents.

You can't copy/paste this one. You have to do it like this: `#read rent.tin`

Set your character name like so:

`char <character name>`

Now you should create the database. You need sqlite3 installed, then do this from
the command line:

`sqlite3 wotmut.db < rent.sql`

Use a different name than wotmut.db if you want. If it's in a different path, set
that also:

`db /path/to/your.db`

There's two actions to capture the room names. If you're using the mapd stuff then
they're not necessary, but the priorities of the mapd actions are such that they
won't conflict or anything so you don't need to worry about it.

When you're at a rent location, just use the `list` command (or `lis` or `li`)
and the script will automagically figure out what's there and update the database
with the stuff.

