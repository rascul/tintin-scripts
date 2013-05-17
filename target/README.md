target
======

Targeting script. Set your targets manually, then use macros and aliases to
kill them. Here's how it works:

The variable $target may be overwritten by the aliases and macros, it's more or
less just the current target. You may set $target with the `target` alias.
There are four main targets. Set them with `t1`, `t2`, `t3` and `t4`.

To kill targets, there are two options. The first is with aliases. The aliases
`k1`, `k2`, `k3` and `k4` will kill the respective targets, and also set $target
to whichever one you're attempting to kill. The alias `kk` will kill the current
target. All five of the aliases will accept specific targets, ie `kk 4` will kill
4.$target and `k2 3` will kill 3.$target2.

There are also macros. The ~ key will kill the current target, and the keys F1
through F4 kill their respective targets and set the current target. It's possible 
that the macros may not work properly on your system, in that case simply remove 
them so they don't mess you up.
