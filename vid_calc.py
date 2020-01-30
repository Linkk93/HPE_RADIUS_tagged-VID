def calculate():
    vid = input("Which VLAN ID shall be converted?\n")

    if 0 < int(vid) <= 4094:

        print("Converting {}...".format(vid))

        # strip "0x"
        hex_strip = hex(int(vid)).lstrip("0x")

        # check for missing leading 0
        while len(hex_strip) < 3:
            hex_strip = "0" + hex_strip

        hex_radius = "0x31000" + hex_strip
        int_radius = int(hex_radius, 16)

        print("The ID is:\n{}".format(int_radius))

    else:
        print("Invalid VLAN ID: {}".format(vid))

    input("Press any key...")

if __name__ == '__main__':
    rerun = "y"
    while rerun == "y":
        calculate()
        rerun = input("Rerun the script? (y/n) \n")
