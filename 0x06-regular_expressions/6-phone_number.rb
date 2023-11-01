#!/usr/bin/env ruby
pattern = /^\d{10}$/
puts ARGV[0].scan(pattern).join