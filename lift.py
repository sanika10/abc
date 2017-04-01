import Adafruit_BBIO.GPIO as GPIO
import time
import math

led5r = "P8_9"
led5g = "P8_10"

led4r = "P8_17"
led4g = "P8_18"

led3r = "P8_19"
led3g = "P9_11"

led2r = "P9_12"
led2g = "P9_13"

led1r = "P9_14"
led1g = "P9_15"

leddn = "P8_8"
ledup = "P8_7"

switch5 = "P8_12"
switch4 = "P8_13"
switch3 = "P8_14"
switch2 = "P8_15"
switch1 = "P8_16"

disp1 = "P9_24"#MSB
disp2 = "P9_23"
disp3 = "P9_22"
disp4 = "P9_21"#LSB



i=0;
cur_floor = 1;

GPIO.setup(led1r, GPIO.OUT)
GPIO.setup(led1g, GPIO.OUT)
GPIO.setup(led2r, GPIO.OUT)
GPIO.setup(led2g, GPIO.OUT)
GPIO.setup(led3r, GPIO.OUT)
GPIO.setup(led3g, GPIO.OUT)
GPIO.setup(led4r, GPIO.OUT)
GPIO.setup(led4g, GPIO.OUT)
GPIO.setup(led5r, GPIO.OUT)
GPIO.setup(led5g, GPIO.OUT)
GPIO.setup(ledup, GPIO.OUT)
GPIO.setup(leddn, GPIO.OUT)
GPIO.setup(disp1, GPIO.OUT)
GPIO.setup(disp2, GPIO.OUT)
GPIO.setup(disp3, GPIO.OUT)
GPIO.setup(disp4, GPIO.OUT)
GPIO.setup(switch1, GPIO.IN)
GPIO.setup(switch2, GPIO.IN)
GPIO.setup(switch3, GPIO.IN)
GPIO.setup(switch4, GPIO.IN)
GPIO.setup(switch5, GPIO.IN)

def start_setup():
	GPIO.output(led1r, GPIO.HIGH)
	GPIO.output(led1g, GPIO.LOW)
	GPIO.output(led2r, GPIO.HIGH)
	GPIO.output(led2g, GPIO.HIGH)
	GPIO.output(led3r, GPIO.HIGH)
	GPIO.output(led3g, GPIO.HIGH)
	GPIO.output(led4r, GPIO.HIGH)
	GPIO.output(led4g, GPIO.HIGH)
	GPIO.output(led5r, GPIO.HIGH)
	GPIO.output(led5g, GPIO.HIGH)
	GPIO.output(ledup, GPIO.HIGH)
	GPIO.output(leddn, GPIO.HIGH)
	return;


def switch_press():
	if (GPIO.input(switch1)) :
		GPIO.output(led1r, GPIO.LOW)
		GPIO.output(led2r, GPIO.HIGH)
		GPIO.output(led3r, GPIO.HIGH)
		GPIO.output(led4r, GPIO.HIGH)
		GPIO.output(led5r, GPIO.HIGH)
 		return(1);
	elif (GPIO.input(switch2)) :
		GPIO.output(led1r, GPIO.HIGH)
		GPIO.output(led2r, GPIO.LOW)
		GPIO.output(led3r, GPIO.HIGH)
		GPIO.output(led4r, GPIO.HIGH)
		GPIO.output(led5r, GPIO.HIGH) 		
		return(2);
	elif (GPIO.input(switch3)) :
 		GPIO.output(led1r, GPIO.HIGH)
		GPIO.output(led2r, GPIO.HIGH)
		GPIO.output(led3r, GPIO.LOW)
		GPIO.output(led4r, GPIO.HIGH)
		GPIO.output(led5r, GPIO.HIGH)
		return(3);
	elif (GPIO.input(switch4)) :
 		GPIO.output(led1r, GPIO.HIGH)
		GPIO.output(led2r, GPIO.HIGH)
		GPIO.output(led3r, GPIO.HIGH)
		GPIO.output(led4r, GPIO.LOW)
		GPIO.output(led5r, GPIO.HIGH)
		return(4);
	elif (GPIO.input(switch5)) :
 		GPIO.output(led1r, GPIO.HIGH)
		GPIO.output(led2r, GPIO.HIGH)
		GPIO.output(led3r, GPIO.HIGH)
		GPIO.output(led4r, GPIO.HIGH)
		GPIO.output(led5r, GPIO.LOW)
		return(5);		
	else:
		return(0);

def clear_green_cur():
	if(cur_floor==1):
		GPIO.output(led1g, GPIO.HIGH)
	elif(cur_floor==2):
		GPIO.output(led2g, GPIO.HIGH)
	elif(cur_floor==3):
		GPIO.output(led3g, GPIO.HIGH)
	elif(cur_floor==4):
		GPIO.output(led4g, GPIO.HIGH)
	elif(cur_floor==5):
		GPIO.output(led5g, GPIO.HIGH)
	return;

def set_green_cur():
	if(cur_floor==1):
		GPIO.output(led1g, GPIO.LOW)
	elif(cur_floor==2):
		GPIO.output(led2g, GPIO.LOW)
	elif(cur_floor==3):
		GPIO.output(led3g, GPIO.LOW)
	elif(cur_floor==4):
		GPIO.output(led4g, GPIO.LOW)
	elif(cur_floor==5):
		GPIO.output(led5g, GPIO.LOW)
	return;

