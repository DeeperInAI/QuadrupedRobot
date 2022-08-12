from UDPComms import Subscriber

port_rv = 3257                   #服务器端口
nextActionFile = "../StanfordQuadruped/nextAction.txt"

subscriber = Subscriber(port_rv)
while True:
    message = subscriber.recv()
    angle = (int(message['left']) - 550) / 100
    nextAction = open(nextActionFile, "w")
    if angle > 0:
        nextAction.write("right")
        print("need trun right, angle = " + str(angle))
    else:
        nextAction.write("left")
        print("need trun left, angle = " + str(-angle))
    nextAction.close()
sock.close()


