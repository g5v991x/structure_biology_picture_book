import sys
fname=sys.argv[-1]
print(fname)

f=open(fname,'r')
lines=f.readlines()
f.close()

lines=[l for l in lines if 'd="' in l]
txt=''.join(lines)

pos=-1
paths=[]
for i in range(100):
	pos=txt.find('d="', pos+1)
	if pos<0:
		break

	p1=txt.find('/>', pos)
	print(txt[pos:p1])
	paths.append(txt[pos:p1])

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

output="""
{::nomarkdown}
<div class='imageWrapper'>
<img class="image0" src="{{ site.baseurl }}/assets/images/kasia_00.jpg" alt="place holder">
<svg viewBox="0 0 160 90" class='image-area'>
<!--#######################-->
<defs>"""

for i,path in enumerate(paths):
	o=f"""
<mask id="myMask_{i}"><rect width="100%" height="100%" fill="white"/>
  <path id="path_{i}" class="path" {path}/></mask>"""
	output+=o

output+="\n</defs>\n<!--#######################-->"

for i,path in enumerate(paths):
	o=f'\n<rect mask="url(#myMask_{i})" class="background" id="background_{i}"/>'
	output+=o

output+="\n<!--#######################-->"

for i,path in enumerate(paths):
	o=f'\n<use href="#path_{i}" class="shape" id="select_{i}"/>'
	output+=o

output+="\n</svg>\n<!--#######################-->"
for i,path in enumerate(paths):
	o=f'\n<div class="overlay" id="textbox_{i}" ><b> Label_{i} </b></div>'
	output+=o

output+="\n</div>\n{:/}"
print(output)



