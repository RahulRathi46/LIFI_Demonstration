import serial , time					        # Headers

ser = serial.Serial('/dev/ttyACM0',9600)  		# open serial port
syn_delay=.650						            # SYN-Delay Value (Decimal Respresent Milliseconds)
pkt_delay=9				                # Packet SYN-Delay ( Seconds )
start="0100"						            # Start bit ( Ascii String start Representation )
stop="1100"						                # Stop bit ( Ascii String stop Representation )

print(ser.name)         				        # check which port was realy used
opt=raw_input("Enter 0 :  Sender & 1 : Reciver ->  ")	# Menu
if (opt=='0') :
    while (1) :
            o=0
            inp=raw_input("Enter massage : ")
            if (inp != "quit") :
                while(o!=len(inp)) :
		    print inp[o]
                    s=bin(ord(inp[o]))[2:].zfill(8)	        # Conversion Of charter to 8 bit string
                    u=0
                    s=start+s+stop
		    if (len(s)>16) : print "error !",len(s)			# Packet Crafting
                    while(u!=len(s)):
                        ser.write(s[u])     		        # write a string to serial port
                        time.sleep(syn_delay)		        # Sleep (SYN Delay )
                        u=u+1
                    o=o+1
		    time.sleep(pkt_delay)		                    # Delay b/w Packets
            else :
                print("Quiting Thank you !")		        # Ouiting Massage
else :

    f = open("raw.txt",'w')				                    # File Opening for logging
    while (1) :
                bytesToRead = ser.inWaiting()		        # Read Bytes From Serial
                data=ser.read(bytesToRead)		            # Reading
                f.write(data)				                # write readed to file
                print(data)				                    # Printing Out Readed0
                time.sleep(1)			            # Sleep (SYN Delay )
    ser.close()						                        # File Close
