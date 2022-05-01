def calc(a,b,c,d,e):
	roi = (float(b) - float(a))/float(a)
	gain = float(b)-float(a)
	tier1 = float(d)/100
	tier2 = float(e)/100
	thresh = float(a)*float(c) 

	if roi < 0:
		return("0! This deal returned")

	elif roi <= float (c):
		return(gain*tier1)
	else:
		x = gain - thresh
		carry_tier2 = x*tier2 
		carry_tier1 = thresh*tier1
		total = carry_tier1 +carry_tier2
		return(total)


a = input("Enter Initial Investment: $")
b = input("Enter Distribution Amount: $")
c = input("Enter ROI Threshold:X")
d = input("Enter Carry Tier 1: %")
e = input("Enter Carry Tier 2:%")

answer = (calc(a,b,c,d,e))

print("DL will recieve: ${} from this deal".format(answer))