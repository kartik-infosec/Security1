#!/bin/bash

escape_json() {
  echo "$1" | \
  sed 's/\\/\\\\/g' | \
  sed 's/"/\\"/g' | \
  sed 's/\$/\\$/g' | \
  sed 's/\n/\\n/g' | \
  sed 's/\r/\\r/g' | \
  sed 's/\t/\\t/g' | \
  sed 's/\b/\\b/g' | \
  sed 's/\f/\\f/g' | \
  sed 's/\//\\\//g' | \
  sed 's/[[:cntrl:]]/\\u&/g' | \
  sed 's/[^[:print:]\t\n\r]/\\u&/g'  # Convert non-printable characters to Unicode escape sequences
}
