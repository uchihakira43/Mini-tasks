def control_loop(x):
  if x < 0:
    return False
  return True

countdown = 10
print("Starting While Loop")
while control_loop(countdown):
  print(countdown)
  countdown -= 1
  
print("We have liftoff!")