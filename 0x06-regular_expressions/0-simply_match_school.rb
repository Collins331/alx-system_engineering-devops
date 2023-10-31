#!/usr/bin/env ruby
# scans '/School/' pattern in the argument used
pattern = /School/
puts ARGV[0].scan(pattern).join
