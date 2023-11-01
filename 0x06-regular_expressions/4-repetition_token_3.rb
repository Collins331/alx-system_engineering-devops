#!/usr/bin/env ruby
# accepts one argument
pattern = /^hb[^o]?t*n/
puts ARGV[0].scan(pattern).join