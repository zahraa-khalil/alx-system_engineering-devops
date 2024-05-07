#!/usr/bin/env ruby
# A regular expression that is simply matching pattern
puts ARGV[0].scan(/^[0-9]{10}$/).join
