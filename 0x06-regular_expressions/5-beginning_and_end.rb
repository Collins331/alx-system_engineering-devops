#!/usr/bin/env ruby
# accepts one argument
pattern = /^h.n$/
puts ARGV[0].scan(pattern).join