def clear_green():
	if(i==1):
		GPIO.output(led1g, GPIO.HIGH)
	elif(i==2):
		GPIO.output(led2g, GPIO.HIGH)
	elif(i==3):
		GPIO.output(led3g, GPIO.HIGH)
	elif(i==4):
		GPIO.output(led4g, GPIO.HIGH)
	elif(i==5):
		GPIO.output(led5g, GPIO.HIGH)
	return;

def set_green():
	if(i==1):
		GPIO.output(led1g, GPIO.LOW)
	elif(i==2):
		GPIO.output(led2g, GPIO.LOW)
	elif(i==3):
		GPIO.output(led3g, GPIO.LOW)
	elif(i==4):
		GPIO.output(led4g, GPIO.LOW)
	elif(i==5):
		GPIO.output(led5g, GPIO.LOW)

	return;

def clear_red():
	if(i==1):
		GPIO.output(led1r, GPIO.HIGH)
	elif(i==2):
		GPIO.output(led2r, GPIO.HIGH)
	elif(i==3):
		GPIO.output(led3r, GPIO.HIGH)
	elif(i==4):
		GPIO.output(led4r, GPIO.HIGH)
	elif(i==5):
		GPIO.output(led5r, GPIO.HIGH)
	return;

def set_red():
	if(i==1):
		GPIO.output(led1r, GPIO.LOW)
	elif(i==2):
		GPIO.output(led2r, GPIO.LOW)
	elif(i==3):
		GPIO.output(led3r, GPIO.LOW)
	elif(i==4):
		GPIO.output(led4r, GPIO.LOW)
	elif(i==5):
		GPIO.output(led5r, GPIO.LOW)		
	return;

def up_arrow():
	GPIO.output(ledup, GPIO.LOW)
	GPIO.output(leddn, GPIO.HIGH)	
	return;

def dn_arrow():
	GPIO.output(ledup, GPIO.HIGH)
	GPIO.output(leddn, GPIO.LOW)	
	return;

def no_arrow():
	GPIO.output(ledup, GPIO.HIGH)
	GPIO.output(leddn, GPIO.HIGH)	
	return;


def disp(t):
	if(t==1):
		GPIO.output(disp1, GPIO.LOW)
		GPIO.output(disp2, GPIO.LOW)
		GPIO.output(disp3, GPIO.LOW)
		GPIO.output(disp4, GPIO.HIGH)
	elif(t==2):
		GPIO.output(disp1, GPIO.LOW)
		GPIO.output(disp2, GPIO.LOW)
		GPIO.output(disp3, GPIO.HIGH)
		GPIO.output(disp4, GPIO.LOW)
	elif(t==3):
		GPIO.output(disp1, GPIO.LOW)
		GPIO.output(disp2, GPIO.LOW)
		GPIO.output(disp3, GPIO.HIGH)
		GPIO.output(disp4, GPIO.HIGH)
	elif(t==4):
		GPIO.output(disp1, GPIO.LOW)
		GPIO.output(disp2, GPIO.HIGH)
		GPIO.output(disp3, GPIO.LOW)
		GPIO.output(disp4, GPIO.LOW)
	elif(t==5):
		GPIO.output(disp1, GPIO.LOW)
		GPIO.output(disp2, GPIO.HIGH)
		GPIO.output(disp3, GPIO.LOW)
		GPIO.output(disp4, GPIO.HIGH)
	elif(t==6):
		GPIO.output(disp1, GPIO.LOW)
		GPIO.output(disp2, GPIO.HIGH)
		GPIO.output(disp3, GPIO.HIGH)
		GPIO.output(disp4, GPIO.LOW)
	elif(t==7):
		GPIO.output(disp1, GPIO.LOW)
		GPIO.output(disp2, GPIO.HIGH)
		GPIO.output(disp3, GPIO.HIGH)
		GPIO.output(disp4, GPIO.HIGH)
	elif(t==8):
		GPIO.output(disp1, GPIO.HIGH)
		GPIO.output(disp2, GPIO.LOW)
		GPIO.output(disp3, GPIO.LOW)
		GPIO.output(disp4, GPIO.LOW)
	elif(t==9):
		GPIO.output(disp1, GPIO.HIGH)
		GPIO.output(disp2, GPIO.LOW)
		GPIO.output(disp3, GPIO.LOW)
		GPIO.output(disp4, GPIO.HIGH)
	elif(t==0):
		GPIO.output(disp1, GPIO.LOW)
		GPIO.output(disp2, GPIO.LOW)
		GPIO.output(disp3, GPIO.LOW)
		GPIO.output(disp4, GPIO.LOW)
	return;



start_setup();
disp(0);
while True:
	tar_floor = switch_press();	
    	if(tar_floor != 0):		
		time.sleep(1);		
		clear_green_cur();
		if(cur_floor < tar_floor):
			up_arrow();
			cur_floor=cur_floor+1;
			for i in range((cur_floor),(tar_floor+1)) :
				set_green();
				disp(i-1);								
				time.sleep(2)								
				clear_green();
			cur_floor=i;			
			no_arrow();
			clear_red();
			set_green();
		elif(tar_floor < cur_floor):
			dn_arrow();
			cur_floor=cur_floor-1;
			for i in range((cur_floor),(tar_floor-1),-1) :
				set_green();
				disp(i-1);								
				time.sleep(2)								
				clear_green();
			cur_floor=i;			
			no_arrow();
			clear_red();
			set_green();
			
		else:
			set_green();
			clear_red();
	
