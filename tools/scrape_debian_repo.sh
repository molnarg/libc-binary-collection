#!/bin/bash

BASE_URL="$1"

scrape_dir() {
  local URL="$1"
  echo "Scraping $URL" 1>&2

  HTML="`curl -s "$URL"`"
  for DEB in `echo "$HTML" | grep '.deb">' | grep 'libc[0-9.]*_' | sed -e 's/.*href="//g' -e 's/".*//g'` ; do
    echo "${URL}${DEB}"
  done
  
  for FOLDER in `echo "$HTML" | grep 'alt="\[DIR\]"' | grep -v 'Parent Directory' | sed -e 's/.*href="//g' -e 's/".*//g'` ; do
    if [[ ! "$URL" =~ /pool/[^/]*/[^/]*/ || "$FOLDER" =~ 'libc' ]] ; then
      scrape_dir "${URL}${FOLDER}"
    fi
  done
}

scrape_dir "$BASE_URL"

