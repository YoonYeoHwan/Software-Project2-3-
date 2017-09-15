#20171656 유성현
#Week3 SoftWare Poject assignment3
#test3_4.py을 수정하여 성적표 관리시스템을 보완함

import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
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
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            if len(parse) == 4:
                try:
                    record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                    scdb += [record]
                except ValueError: #정수가 아닌 다른 수를 입력했을 때 예외 처리
                    print("정수를 입력해주세요")
            else:
                print("이름, 나이, 점수를 알맞게 입력해주세요.")

        #del 명령 수정
        elif parse[0] == 'del':
            if len(parse) == 2:
                for i in scdb: #2중 for문으로 이름이 같은 모든 레코드 제거
                    for p in scdb:
                        if p['Name'] == parse[1]:
                                scdb.remove(p)

            else:
                print("이름을 정확히 입력해주세요.")

        # find 명령 추가
        elif parse[0] == 'find':
            if len(parse) == 2:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        for attr in p:
                            print(attr + "=" + str(p[attr]), end=' ')  # 주어진 name의 정보 출력
                        print('')
            else:
                print("이름을 정확히 입력해주세요.")

        # inc 명령 추가
        elif parse[0] == 'inc':
            if len(parse) == 3:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        try:
                            p['Score'] += int(parse[2])  # 입력한 값을 score 에 더해줌
                        except ValueError: #정수가 아닌 값을 입력했을 때 예외처리
                            print("정수를 입력해주세요.")
            else:
                print("이름과 점수를 알맞게 입력해주세요.")


        elif parse[0] == 'show':
            try:
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            except KeyError: #다른 값을 넣었을 때 발생하는 에러 처리
                print("Name, Score, Age 중에 선택하여 입력해주세요.")

        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb,reverse=True, key=lambda person: person[keyname]): #보기 편하게 높은 순서대로 보기위해 역순으로 바꿈
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
