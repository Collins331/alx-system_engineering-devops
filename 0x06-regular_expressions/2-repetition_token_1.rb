#!/usr/bin/env ruby
# accepts one argument
pattern = /^hb?tn/
puts ARGV[0].scan(pattern).join