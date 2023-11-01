#!/usr/bin/env ruby
# accepts one argument
pattern = /^hbt*n/
puts ARGV[0].scan(pattern).join