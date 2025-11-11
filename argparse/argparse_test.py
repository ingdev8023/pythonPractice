import argparse
#using positional arguments

# parser = argparse.ArgumentParser()
# parser.add_argument('square', help='display a square of a given number',type= int)
# args = parser.parse_args()
# print(args.square**2)

#using optional arguments

# parser =  argparse.ArgumentParser()
# parser.add_argument("-v","--verbose", help='increase out verbosity', action='store_true')
# args = parser.parse_args()
# if args.verbose:
#     print('verbosity turned on')

# parser = argparse.ArgumentParser()
# parser.add_argument('square', type = int, help='display the square of any given number')
# parser.add_argument("-v",'--verbose',action='store_true', choices=[0, 1, 2], help='increase out verbosity')
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:

#     print(f"the square of {args.square} equals {answer}")
# else:
#     print(answer)

# parser = argparse.ArgumentParser()
# parser.add_argument('square', type = int, help='display the square of any given number')
# parser.add_argument("-v",'--verbose',action='count', help='increase out verbosity',default=0)
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity >= 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity >= 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)

# parser = argparse.ArgumentParser()
# parser.add_argument('x', type = int, help='the base')
# parser.add_argument('y', type = int, help='the exponent')
# parser.add_argument("-v",'--verbose',action='count', help='increase out verbosity',default=0)
# args = parser.parse_args()
# answer = args.x**args.y
# if args.verbose >= 2:
#     print(f"{args.x} to the power of {args.y} equals {answer}")
# elif args.verbose >= 1:
#     print(f"{args.x}^{args.y} == {answer}")
# else:
#     print(answer)

# parser = argparse.ArgumentParser(description="calculate X to the power of Y")
# parser.add_argument('x', type = int, help='the base')
# parser.add_argument('y', type = int, help='the exponent')
# parser.add_argument("-v",'--verbose',action='count', help='increase out verbosity',default=0)
# args = parser.parse_args()
# answer = args.x**args.y
# if args.verbose >= 2:
#     print(f"Running {__file__}")
# elif args.verbose >= 1:
#     print(f"{args.x}^{args.y} == {answer}")
# else:
#     print(answer)

parser = argparse.ArgumentParser(prog = "Tutorial program for the argparse module", description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")


