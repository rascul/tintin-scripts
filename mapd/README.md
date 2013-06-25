mapd
=====================
This is a connector. Allows you to use tintin++ on linux to mud, and
connect with zmud to use a map in zmud's mapper and have it follow you
around, while still mudding from tintin++.

NOTE: This is a work in progress.

python-twisted is required.

First thing to do, load up the tintin++ script. Also, run mapd.py as follows:

`twistd -y mapd.py`

Then you'll need to load up zmud with the zmud script. This can be on the
same computer in a virtual machine, or another computer. As long as both
machines (physical or virtual) can connect to mapd.py.

In tintin++, `#session mapd localhost 2222`, replacing localhost with the ip
or hostname of the machine that is running mapd.py, if it's not localhost.

In zmud, connect to the ip or hostname that mapd.py is running on, port 2222 also.

When you connect to the mud from tintin++, you should be able to see
stuff in the zmud window as you're walking around. This is what is going
to drive the map.

Go to the mapper, set your current position. Or use the `findme` alias. The map 
should now follow you around.

When you flee, the map will automatically find where you fled to. If the map gets
lost and confused, use the `findme` alias. When you're moving around, it simply 
moves in that direction.

Sometimes (haven't got this figured out yet) the stack of commands for the map
will get backed up. `mapstack` to view the stack, and if there's still stuff
there and you're no longer moving, `clearstack` to clear it. `findme` afterwards
is probably a good idea because at this point the map probably doesn't realize
where you are.

There may be more interesting things coming in the future.
