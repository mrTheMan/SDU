Author: 	Alexandros Karambelas Langkilde
Student mail:	alang16
Language: 	Python


The fluffy stuff:

I have implemented a state machine for a TV. It has channels and volume and a state of either on/off.
Method chaining is used but any indeentation can be used because of Python inside the {} brackets.

An instance of the class TV is made so that we can remove the () brackets in the TV to make it more clean.

You can write all method calls in any case sensitivity you like except where you set a value (like ChannelSet and VolumeSet) 
which require that specific case sensitivity. The other methods (see list of callable methods below) can be written however you like ( pRiNt ) would still print the current state because we compare in lower case. You can print the state continues, just add print to the method chain at any point. The channels and volume on the TV both range between 0 and 100.


Right to the chase!:

using __getattr__ i get the unidentified item. The code example shows how to get all the methods in a class. 
Using this list I loop through matching the 'item' passed through with any method in the class, this is done in lowercase.

*Sidenote: the methods in the class have a '_f' extention so that the user has the full usage of case sensitivity (e.g. Print, prinT, prInt, PRINT)  



Code example:
method_list = [func for func in dir(TV) if callable(getattr(TV, func)) and not func.startswith("__")]


Callable methods in TV:
PowerOn
PowerOff
ChannelUp
ChannelDown
ChannelSet( int )
VolumeUp
VolumeDown
VolumeSet( int )
Print


Usage Example:
TV = TV()

{

    TV.PowerOn.
            ChannelUp.
            ChannelSet(34).
            VolumeUp.
            VolumeSet(56).
        Print.
	VolumeUp.
	VolumeUp.
	Print
}