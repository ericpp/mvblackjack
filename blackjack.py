import pyautogui
import random
import time
import os
from PIL import Image
from PIL import ImageChops
import csv

region = None
bregion = None

image_dir = "images/"

# 1482 142
# 1783 813

# 1731 216
# 1995 582

doff = ( 360, 100 )
poff = ( 350, 370 )
p2off = ( 410, 250 )
acoff = ( 310, 385 )

numbers = [
	"2.png",
	"3.png",
	"4.png",
	"5.png",
	"6.png",
	"7.png",
	"8.png",
	"9.png",
	"10.png",
	"1-11.png",
	"2-12.png",
	"3-13.png",
	"4-14.png",
	"5-15.png",
	"6-16.png",
	"7-17.png",
	"8-18.png",
	"9-19.png",
	"10-20.png",
	"11.png",
	"12.png",
	"13.png",
	"14.png",
	"15.png",
	"16.png",
	"17.png",
	"18.png",
	"19.png",
	"20.png",
]

hits = {
	"2": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
	"3": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
	"4": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
	"5": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
	"6": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
	"7": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
	"8": [ "2", "3", "4", "7", "8", "9", "10", "1-11" ],
	"9": [ "7", "8", "9", "10", "1-11" ],
	"10": [ "10", "1-11" ],
	"12": [ "2", "3", "7", "8", "9", "10", "1-11" ],
	"13": [ "7", "8", "9", "10", "1-11" ],
	"14": [ "7", "8", "9", "10", "1-11" ],
	"15": [ "7", "8", "9", "10", "1-11" ],
	"16": [ "7", "8", "9", "10", "1-11" ],
	"3-13": [ "2", "3", "7", "8", "9", "10", "1-11" ],
	"4-14": [ "2", "3", "7", "8", "9", "10", "1-11" ],
	"5-15": [ "2", "3", "7", "8", "9", "10", "1-11" ],
	"6-16": [ "2", "3", "7", "8", "9", "10", "1-11" ],
	"7-17": [ "7", "8", "9", "10", "1-11" ],
	"8-18": [ "9", "10" ],
	"9-19": [ ],
	"10-20": [ ],
}

stands = {
	"12": [ "4", "5", "6" ],
	"13": [ "2", "3", "4", "5", "6" ],
	"14": [ "2", "3", "4", "5", "6" ],
	"15": [ "2", "3", "4", "5", "6" ],
	"16": [ "2", "3", "4", "5", "6" ],
	"17": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
	"18": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
	"19": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
	"20": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
	"8-18": [ "2", "7", "8", "1-11" ],
	"9-19": [ "2", "3", "4", "5", "7", "8", "9", "10", "1-11" ],
	"10-20": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
}

splits = {
	"2-12": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
	"4": [ "3", "4", "5", "6", "7" ],
	"6": [ "4", "5", "6", "7" ],
	"12": [ "2", "3", "4", "5", "6" ],
	"14": [ "2", "3", "4", "5", "6", "7" ],
	"16": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
	"18": [ "2", "3", "4", "5", "6", "8", "9" ],
}

doubles = {
	"8": [ "5", "6" ],
	"9": [ "2", "3", "4", "5", "6" ],
	"10": [ "2", "3", "4", "5", "6", "7", "8", "9" ],
	"11": [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "1-11" ],
	"3-13": [ "4", "5", "6" ],
	"4-14": [ "4", "5", "6" ],
	"5-15": [ "4", "5", "6" ],
	"6-16": [ "4", "5", "6" ],
	"7-17": [ "2", "3", "4", "5", "6" ],
	"8-18": [ "3", "4", "5", "6" ],
	"9-19": [ "6" ],
}

image_cache = {}

def get_image(name):
	if name not in image_cache:
		print "caching: " + name
		image_cache[name] = Image.open(open(image_dir + name, 'rb'))

	return image_cache[name]

def find_btn(btn, region=None):
	return pyautogui.locateCenterOnScreen(get_image(btn + ".png"), grayscale=True, region=region)

def find_first(btns, region=None):
	for btn in btns:
		c = find_btn(btn, region)
		if c:
			return btn

def click_btn(btn, region=None):
	loc = find_btn(btn, region)
	clicked = False

	if loc:
		print btn, loc

	if loc is not None:
		mouse = pyautogui.position()
		pyautogui.moveTo(loc[0], loc[1], 0.25)
		pyautogui.click(loc[0], loc[1])
		pyautogui.moveTo(mouse[0], mouse[1], 0.25)
		clicked = True

	return clicked

