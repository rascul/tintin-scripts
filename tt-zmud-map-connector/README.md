tt-zmud-map-connector
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
of the machine that is running mapd.py, if it's not localhost.

In zmud, connect to the ip that mapd.py is running on, port 2222 also.

When you connect to the mud from tintin++, you should be able to see
stuff in the zmud window as you're walking around. This is what is going
to drive the map.

Load up the map, and reconfigure it. Set the seconds of delay to 10 seconds
so you have time. When you hit next in the zmud map configuration window,
you'll have to go to tintin++ and hit whatever direction. Be sure you're in
a room where you can travel in that direction. Go through the screens,
ensuring the mapper has the room name, description and exits matched properly.

Go to the mapper, set your current position. The map should now follow you around.

When you flee, the map will automatically find where you fled to. Whenever
you hit look, the map will compare where you actually are to where it
thinks you are, if the map is off it will try and locate you. When you're
moving around, it simply moves in that direction.

There may be more interesting things coming in the future.
