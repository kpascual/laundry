# Laundry

*Problem*: Often I forget about a load of laundry. I would like to minimize the time a load has been sitting idle. 

*Solution*: Sense that the washer or dryer is no longer in use, then contact me via SMS.

I chose SMS because, like many others, my phone is with me at all times. Interfacing with SMS is simple thanks to Twilio, especially compared to building my own phone-based client, or integrating with chat-based apps like Facebook Messenger. Email was another alternative, but I did not want to fill my inbox with more junk. 

## Architectural Diagram
![Architectural Diagram](https://github.com/kpascual/laundry/blob/master/laundry_system_diagram.png)

Both the MQTT broker and subscriber live on the same Raspberry Pi device, however this is not necessary. 

##  Tilt Sensor Wiring Diagram
![Tilt Sensor Wiring Diagram](https://github.com/kpascual/laundry/blob/master/laundry_fritzing_v2.png)

## Possible Future Improvements (assuming I care to improve this)

* Apply certificates for secure message transport
* Use a more robust sensor than the tilt sensor
* Use different algorithm and threshold to trigger SMS notification

[Replicated from my website](http://kenpascual.com/projects/laundry.html)
