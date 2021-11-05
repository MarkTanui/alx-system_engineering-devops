#!/usr/bin/env ruby
puts ARGV[0].scan(/(\+?\d{8,}|\-1\b:\d\b:\-?\d\b:\-?\d\b:\-?\d)/).join(",")