def click_any(btns, region=None):
	clicked = False

	for btn in btns:
		c = click_btn(btn, region)
		if c:
			clicked = True

	return clicked

def click_first(btns, region=None):
	for btn in btns:
		c = click_btn(btn, region)
		if c:
			return btn

	return None

def is_hand1(pos):
	reg = (pos[0], pos[1], 50, 20)
	active = False

	im1 = pyautogui.screenshot(region=(region[0]+acoff[0], region[1]+acoff[1], 50, 20))
	time.sleep(.1)

	im2 = pyautogui.screenshot(region=(region[0]+acoff[0], region[1]+acoff[1], 50, 20))
	time.sleep(.2)

	im3 = pyautogui.screenshot(region=(region[0]+acoff[0], region[1]+acoff[1], 50, 20))
	time.sleep(.3)

	if ImageChops.difference(im1, im2).getbbox() is not None:
		active = True

	if ImageChops.difference(im2, im3).getbbox() is not None:
		active = True

	if ImageChops.difference(im1, im3).getbbox() is not None:
		active = True

	return active

def get_hand(pos, name=None):
	hand = None
	img = pyautogui.screenshot(region=(pos[0], pos[1], 40, 40))

	for num in reversed(numbers):
		loc = pyautogui.locate(get_image(num), img, grayscale=True)

		# if name:
		# 	print name + ":", num, loc

		if loc is not None:
			fn, fext = os.path.splitext(num)
			hand = fn
			break

	return hand


def get_action(dhand, phand):
	split = pyautogui.locateOnScreen(get_image("split.png"), grayscale=True, region=bregion)

	if split is not None and splits.has_key(phand) and dhand in splits[phand]:
		return "split"

	if doubles.has_key(phand) and dhand in doubles[phand]:
		return "dd"

	if hits.has_key(phand) and dhand in hits[phand]:
		return "hit"

	if stands.has_key(phand) and dhand in stands[phand]:
		return "stand"

	return None

def run_action(dhand, phand, player="player"):
	action = get_action(dhand, phand)
	clicked = None

	print "dealer: ", dhand, " " + player + ": ", phand, " action: ", action

	if action == "split":
		btns = ["split", "hit"]
		clicked = click_first(btns, bregion)
	elif action == "dd":
		btns = ["dd", "hit"]
		clicked = click_first(btns, bregion)
	elif action is not None:
		clicked = click_first([action], bregion)

	return clicked

def write_log(writer, row):
	print "log", row
	writer.writerow(row)

# 7 fail
# 8 fail
# 9 fail
# 18, 13
# d17

round = time.time()
dhand = None
phand = None
p2hand = 0
p1active = True
splitted = False
action = None

logfile = open('logfile.csv', 'a')
logwriter = csv.writer(logfile, lineterminator='\n')

while True:
	anc = pyautogui.locateCenterOnScreen(get_image("anchor.png"), grayscale=True)

	# if anc:
	# 	print "anchor", anc

	if anc is not None:
		region = ( anc[0]-100, anc[1], 700, 800 )
		bregion = ( anc[0]-100, anc[1]+425, 700, 100)

	# if region:
	# 	# deal1 = (region[0]+270, region[1]+25, 20, 100)
	# 	deal1 = (region[0]+305, region[1]+290, 20, 100)
	# 	# dealer card 1
	# 	# pyautogui.screenshot('test.png', region=(region[0]+270, region[1]+25, 20, 100))
	# 	suits = ["club", "heart", "spade", "diamond"]
	# 	ranks = ["2","3","4","5","6","7","8","9","a","j","q","k"]

	# 	for suit in suits:
	# 		loc = pyautogui.locateOnScreen(image_dir + "suit-" + suit + ".png", grayscale=True, region=deal1)
	# 		print suit, loc

	# 	for rank in ranks:
	# 		loc = pyautogui.locateOnScreen(image_dir + "rank-" + rank + ".png", grayscale=True, region=deal1)
	# 		print rank, loc


	# 	# player card 1
	# 	#pyautogui.screenshot('test.png', region=(region[0]+310, region[1]+290, 20, 100))

	# continue

