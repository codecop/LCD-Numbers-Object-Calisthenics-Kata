[
  'numbers grid 3x5 - size 1.txt',
  'numbers grid 4x7 - size 2.txt',
  'numbers grid 5x9 - size 3.txt',
].each do |file|

  file =~ /size (\d)\./
  size = $1.to_i
  
  dir = "size_#{size.to_s}"
  Dir.mkdir(dir) unless File.exist? dir
  
  0.upto(9) do |digit|
    lcd = IO.readlines(file).map { |line|
      width = 2 + size
      column = width * digit
      line[column...(column + width)]
    }.map { |line| line + "\n" }
  
    number = (digit + 1) % 10
    File.open("#{dir}/number #{number.to_s}.txt", 'w') { |f|
      lcd.each { |line| f.write(line) }
    }
  end
end
