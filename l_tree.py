import argparse
import json
import turtle as ttl
import random

def main():
	print("Type 'python l_tree.py -h' or 'python l_tree.py --help' for usage options.")

	args = setArgs();

	axiom = "F"
	rules = {"F": "FF+[+F-F+F]-[-F+F-F]"}#"FF+[+F-F]-[-F+F-F]"}
	len = 100.0
	max_iter = 3
	angle = 25
	animate = False

	if args.axiom:
		axiom = args.axiom
	#if args.rules:
	#	rules = args.rules
	if args.len:
		len = args.len
	if args.iter:
		max_iter = args.iter
	if args.angle:
		angle = args.angle
	if args.noanim: 
		animate = True

	len *= 0.5**max_iter

	sentence = genPattern(axiom, rules, max_iter)
	turtleDraw(sentence, len, angle, animate)

	key = raw_input("Press any key to exit: ")



def setArgs():
	parser = argparse.ArgumentParser()
	parser.add_argument("-a", "--axiom", type=str, help="Specify the starting sequence of L-System generator.")
	#parser.add_argument("-r", "--rules", action='append', type=lambda kv: kv.split("="), dest='rules', help="Specify rule")
	parser.add_argument("-l", "--len", type=float, help="Length of each segment.")
	parser.add_argument("-i", "--iter", type=int, help="Number of iterations to apply rules to axiom. [Caution: For values greater than 4, use --noanim flag alongside]")
	parser.add_argument("-d", "--angle", type=float, help="Angle for turtle rotation in degrees.")
	parser.add_argument("--noanim", help="Do not animate turtle movements. [Caution: Do use this flag for 'iter' greater than 4]", action="store_true")

	return parser.parse_args()

def genPattern(axiom, rules, max_iter = 1):
	sentence = axiom
	for i in range(max_iter):
		nextSentence = ""
		for current in sentence:
			found = False
			for rule in rules:
				if current == rule:
					found = True
					nextSentence += rules[rule]
					break	
			if (not found):
				nextSentence += current
		sentence = nextSentence
	return sentence


def setup():
	random.seed(21)
	ttl.seth(90)
	ttl.goto(0, 0)
	ttl.clear()
	width = ttl.window_width()
	height = ttl.window_height()
	ttl.pu()
	ttl.bk(height / 2)

	ttl.colormode(255)
	ttl.pencolor((255,255,255))
	ttl.bgcolor((51,51,51))

	ttl.pd()
	ttl.speed("fastest")
	ttl.clear()



def push(stk):
	pos = ttl.pos()
	head = ttl.heading()
	dsct = {"pos": pos, "head": head}
	stk.append(dsct)


def pop(stk):
	dsct = stk.pop()
	pos = dsct["pos"]
	head = dsct["head"]
	ttl.pu()
	ttl.goto(pos)
	ttl.seth(head)
	ttl.pd()

def turtleDraw(sentence, len = 0.0, angle = 25, animate = False):
	stk = []

	if animate:
		ttl.tracer(0, 0)
	setup()

	for char in sentence:
		if char == "F":
			ttl.fd(len)
			#ttl.pencolor((random.randrange(55, 255),random.randrange(55, 255),random.randrange(55, 255)))
		elif char == "+":
			ttl.rt(angle)
		elif char == "-":
			ttl.lt(angle)
		elif char == "[":
			push(stk)
		elif char == "]":
			pop(stk)
	if animate:
		ttl.update()


main()