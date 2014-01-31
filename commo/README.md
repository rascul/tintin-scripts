comms-logger
============

This is useful for logging all tells, yells, narrates, chats and speaks to a file. 
What makes it really useful is that you can set your terminal running tintin++ to 
be always on bottom, then make a smaller window, run `tailf .wotmud-comms` or
`tail -f .wotmud-comms` in the smaller window, and have a comms window. Comms will
be logged to .wotmud-comms.

NOTE: `#line log` is not functioning properly in tintin-2.00.9. Either use an older
version, or use the beta until 2.01.0 is released.
