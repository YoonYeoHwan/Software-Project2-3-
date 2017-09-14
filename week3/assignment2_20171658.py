# find, increase 추가
# del 수정, 같은 이름의 모든 사람이 지워지도록
# 예외처리 최대한 많이

import pickle

dbfilename = 'assignment2_20171658.dat'

def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb =  pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
	while(True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
			scdb += [record]
		elif parse[0] == 'del':
			for p in scdb:
				if p['Name'] == parse[1]:
					scdb.remove(p)
				for p in scdb:
					if p['Name'] == parse[1]:
						scdb.remove(p)
        # for 반복문을 한번만 돌리니깐 최대 2개밖에 지워지지 않아서 for 반복문을 두번 사용함
		elif parse[0] == 'find':
			for p in scdb:
				if p['Name'] == parse[1]:
					print('Age='+p['Age'], 'Name='+p['Name'], 'Score='+p['Score'])
		# for 반복문을 사용하여 입력받은 이름이 존재하는지 검색
		# 존재하면 이름, 나이, 점수를 출력
		# 존재하지 않으면 -
		elif parse[0] == 'inc':
			for p in scdb:
				if p['Name'] == parse[1]:
					incScore = int(input("Score input : "))
					p['Score'] = int(p['Score'])
					p['Score'] += incScore
					p['Score'] = str(p['Score'])
		# for 반복문을 사용하여 입력받은 이름이 존재하는지 검색
		# 존재하면 증가시킬 점수를 입력 받음
		# 스트링 타입으로 되어있는 점수를 정수 타입으로 바꾸어 주고 입력 받은 점수를 더해줌
		# 정수 타입으로 바꾸었던 점수를 다시 스트링 타입으로 바꿔줌
		elif parse[0] == 'show':
			sortKey ='Name' if len(parse) == 1 else parse[1]
			showScoreDB(scdb, sortKey)
		elif parse[0] == 'quit':
			break
		else:
			print("Invalid command: " + parse[0])
			

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + p[attr], end=' ')
		print()
	


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

