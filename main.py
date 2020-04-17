from vehicle import Vehicle 

vehicle1 = Vehicle("vehicle1", "red", "fast")
vehicle2 = Vehicle("vehicle2", "blue", "fast")
vehicle3 = Vehicle("vehicle3", "yellow", "slow")
vehicle4 = Vehicle("vehicle4", "white", "fast")
vehicle5 = Vehicle("vehicle5", "purple", "slow")

vehicle1.drive()
vehicle2.drive()
vehicle1.stop()
vehicle3.drive()
vehicle2.turn("left")
vehicle4.turn("right")
vehicle5.drive()
