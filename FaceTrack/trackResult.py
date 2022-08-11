from UDPComms import Subscriber

HOST = '10.32.176.172'           #服务器的ip
pipe_port = 3257                   #服务器端口
self_port = 3259
nextActionFile = "../StanfordQuadruped/nextAction.txt"

subscriber = Subscriber(pipe_port,self_port)
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


