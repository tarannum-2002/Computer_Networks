
inputPacket=0
outputPacket=3
BucketBuffer=0
time =0

while(time<10):
    print("give input packet at time " + str(time))
    inputPacket= int(input())
    BucketBuffer=BucketBuffer+inputPacket
    if BucketBuffer>60:
        time=time+1
        BucketBuffer=BucketBuffer-inputPacket
        print("packet couldnot be stored in bucket")
        BucketBuffer=BucketBuffer-outputPacket  
        print("Packet of size " + str(outputPacket) + " is removed")
        print("Bucket has "+ str(BucketBuffer) + " packets")
        
    else:
        time=time+1
        if BucketBuffer<outputPacket:
           
            print("Packet of size " + str(BucketBuffer) + " is removed")
            BucketBuffer=0
            print("Bucket has "+ str(BucketBuffer) + " packets")
        
        else:
            BucketBuffer=BucketBuffer-outputPacket    
            print("Packet of size " + str(outputPacket) + " is removed")
            print("Bucket has "+ str(BucketBuffer) + " packets")
            
            
