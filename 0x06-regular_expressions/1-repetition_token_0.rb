#!/usr/bin/env ruby
#accepts one argument
pattern = /^hbt{2,5}n/

puts ARGV[0].scan(pattern).join