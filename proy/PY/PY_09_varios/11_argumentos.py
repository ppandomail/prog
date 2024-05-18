# sin argparse --> se ejecuta, por ejemplo: python xxx.py 5 2 suma
import sys
import argparse

print(sys.argv)
for elem in sys.argv:
    print(elem)

# con argparse --> se ejecuta, por ejemplo: python xxx.py -a 5 -b 2 -o suma
# se puede alterar el orden de los args porque no son posicionales.

parse = argparse.ArgumentParser(description='Calculadora')
parse.add_argument('-a', '--num_a', type=int, help='Parametro a')
parse.add_argument('-b', '--num_b', type=int, help='Parametro b')
parse.add_argument('-o', '--oper', type=str,
                   choices=['suma', 'resta', 'multi'],
                   default='suma',
                   required=False,
                   help='Operacion a realizar con a y b')
args = parse.parse_args()
if args.oper == 'suma':
    print(args.num_a + args.num_b)
elif args.oper == 'resta':
    print(args.num_a - args.num_b)
else:
    print(args.num_a * args.num_b)
