Libc binary collection
======================

A collection of binary libc releases from various distributions. Mainly useful for identifying
the exact libc version running on a remote Linux host in an exploitation process based on
leaked pointers.

```bash
$ ./identify.py printf=0x7ffff7a9f0d0 | grep amd64
debian/libc6_2.13-38+deb7u6_amd64/lib/x86_64-linux-gnu/libc-2.13.so

$ ./identify.py main_call_site=0x7f8f31a99ec5 system=? | grep ubuntu | sort
system=0x00007f8f31abcb30 ubuntu/libc6_2.19-10ubuntu1_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abcb30 ubuntu/libc6_2.19-10ubuntu2.1_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abcb30 ubuntu/libc6_2.19-10ubuntu2_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abcc40 ubuntu/libc6_2.19-10ubuntu2.2_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abcc40 ubuntu/libc6_2.19-13ubuntu2_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abcc40 ubuntu/libc6_2.19-13ubuntu3_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abcf50 ubuntu/libc6_2.19-4ubuntu1_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abcf50 ubuntu/libc6_2.19-4ubuntu2_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abe530 ubuntu/libc6_2.19-0ubuntu6.3_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abe530 ubuntu/libc6_2.19-0ubuntu6.4_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abe640 ubuntu/libc6_2.19-0ubuntu6.5_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abe8f0 ubuntu/libc6_2.19-0ubuntu1_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abe8f0 ubuntu/libc6_2.19-0ubuntu2_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abe8f0 ubuntu/libc6_2.19-0ubuntu3_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abe8f0 ubuntu/libc6_2.19-0ubuntu4_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abe8f0 ubuntu/libc6_2.19-0ubuntu5_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abe8f0 ubuntu/libc6_2.19-0ubuntu6_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abe900 ubuntu/libc6_2.19-0ubuntu6.1_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abe900 ubuntu/libc6_2.19-0ubuntu6.2_amd64/lib/x86_64-linux-gnu/libc-2.19.so

$ ./identify.py main_call_site=0x7f8f31a99ec5 printf=0x7f8f31acc2f0 system=?
system=0x00007f8f31abe530 ubuntu/libc6_2.19-0ubuntu6.3_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abe530 ubuntu/libc6_2.19-0ubuntu6.4_amd64/lib/x86_64-linux-gnu/libc-2.19.so

$ wget http://gabor.molnar.es/libc/ubuntu/libc6_2.19-0ubuntu6.3_amd64/lib/x86_64-linux-gnu/libc-2.19.so
```

How does it work?
-----------------

The last 12 bits of the addresses are constant even when using ASLR (because of the alignment to page
boundary). These can be used to fingerprint the used libc version. When multiple symbols are specified,
the difference between symbols are also used for fingerprinting.

Symbols
-------

All dynamic symbols were extracted from the libc.so files. Besides this, there's a special symbol
called `main_call_site` which is the call site where the libc calls back the main function. This
is extracted dynamically, and only available for certain libc releases. If you specify this symbol
on the command line, you'll only get results where this symbol is defined. This useful when it is
possible to leak addresses from the stack since this address is always there.

Libc versions in this collection
--------------------------------

The collection is far from complete. Current files are from [Ubuntu Launchpad](https://launchpad.net/ubuntu/)
and [archive.debian.org](http://archive.debian.org/). There are currently 1293 different libc builds in
this repo. Feel free to contribute missing versions.

License
-------

The MIT License

Copyright (C) 2014 Gábor Molnár <gabor@molnar.es>

