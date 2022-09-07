import pyautogui
import time
import json
import sys
from pynput import keyboard

SET_KLICK_BUTTON='m'
SET_COLOR_BUTTON='c'
SET_NODE_BUTTON='n'
SET_DEL_NODE_BUTTON="d"

SET_ALGORITM_BUTTON='a'
SAVE_BUTTON='s'
#pyautogui.PAUSE=4
pyautogui.FAILSAFE = False
SFK=1

#pyautogui.moveTo(0,1080,duration=0.2)
#pyautogui.click(clicks=1,interval=1)
ALGO_ARRAY=list()

def chekXY():
	x,y=pyautogui.position()
	return[int(x),int(y)]

def READ_PX(x,y):
	pix = pyautogui.pixel(x, y)
	#print(pix)
	time.sleep(0.01)
	return pix
#READ_PX(100,100)

def GO():
	while 1:
		x,y=chekXY()
		#print(pyautogui.event())
		print(x,"  ",y)
		time.sleep(0.01)


SECONDS =0
def on_press(key):
	
	global ALGO_ARRAY, WONKY,SECONDS

	try:
	#if True:
		KEY=key.char
		if(KEY==SET_NODE_BUTTON):
			ALGO_ARRAY.append({
				"COLORS":list(),
				"COLOR_XY":list(),
				"SFK":list(),#sleep_front_clik
				"CLICK_XY":list(),
				"CIM":False, #corect_it_mous
				})
			print("Create a new node: ",len(ALGO_ARRAY))

		if(KEY==SET_DEL_NODE_BUTTON):
			if(len(ALGO_ARRAY)>0):
				ALGO_ARRAY.pop(len(ALGO_ARRAY)-1)
				print("Delete  curent node: ",len(ALGO_ARRAY))
			else:
				print("Notes are missing")

		if(KEY==SET_COLOR_BUTTON and len(ALGO_ARRAY)>0):
			x,y=chekXY()
			ALGO_ARRAY[len(ALGO_ARRAY)-1]["COLOR_XY"].append([x,y])
			ALGO_ARRAY[len(ALGO_ARRAY)-1]["COLORS"].append(READ_PX(x,y))

			node=ALGO_ARRAY[len(ALGO_ARRAY)-1]
			print(READ_PX(x,y))

		if( KEY==SET_KLICK_BUTTON and len(ALGO_ARRAY)>0):
			#print("good")
			if(ALGO_ARRAY[len(ALGO_ARRAY)-1]["CIM"]==False):
				ALGO_ARRAY[len(ALGO_ARRAY)-1]["CIM"]=True
				SECONDS=time.time()
				
			ALGO_ARRAY[len(ALGO_ARRAY)-1]["CLICK_XY"].append(chekXY())
			ALGO_ARRAY[len(ALGO_ARRAY)-1]["SFK"].append(round(time.time()-SECONDS,2))
			print("node: ",len(ALGO_ARRAY), "PARAMS: ",chekXY()," delay: ",round(time.time()-SECONDS,2))
			SECONDS=time.time()

		if(KEY==SAVE_BUTTON):
			print("\n\n\n\n\n\n\n\n\n\n ================SAVE NODES================\n\n")
			in_dex=0
			NF={}
			for node in ALGO_ARRAY:
				if(node["CIM"] is True and len(node["COLORS"])>0 and len(node["COLOR_XY"])>0 ):
					in_dex+=1
					print("NODE: ",in_dex,"\n  color: ",node["COLORS"],"\n  cocol_xy: ",node["COLOR_XY"],
						"\n  place xy:",node["CLICK_XY"])

					NF[str("NODE"+str(in_dex))]=node
				pass
			input("\n press Enter to contune...")
			with open(str(input("inter save name file:")+".json"),"w")as json_file:
				json.dump(NF,json_file,indent=3)

			print("SUCCESSFULLY")
			time.sleep(1)
			sys.exit()#is out to prgamm

	except AttributeError:
		if(0==1):
			print('special key {0} pressed'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        return False
###########################################################################################################################
def noTouch(l1,l2):
	x1=int(l1[0])
	x2=int(l2[0])

	y1=int(l1[1])
	y2=int(l2[1])

	if(x1==x2 and y1==y2):
		return True
	ret=0
	if(x1>x2):
		ret+=(x1-x2)
	else:
		ret+=(x2-x1)

	if(y1>y2):
		ret+=(y1-y2)
	else:
		ret+=(y2-y1)
	if(ret>20):
		return False

	return True

def WORK_CLIC():
	JSFIL=0
	SUk1=True
	while SUk1 is True:
		try:
			with open(str(input("enter_import_file_name:")),"r")as json_file:
				JSFIL=json.load(json_file)
			SUk1=False
		except Exception as e:
			print(e)
	
				#print(JSFIL["NODE2"])
	ARAY_MALE=list()
	rst=1
	while rst>0:
		try:
			ARAY_MALE.append( JSFIL[str("NODE"+str(rst))] )
			rst+=1
		except KeyError:
			rst=0
	in_dex=1
	for node in ARAY_MALE:
		print("NODE: ",in_dex,"\n  color: ",node["COLORS"],"\n  cocol_xy: ",node["COLOR_XY"],"\n  place xy:",node["CLICK_XY"],node)
		in_dex+=1

	time.sleep(4)

	conlroleXY=chekXY() 
	BREKER=True
	while BREKER and noTouch(conlroleXY,chekXY()):
		inDEX=0
		time.sleep(0.01)
		for node in ARAY_MALE:
			inDEX+=1
			siza=len(node["COLORS"])

			fulltrue=True
			for index in range(0,siza):
				#print(index)
				COR=READ_PX(node["COLOR_XY"][index][0],node["COLOR_XY"][index][1])
				#print(COR," ",node["COLORS"][index])
				if(COR[0]==node["COLORS"][index][0] and COR[1]==node["COLORS"][index][1] and COR[2]==node["COLORS"][index][2]):
					pass
				else:
					fulltrue=False

			if(noTouch(conlroleXY,chekXY()) is False):
				REKER=False
				break

			if fulltrue is True:
				SFKtim=0
				for clxy in node["CLICK_XY"]:

					
					time.sleep(node["SFK"][SFKtim])
					if(noTouch(conlroleXY,chekXY()) is False):
						BREKER=False
						break

					print("clk: ",clxy," NODE: ",inDEX,"  delay: ",node["SFK"][SFKtim])
					pyautogui.moveTo(clxy[0],clxy[1], duration=0.2)	
					pyautogui.click(clicks=1,interval=1)
					SFKtim+=1
					
					conlroleXY=chekXY()

					
				
	print("control is given to the user")
	time.sleep(1)



WONKY=True
while WONKY:
	imP=input("make new preset[n] or import file preset[f]: ")
	if(imP=="n"):

		suka=True
		while suka is True:
			try:
				SFKK=float(input("enter delay sec: "))
				if SFKK<0.01:
					SFKK=0.05
				suka =False
			except Exception as e:
				print(e)
		

		with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:listener.join()
		listener = keyboard.Listener(on_press=on_press,on_release=on_release)
		listener.start()
		WONKY=False
	elif(imP=="f"):
		WORK_CLIC()
		WONKY=False
	else:
		print("WRONG COMMAND")



##################GO_AUTOCLICER############################################

#with open(input("inter_preset_name_file:"),"r")as json_file:
#	nod_js=json.load(json_file)

#print(nod_js)


#if( key.char==SET_KLICK_BUTTON and ALGO_ARRAY.length()>0  and ALGO_ARRAY.length()>0):
