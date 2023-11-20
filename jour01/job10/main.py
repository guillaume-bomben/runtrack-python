init_inv = 10000
rend = 1.20

invest = init_inv * rend
gain = invest - init_inv

print( "gain : " + str(gain))

init_inv += 5000
rend += 0.02

invest = init_inv * rend
gain = invest - init_inv

print( "gain : " + str(gain))

init_inv *= 0.9
rend -= 0.01

invest = init_inv * rend
gain = invest - init_inv

print( "gain : " + str(gain))