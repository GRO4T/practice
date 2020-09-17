#! python3
# logging_module.py - Example of using logging module
# For more information go to Automate Boring Stuff With Python page 221

import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = ' %(asctime)s -  %(levelname)s -  %(message)s')

logging.debug('Start of program')

def factorial(n):
  logging.debug('Start of factorial(%s)' % (n))
  total = 1
  for i in range(n + 1):
    total *= i
    logging.debug('i is ' + str(i) + ', total is ' + str(total))
  logging.debug('End of factorial(%s)' % (n))
  return total

print(factorial(5))

logging.debug('End of program')
