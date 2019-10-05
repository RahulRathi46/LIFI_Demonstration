class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def decoder ():                                     # Decoder
    global scc
    global err
    global p
    f=open("sample.txt",'r')
    result=''
    while True:
        s=f.readline()
        if (s=='') : break
        if (s[0:4]!="0100" and s[12:16]!="1100") :                       # Start &  stop bit handling  error is here
	    print color.RED+"  Packet Header And Footer Error !"
            err=err+1
	else :
		if (s[0:4]!="0100") :                       # Start &  stop bit handling  error is here
		    print color.RED+"  Packet Header Error !"
		    err=err+1
		else :
			if (s[12:16]!="1100") :                       # Start &  stop bit handling  error is here
			    print color.RED+"  Packet Footer Error !"
			    err=err+1
			else :
			    scc=scc+1
        print color.END+"\t\t\t" + str(f.tell()) + " @ Massage Packet Binary : " + s
	s=s[4:12]                                   # Take DATA Out From Packet
        print "\t\t\t  # Massage Binary : " + s + "\n"
        s=int(s,2)                                  # conversion's
        s=unichr(s)
        result=result+s                             # staffing decoded massage final result
    return result

def take_sample (t) :                               # Sampler
    global sampling
    global debug
    c=0
    if ( (t+16) > len(temp) ): return t+1
    while (t!=0):
        sampling = sampling+temp[t]
        c=c+1
        t=t+1
	if(c==16): break                             # Packet Read Complete
    y.write(sampling)                                # Writing to sample file
    y.write("\n")
    debug = debug + sampling                         # adding packet sample to debug massage
    sampling=""
    return t

def Sample(o):
    while(o<len(temp)):
        if(temp[o]=='0'):                           # Taking Break Point for start bit
            o=take_sample(o)                        # Calling  Sampler
        else :
            o=o+1                                   # ignore case


# Main Program Start
from os import system
from sys  import argv
system("clear")
f = open("raw.txt",'r')                             # File Have Logs
y = open("sample.txt","w")                          # Logging Packets To file
temp=""                                             # temp variable
sampling=""                                         # sampling variable
debug=""                                            # debug Variable
o=0
scc=0                                               # Success counter
err=0                                               # Error counter
while True:        				    # making String From Stream Capture
    s=f.read(1)
    if (s=="") : break                              # File end identifiers
    if (s=="0") : temp=temp+s                       # loggers
    if (s=="1") : temp=temp+s                       # loggers
print color.RED+"\nReceived Sequence : " + color.END + temp + "\n"
Sample(1)                                           # call in sample
f.close()                                           # releasing resource
y.close()                                           # releasing resource
print   color.GREEN+color.BOLD+"Identified Message Sequence : " + color.END + debug + "\n"
print "Packet's Extracted From Received Sequence : " + "\n"
print  color.DARKCYAN + color.BOLD + "\nMessage Decoded : " + color.END + color.BLUE +  decoder() + "\n" + color.END       # Getting decode
print color.YELLOW+"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n"
print "Total Status Report :\n\t\t\tError : ",err
print "\t\t\tSuccess : ",scc
print "\t\t\tTotal Packets : ",(err+scc)
print "Success Rate : ",float((100*scc)/(err+scc)),"%"
print
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n"
print color.END
