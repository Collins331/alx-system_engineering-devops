#!/usr/bin/env ruby
# accepts one argument to scan
pattern = /^hbt+n/
puts ARGV[0].scan(pattern).join