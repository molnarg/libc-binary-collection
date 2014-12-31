#!/bin/bash

for RELEASE in vivid utopic trusty saucy raring quantal precise oneiric natty maverick lucid karmic jaunty intrepid hardy gutsy feisty edgy dapper breezy hoary warty ; do
  for ARCH in amd64 arm64 armel armhf ia64 i386 ppc64el powerpc sparc ; do
    for PACKAGE in libc libc6-i386 ; do
      BASE_PATH="/ubuntu/$RELEASE/$ARCH/$PACKAGE"
      PAGE="https://launchpad.net$BASE_PATH"
      echo "$PAGE" >&2
      HTML=`curl -s "$PAGE"`

      for VERSION in `echo "$HTML" | grep "<a href=\"$BASE_PATH/[^\"]\+\">" | sed -e 's/^[^"]*"//g' -e 's/".*//g' | sort | uniq` ; do
	HTML=`curl -s "https://launchpad.net$VERSION"`
	echo "$HTML" | grep 'href="[^"]*.deb"' | sed -e 's/^.*href="//g' -e 's/".*//g'
      done
    done
  done
done
