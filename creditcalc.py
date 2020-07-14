import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("--type")
parser.add_argument("--principal", type=int, default=0)
parser.add_argument("--periods", type=int, default=0)
parser.add_argument("--payment", type=int, default=0)
parser.add_argument("--interest", type=float, default=0)

args = parser.parse_args()

args.interest = args.interest / (12 * 100)

if args.type != "diff" and args.type != "annuity" or args.interest <= 0\
   or args.principal <= 0 and (args.periods <= 0 or args.payment <= 0)\
   or args.periods <= 0 and (args.principal <= 0 or args.payment <= 0)\
   or args.payment <= 0 and (args.principal <= 0 or args.periods <= 0):
    print("Incorrect parameters")
elif args.type == "diff":
    if args.payment != 0:
        print("Incorrect parameters")
    else:
        all_payments = 0
        for i in range(1, args.periods + 1):
            d = math.ceil(args.principal / args.periods+args.interest
                          * (args.principal-(args.principal*(i-1)/args.periods)))
            all_payments += d
            print(f"Month {i}: paid out {d}")
        print()
        print(f"Overpayment = {math.ceil(all_payments - args.principal)}")
elif args.type == "annuity":
    if args.principal == 0:
        args.principal = args.payment / (args.interest * math.pow(1 + args.interest, args.periods)
                                         / (math.pow(1 + args.interest, args.periods) - 1))
        print(f'Your credit principal = {math.floor(args.principal)}!')
    elif args.payment == 0:
        args.payment = math.ceil(args.principal * ((args.interest * math.pow(1 + args.interest, args.periods))
                                 / (math.pow(1 + args.interest, args.periods) - 1)))
        print(f'Your annuity payment = {args.payment}!')
    elif args.periods == 0:
        args.periods = math.ceil(math.log(args.payment / (args.payment - (args.interest
                                 * args.principal)), 1 + args.interest))
        years = args.periods // 12
        months = args.periods - years * 12
        if months % 12 == 0:
            print(f'You need {years} years to repay this credit!')
        elif months < 12 and years == 0:
            print(f'You need {months} months to repay this credit!')
        else:
            print(f'You need {years} years and {months} months to repay this credit!')
    print(f"Overpayment = {math.ceil(args.payment * args.periods - args.principal)}")