#	if anc is None:
#		btns = ["okay", "tablegames", "play", "play2", "play3"]
#		eks = ["x", "x2", "x3", "x4", "x5", "x6"]
#
#		clicked = click_any(btns)
#		time.sleep(1)
#
#		if not clicked:
#			click_first(eks)

	if region is None or bregion is None:
		continue

	btns = ["rebet", "deal", "no"]
	click = find_first(btns, bregion)

	if click == "rebet":
		outcomes = ['win','lose','bust','blackjack','push']
		result = find_first(outcomes, (region[0]+acoff[0], region[1]+acoff[1], 75, 25))
		dfinal = get_hand((region[0]+doff[0], region[1]+doff[1]), "dfinal")
		# pfinal = get_hand((region[0]+poff[0], region[1]+poff[1]), "player")
		# p2final = get_hand((region[0]+poff[0], region[1]+poff[1]), "player2")
		if not phand and result != 'bust':
			phand = get_hand((region[0]+poff[0], region[1]+poff[1]), "p1final")

		if not p1active and not p2hand:
			p2hand = get_hand((region[0]+p2off[0], region[1]+p2off[1]), "p2final")

		write_log(logwriter, [ time.time(), round, dfinal, phand, p2hand, p1active, action, result ])

		round = time.time()
		dhand = None
		phand = None
		p2hand = None
		splitted = False

	if click:
		clicked = click_btn(click, bregion)

	p1active = True

	if splitted:
		p1active = is_hand1((region[0]+acoff[0], region[1]+acoff[1]))
		print "player1 hand: ", p1active

	if dhand is None:
		dhand = get_hand((region[0]+doff[0], region[1]+doff[1]), "dealer")
		print "dealer has:", dhand

	if p1active:
		if phand is None:
			phand = get_hand((region[0]+poff[0], region[1]+poff[1]), "player")
			print "player has:", phand

		if phand is not None and dhand is not None:
			action = run_action(dhand, phand)

			if action:
				write_log(logwriter, [ time.time(), round, dhand, phand, p2hand, p1active, action, None ])

			if action != "stand":
				phand = None

			if action == "split":
				p2hand = None
				splitted = True

	if not p1active:
		if p2hand is None:
			p2hand = get_hand((region[0]+p2off[0], region[1]+p2off[1]), "player2")
			print "player2 has:", p2hand

		if p2hand is not None and dhand is not None:
			action = run_action(dhand, p2hand, "player2")

			if action:
				write_log(logwriter, [ time.time(), round, dhand, phand, p2hand, p1active, action, None ])

			if action != "stand":
				p2hand = None



		# split = pyautogui.locateOnScreen(image_dir + "split.png", grayscale=True, region=bregion)

		# if split is not None and splits.has_key(phand) and dhand in splits[phand]:
		# 	mouse = pyautogui.position()
		# 	pyautogui.moveTo(split[0], split[1], 0.25)
		# 	pyautogui.click(split[0], split[1])
		# 	pyautogui.moveTo(mouse[0], mouse[1], 0.25)
		# 	phand = None
		# 	p2hand = None

		# if doubles.has_key(phand) and dhand in doubles[phand]:
		# 	print "action: double down"
		# 	dd = pyautogui.locateCenterOnScreen(image_dir + "dd.png", grayscale=True, region=bregion)

		# 	if dd is None:
		# 		dd = pyautogui.locateCenterOnScreen(image_dir + "hit.png", grayscale=True, region=bregion)

		# 	if dd is not None:
		# 		mouse = pyautogui.position()
		# 		pyautogui.moveTo(dd[0], dd[1], 0.25)
		# 		pyautogui.click(dd[0], dd[1])
		# 		pyautogui.moveTo(mouse[0], mouse[1], 0.25)
		# 		phand = None

		# if hits.has_key(phand) and dhand in hits[phand]:
		# 	print "action: hit"
		# 	hit = pyautogui.locateCenterOnScreen(image_dir + "hit.png", grayscale=True, region=bregion)
		
		# 	if hit is not None:
		# 		mouse = pyautogui.position()
		# 		pyautogui.moveTo(hit[0], hit[1], 0.25)
		# 		pyautogui.click(hit[0], hit[1])
		# 		pyautogui.moveTo(mouse[0], mouse[1], 0.25)
		# 		phand = None

		# if stands.has_key(phand) and dhand in stands[phand]:
		# 	print "action: stand"
		# 	stand = pyautogui.locateCenterOnScreen(image_dir + "stand.png", grayscale=True, region=bregion)
		
		# 	if stand is not None:
		# 		mouse = pyautogui.position()
		# 		pyautogui.moveTo(stand[0], stand[1], 0.25)
		# 		pyautogui.click(stand[0], stand[1])
		# 		pyautogui.moveTo(mouse[0], mouse[1], 0.25)
