## Custom Protocol

After PWM fails to perform the task there are many problems but the major problem is that using PWM we can not able to achive SYN and error
dectection. To over come these problem i brain stromed a soltion which is this custom proctocol. It is not the orignal idea it is a mix of multiple comm protocals which are edited to make my demonstration.

This protocol takes the 16 bit sequence as data packets with first 4 bits and last 4 bits as start and end of a vaild data pack with 8 bit reprentation of data in binary. For SYN & Error data problem protocal will take all the bits which are transmitting over the channel and check for the start and end bits if its in proper format it will decode it if any one of many invaild combinations it will count as error.

## Protocol In-Action

<img src="https://github.com/vangiex/LIFI_Demonstration/blob/master/Approch%202/High%20Level%20Code/output.png" width="100%" height="600" />

## Credits

- Rahul Rathi
