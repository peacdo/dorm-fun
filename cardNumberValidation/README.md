# cardNumberValidation

Card numbers are created with respect to the Luhn Algorithm, a program or script can check if the credit card is valid or not with reversing the Luhn Algoritm. In order to do it we should follow this steps:

    1. Double every second digit from right to left.
    2. If doubled numbere is higher or superior than 10, get the sum of its digits.
    3. Add all single digits from step 2.
    4. Add all odd numbered digits from right to left.
    5. Sum rusults o 3 & 4.
    6. If the result of step 5 is divisble by 10, card number is valid.

Valid card numbers for testing:
	378282246310005
	371449635398431
	6011111111111117
	6331101999990016
	76009244561
	38520000023237