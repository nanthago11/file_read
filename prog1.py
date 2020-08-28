
import sys
import os
import re


#python prog1.py in.txt out1.txt a,about,above,after,again,against,all,am,an,and,any,are,aren't,as,at,be,because,been,before,being,below,between,both,but,by,can't,cannot,could,couldn't,did,didn't,do,does,doesn't,doing,don't,down,during,each,few,for,from,further,had,hadn't,has,hasn't,have,haven't,having,he,he'd,he'll,he's,her,here,here's,hers,herself,him,himself,his,how,how's,i,i'd,i'll,i'm,i've,if,in,into,is,isn't,it,it's,its,itself,let's,me,more,most,mustn't,my,myself,no,nor,not,of,off,on,once,only,or,other,ought,our,ours,ourselves,out,over,own,same,shan't,she,she'd,she'll,she's,should,shouldn't,so,some,such,than,that,that's,the,their,theirs,them,themselves,then,there,there's,these,they,they'd,they'll,they're,they've,this,those,through,to,too,under,until,up,very,was,wasn't,we,we'd,we'll,we're,we've,were,weren't,what,what's,when,when's,where,where's,which,while,who,who's,whom,why,why's,with,won't,would,wouldn't,you,you'd,you'll,you're,you've,your,yours,yourself,yourselves


#Steps
#Call script with input/output/exclude_list
#remove words in exclude_list that are present in input_file
#print output to output_file

def main():

	fileInputString=sys.argv[1]
	excludeList=sys.argv[3]
	fileOutputString=sys.argv[2]





	excludeList=excludeList.replace('\'', '')
	regex1='[^a-zA-Z 0-9,_]+'
	excludeList= re.sub(regex1, '', excludeList) .lower()
	SplitExcludeList = list(excludeList.split(","))
	print(SplitExcludeList)
	#SplitExcludeList.sort()
	WriteFile = open( os.path.join(os.getcwd() ,fileOutputString ), "w")
	with open( os.path.join(os.getcwd() , fileInputString ), "r" ) as f:
		for line in f:
			line=line.replace('\t', ' ')
			pline= re.sub(regex1, '', line) .lower()
			pline=pline.replace('\t', ' ')
			pline=pline.replace(' ', '~')
			DataArray = list(pline.split("~"))
			#DataArray.sort()
			FirstItemInArray=list(DataArray[0].split(" "))
			WriteFile.write("%s\t"%(" ".join(FirstItemInArray)))
			TempSet=list(set(DataArray) - set(SplitExcludeList))
			intList=list(set(TempSet)-set(FirstItemInArray))
			intList.sort()
			WriteFile.write("%s\n"%(" ".join(intList)))
	WriteFile.close()

main()
