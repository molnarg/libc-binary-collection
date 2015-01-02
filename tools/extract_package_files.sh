#!/bin/bash

# Argument handling and help
PACKAGE="$1"
PATTERN="$2"
if [[ -z "$PACKAGE" || -z "$PATTERN" ]] ; then
  echo "Overview: A tool to extract specific files from Linux packages."
  echo "          The extracted files will be put under the DISTRO/PACKAGE_CANONICAL_NAME/"
  echo "          directory within subdirectories corresponding to the absolute path"
  echo "          of the files in the package."
  echo
  echo "Usage: $0 package_file file_pattern"
  echo
  echo "Example: $ $0 ./libc6_2.11.1-0ubuntu7.19_amd64.deb '*libc[^a-zA-Z]*so*'"
  echo "         ubuntu/libc6_2.19-0ubuntu6.4_amd64/lib/x86_64-linux-gnu/libc-2.19.so"
  exit
fi
PACKAGE="$(`which greadlink || which readlink` -f "$PACKAGE")"
if [[ ! "`file "$PACKAGE"`" =~ 'Debian binary package' ]] ; then
  echo 'This is not a Debian/Ubuntu package. Currently, only this package format is supported.'
  exit
fi

# Temp dir and error handling
pushd . >/dev/null
TEMP="`mktemp -d tmp-XXXXX`"
set -e
trap cleanup 0 2
cleanup() {
  popd >/dev/null
  rm -rf $TEMP
}

# Unpack the package and read metadata
cd $TEMP
ar x "$PACKAGE"
tar -xzf data.tar.*
tar -xzf control.tar.*
PACKAGE=`grep -i '^Package: ' control | sed 's/[^:]*: //g'`
VERSION=`grep -i '^Version: ' control | sed 's/[^:]*: //g'`
ARCHITECTURE=`grep -i '^Architecture: ' control | sed 's/[^:]*: //g'`
DISTRO=`if [[ "$VERSION" =~ ubuntu ]] ; then echo ubuntu ; else echo debian ; fi`
TARGET_DIR="${DISTRO}/${PACKAGE}_${VERSION}_${ARCHITECTURE}"
cd ..

# Find and move files
for F in `(cd $TEMP; find . -name "$PATTERN")` ; do
  DIR="$TARGET_DIR/`dirname "$F" | sed 's|^./||g'`"
  mkdir -p "$DIR"
  mv "$TEMP/$F" "$DIR/"
  echo "$DIR/`basename "$F"`"
done

