# encoding=utf8
import requests
import shutil
import xml.dom.minidom as minidom

xmlfile='bel.xml'
xml=minidom.parse(xmlfile)
items=xml.getElementsByTagName('C')
for s in items:
	try:
		conv=[]
		id_=s.attributes['id'].value

		name=s.attributes['n'].value
		for letter in name:
			letter.encode('ascii','ignore')
			conv.append(letter)
		
		imgname=xmlfile[4:7]+"_"+unicode(''.join(conv))+"_"+id_

		r=requests.get('http://smimgs.com/images/logos/clubs/'+str(id_)+".jpg",stream=True)

		if r.status_code==200:
			with open(str(imgname),'wb') as f:
				r.raw.decode_content=True
				shutil.copyfileobj(r.raw,f)
	except Exception as e:
		file_ = open("lost_club_logos.txt","a")
		file_.write(xmlfile[4:7]+"_"+id_) 
		file_.write("\n") 
		file_.close()
		pass
