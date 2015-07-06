import random
import mycolor

def main_header():

    header_1 = mycolor.color.cyan + """
      1000101100000000111111111111111000000011111110000
      0011111111000000011111101010101010101010000000000
      1111111111111111111111111000000000001010000000111
      0011110000001010101011111111111010101011111111111
      1111110011110000011111111111111111100000000111111
				00001111111
				00001111110
				11000000111
		0 0		01010101010
				01111111010
				11111100101
				00000001111101010101011
				11111111110001111010111

      11111111111110000000
      00000101010101111111""" + mycolor.color.end

    header_2 = mycolor.color.green + r"""
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      M						      M
      M						      M
      M						      M
      M		    King Sploit Framework   	      M
      M						      M
      M						      M
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      MMMMMMMMMMMMMM			 MMMMMMMMMMMMMM
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM""" + mycolor.color.end

    header_3 = mycolor.color.purple + r"""
      ooooooooooooooooooooooooooooooooooooooooooooooooo
      VVVV					   VVVV
       V	   00			00          V
    
	
			___________
			    |  |
			    |  |
			    UUUU

	    ____________________________________
	    000000000000000000000000000000000000
	    000000000000000000000000000000000000
	    ------------------------------------""" + mycolor.color.end

    header_4 = mycolor.color.darkcyan + """
	_
       | |          O        @@				
       | |        O					10    -------------|
       | |      O					10		   |
       | |    O              [ ]			10		   |
       | |  O		     [ ]			10		   |
       | |O		     [ ]     `~~~~~~~~~~~`	10		   |
       | |		     [ ]     M		 M	10		   |
       | |O		     [ ]     M           M	11    --------------
       | |  O		     [ ]     M		 M	11		   |
       | |    O		     [ ]     M		 M	11		   |
       | |      O	     [ ]     M		 M	10		   |
       | |        O	     [ ]     M		 M	10		   |
       | |          O	     [ ]     M	         M	11		   |
       | |            O	     [ ]     M		 M	10		   |
       | |              O    [ ]     M		 M	10		   |
       |_|                   [ ]     M		 M	11    --------------
	""" + mycolor.color.end	

    rand_num = random.randint(1,4)
    if rand_num == 1:
	print(header_1)
    if rand_num == 2:
	print(header_2)
    if rand_num == 3:
	print(header_3)
    if rand_num == 4:
	print(header_4)
