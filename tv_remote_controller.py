#Screen that shows you can do.
print("""
***CHANNELS***

1-TRT
2-ATV
3-KANAL D
4-FOX TV
5-TV 8
6-CARTOON NETWORK

Volume up(+)
Volume down(-)
Previous channel(p)
Next channel(n)
Mute(m)

Quit(q)
""")



volume=15   #Volume parameter

channel=1   #Channel parameter

dict_channels={1:"TRT",2:"ATV",3:"KANAL D",4:"FOX TV",5:"TV 8",6:"CARTOON NETWORK"}   #Dict of channels




while True:

    n= input("ENTER A PROCESS:")

    if n == "q":  #Closing button
        print("Remote is closing...")
        break

    elif n == "+":    #Volume up button
        if volume < 30 :  #Choose max limit
            volume+=1
            print("<"+")"*volume)

    elif n == "-":    #Volume Down button
        if volume > 0 :   #Choose min limit
            volume-=1
            print("<"+")"*volume)

    elif n == "p":    #Channel down button
        if channel>1:   #Choose min limit
            channel-=1
            print(dict_channels[channel])
        else:
            print("There is not a channel saved")

    elif n == "n":    #Channel up button
        if channel<6:   #Choose max limit
            channel+=1
            print(dict_channels[channel])
        else:
            print("There is not a channel saved")

    elif n == "m":    #To mute TV
        volume=0
        print("<X")

    elif n == "1" or n == "2" or n == "3" or n == "4" or n == "5" or n == "6":    #Choosing channel from dict
        n=int(n)
        print(dict_channels[n])
    else:
        print("PLEASE ENTER A VALID PROCESS")
