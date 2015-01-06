Libc binary collection
======================

```bash
$ ./identify.py printf=0x7ffff7a9f0d0 system=? | grep amd64
system=0x00007ffff7a90c70 debian/libc6_2.13-38+deb7u6_amd64/lib/x86_64-linux-gnu/libc-2.13.so
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
$ ./identify.py main_call_site=0x7f8f31a99ec5 printf=0x7f8f31acc2f0 system=? | grep ubuntu | sort
system=0x00007f8f31abe530 ubuntu/libc6_2.19-0ubuntu6.3_amd64/lib/x86_64-linux-gnu/libc-2.19.so
system=0x00007f8f31abe530 ubuntu/libc6_2.19-0ubuntu6.4_amd64/lib/x86_64-linux-gnu/libc-2.19.so
```

