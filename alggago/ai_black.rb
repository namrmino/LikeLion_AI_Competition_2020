require "xmlrpc/server"
require "socket"

s = XMLRPC::Server.new(ARGV[0])
MAX_NUMBER = 16000

class MyAlggago
  def calculate(positions)

    #Codes here
    
    #Insert Your Codes here
  





    #Return values
    message = get_name
    stone_number = current_stone_number
    stone_x_strength = x_length * 5
    stone_y_strength = y_length * 5
    return [stone_number, stone_x_strength, stone_y_strength, message]

    #Codes end
  end

  def get_name
    "MY AI!!!" #Set your name or team name
  end
end

s.add_handler("alggago", MyAlggago.new)
s.serve
