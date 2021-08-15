#!/bin/ruby

require 'json'
require 'stringio'



#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#

require 'uri'
require 'net/http'

def getNumDraws(year)
    uri = URI('https://jsonmock.hackerrank.com/api/football_matches')
    params = {year: year, page: 1}

    
    draws = 0
    
    data = http_request(params, uri)
    puts "The type is: #{data.class}"
    puts "The data value is: #{get_draw_count(data["data"]).class}"
    draws += get_draw_count(data["data"])
    
    total_pages = data["total_pages"]
    
    current_page = 2
    
    while current_page <= total_pages
      puts "Now Processing page #{current_page}"
        params = {year: year, page: current_page}
        data = http_request(params, uri)
        puts "Page number in data = #{data["page"]}"
        unless data.nil?
            draws += get_draw_count(data["data"])
        end
        
        current_page += 1
    end
    
    puts "The output is: #{draws}"
    draws
end

def http_request(params, uri)
    uri.query = URI.encode_www_form(params)
    res = Net::HTTP.get_response(uri)

    return nil if !res.is_a?(Net::HTTPSuccess)
    
    JSON.parse(res.body)
end

def get_draw_count(matches)
    draws = 0

    return draws if matches.nil?
    
    matches.each do |match|
        if match["team1goals"] == match["team2goals"]
          puts match
            puts "current draw score is: #{draws}"
            draws += 1 
        end
    end
    
    draws
end

getNumDraws(2011)
