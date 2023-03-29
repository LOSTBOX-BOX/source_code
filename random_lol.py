import random


team_1 = [] 
team_2=[]
end_team_1=[]
end_team_2=[]
ran_num = random.randint(1,5)

for i in range(5):
    while ran_num in team_1:
        ran_num = random.randint(1,5)
    team_1.append(ran_num)
for i in range(5):
    while ran_num in team_2:
        ran_num = random.randint(1,5)
    team_2.append(ran_num)

 
for i in range(1,3):
    if i==1:
        tmp=team_1
    else:
        tmp=team_2
        
    for j in range(0,5):
        tmp_str="err"
        if tmp[j]==1:
            tmp_str="탑  "
        elif tmp[j]==2:
            tmp_str="정글"
        elif tmp[j]==3:
            tmp_str="미드"
        elif tmp[j]==4:
            tmp_str="원딜"
        elif tmp[j]==5:
            tmp_str="서폿"

        if i==1:
            end_team_1.append(tmp_str)
        else:
            end_team_2.append(tmp_str)
 

for i in range(1,3):
        
    for j in range(0,5):
        ran_num = random.randint(1,7)
        tmp_str="err"
        if ran_num==1:
            tmp_str="극치명"
        elif ran_num==2:
            tmp_str="극공속"
        elif ran_num==3:
            tmp_str="극흡혈"
        elif ran_num==4:
            tmp_str="극탱 (방마저체력)"
        elif ran_num==5:
            tmp_str="극이속 신화템 고정 (터화탱 슈렐) / (기동신 신속)"
        elif ran_num==6:
            tmp_str="극방관"
        elif ran_num==7:
            tmp_str="올사용템"
        
        if i==1:
            end_team_1[j]=end_team_1[j]+" : "+tmp_str
        else:
            end_team_2[j]=end_team_2[j]+" : "+tmp_str
 

for i in range(1,3):
    for j in range(0,5):
        ran_num = random.randint(1,155)
        tmp_str="err"
        if ran_num==1:
            tmp_str="가렌"
        elif ran_num==2:
            tmp_str="갈리오"
        elif ran_num==3:
            tmp_str="갱플랭크"
        elif ran_num==4:
            tmp_str="그라가스"
        elif ran_num==5:
            tmp_str="그레이브즈"
        elif ran_num==6:
            tmp_str="그웬"
        elif ran_num==7:
            tmp_str="나르"
        elif ran_num==8:
            tmp_str="나미"
        elif ran_num==9:
            tmp_str="나서스"
        elif ran_num==10:
            tmp_str="노틸러스"
        elif ran_num==11:
            tmp_str="녹턴"
        elif ran_num==12:
            tmp_str="누누와 윌럼프"
        elif ran_num==13:
            tmp_str="니달리"
        elif ran_num==14:
            tmp_str="니코"
        elif ran_num==15:
            tmp_str="다리우스"
        elif ran_num==16:
            tmp_str="다이애나"
        elif ran_num==17:
            tmp_str="드레이븐"
        elif ran_num==18:
            tmp_str="라이즈"
        elif ran_num==19:
            tmp_str="라칸"
        elif ran_num==20:
            tmp_str="람머스"
        elif ran_num==21:
            tmp_str="럭스"
        elif ran_num==22:
            tmp_str="럼블"
        elif ran_num==23:
            tmp_str="레넥톤"
        elif ran_num==24:
            tmp_str="레오나"
        elif ran_num==25:
            tmp_str="렉사이"
        elif ran_num==26:
            tmp_str="렐"
        elif ran_num==27:
            tmp_str="렝가"
        elif ran_num==28:
            tmp_str="루시안"
        elif ran_num==29:
            tmp_str="룰루"
        elif ran_num==30:
            tmp_str="르블랑"
        elif ran_num==31:
            tmp_str="리신"
        elif ran_num==32:
            tmp_str="리븐"
        elif ran_num==33:
            tmp_str="리산드라"
        elif ran_num==34:
            tmp_str="릴리아"
        elif ran_num==35:
            tmp_str="마스터 이"
        elif ran_num==36:
            tmp_str="마오카이"
        elif ran_num==37:
            tmp_str="말자하"
        elif ran_num==38:
            tmp_str="말파이트"
        elif ran_num==39:
            tmp_str="모데카이저"
        elif ran_num==40:
            tmp_str="모르가나"
        elif ran_num==41:
            tmp_str="문도 박사"
        elif ran_num==42:
            tmp_str="미스 포츈"
        elif ran_num==43:
            tmp_str="바드"
        elif ran_num==44:
            tmp_str="바루스"
        elif ran_num==45:
            tmp_str="바이"
        elif ran_num==46:
            tmp_str="베이가"
        elif ran_num==47:
            tmp_str="베인"
        elif ran_num==48:
            tmp_str="벨코즈"
        elif ran_num==49:
            tmp_str="볼리베어"
        elif ran_num==50:
            tmp_str="브라움"
        elif ran_num==51:
            tmp_str="브랜드"
        elif ran_num==52:
            tmp_str="블라디미르"
        elif ran_num==53:
            tmp_str="블리츠크랭크"
        elif ran_num==54:
            tmp_str="비에고"
        elif ran_num==55:
            tmp_str="빅토르"
        elif ran_num==56:
            tmp_str="뽀삐"
        elif ran_num==57:
            tmp_str="사미라"
        elif ran_num==58:
            tmp_str="사이온"
        elif ran_num==59:
            tmp_str="사일러스"
        elif ran_num==60:
            tmp_str="샤코"
        elif ran_num==61:
            tmp_str="세나"
        elif ran_num==62:
            tmp_str="세라핀"
        elif ran_num==63:
            tmp_str="세주아니"
        elif ran_num==64:
            tmp_str="세트"
        elif ran_num==65:
            tmp_str="소나"
        elif ran_num==66:
            tmp_str="소라카"
        elif ran_num==67:
            tmp_str="쉔"
        elif ran_num==68:
            tmp_str="쉬바나"
        elif ran_num==69:
            tmp_str="스웨인"
        elif ran_num==70:
            tmp_str="스카너"
        elif ran_num==71:
            tmp_str="시비르"
        elif ran_num==72:
            tmp_str="신 짜오"
        elif ran_num==73:
            tmp_str="신드라"
        elif ran_num==74:
            tmp_str="신지드"
        elif ran_num==75:
            tmp_str="쓰레쉬"
        elif ran_num==76:
            tmp_str="아리"
        elif ran_num==77:
            tmp_str="아무무"
        elif ran_num==78:
            tmp_str="아우렐리온 솔"
        elif ran_num==79:
            tmp_str="아이번"
        elif ran_num==80:
            tmp_str="아지르"
        elif ran_num==81:
            tmp_str="아칼리"
        elif ran_num==82:
            tmp_str="아트록스"
        elif ran_num==83:
            tmp_str="아펠리오스"
        elif ran_num==84:
            tmp_str="알리스타"
        elif ran_num==85:
            tmp_str="애니"
        elif ran_num==86:
            tmp_str="애니비아"
        elif ran_num==87:
            tmp_str="애쉬"
        elif ran_num==88:
            tmp_str="야스오"
        elif ran_num==89:
            tmp_str="에코"
        elif ran_num==90:
            tmp_str="엘리스"
        elif ran_num==91:
            tmp_str="오공"
        elif ran_num==92:
            tmp_str="오른"
        elif ran_num==93:
            tmp_str="오리아나"
        elif ran_num==94:
            tmp_str="올라프"
        elif ran_num==95:
            tmp_str="요네"
        elif ran_num==96:
            tmp_str="요릭"
        elif ran_num==97:
            tmp_str="우디르"
        elif ran_num==98:
            tmp_str="우르곳"
        elif ran_num==99:
            tmp_str="워윅"
        elif ran_num==100:
            tmp_str="유미"
        elif ran_num==101:
            tmp_str="이렐리아"
        elif ran_num==102:
            tmp_str="이블린"
        elif ran_num==103:
            tmp_str="이즈리얼"
        elif ran_num==104:
            tmp_str="일라오이"
        elif ran_num==105:
            tmp_str="자르반 4세"
        elif ran_num==106:
            tmp_str="자야"
        elif ran_num==107:
            tmp_str="자이라"
        elif ran_num==108:
            tmp_str="자크"
        elif ran_num==109:
            tmp_str="잔나"
        elif ran_num==110:
            tmp_str="잭스"
        elif ran_num==111:
            tmp_str="제드"
        elif ran_num==112:
            tmp_str="제라스"
        elif ran_num==113:
            tmp_str="제이스"
        elif ran_num==114:
            tmp_str="조이"
        elif ran_num==115:
            tmp_str="직스"
        elif ran_num==116:
            tmp_str="진"
        elif ran_num==117:
            tmp_str="질리언"
        elif ran_num==118:
            tmp_str="징크스"
        elif ran_num==119:
            tmp_str="초가스"
        elif ran_num==120:
            tmp_str="카르마"
        elif ran_num==121:
            tmp_str="카밀"
        elif ran_num==122:
            tmp_str="카사딘"
        elif ran_num==123:
            tmp_str="카서스"
        elif ran_num==124:
            tmp_str="카시오페아"
        elif ran_num==125:
            tmp_str="카이사"
        elif ran_num==126:
            tmp_str="카직스"
        elif ran_num==127:
            tmp_str="카타리나"
        elif ran_num==128:
            tmp_str="칼리스타"
        elif ran_num==129:
            tmp_str="케넨"
        elif ran_num==130:
            tmp_str="케이틀린"
        elif ran_num==131:
            tmp_str="케인"
        elif ran_num==132:
            tmp_str="케일"
        elif ran_num==133:
            tmp_str="코그모"
        elif ran_num==134:
            tmp_str="코르키"
        elif ran_num==135:
            tmp_str="퀸"
        elif ran_num==136:
            tmp_str="클레드"
        elif ran_num==137:
            tmp_str="키아나"
        elif ran_num==138:
            tmp_str="킨드레드"
        elif ran_num==139:
            tmp_str="타릭"
        elif ran_num==140:
            tmp_str="탈론"
        elif ran_num==141:
            tmp_str="탈리야"
        elif ran_num==142:
            tmp_str="탐 켄치"
        elif ran_num==143:
            tmp_str="트런들"
        elif ran_num==144:
            tmp_str="트리스타나"
        elif ran_num==145:
            tmp_str="트린다미어"
        elif ran_num==146:
            tmp_str="트위스티드페이트"
        elif ran_num==147:
            tmp_str="트위치"
        elif ran_num==148:
            tmp_str="티모"
        elif ran_num==149:
            tmp_str="파이크"
        elif ran_num==150:
            tmp_str="판테온"
        elif ran_num==151:
            tmp_str="피들스틱"
        elif ran_num==152:
            tmp_str="피오라"
        elif ran_num==153:
            tmp_str="피즈"
        elif ran_num==154:
            tmp_str="하이머딩거"
        elif ran_num==155:
            tmp_str="헤카림"
        
        if i==1:
            end_team_1[j]=end_team_1[j]+" : "+tmp_str
        else:
            end_team_2[j]=end_team_2[j]+" : "+tmp_str

for i in range(1,3):
    if i==1:
        tmp=end_team_1
        print("1팀")
    else:
        tmp=end_team_2
        print("2팀")
    for j in range(0,5):
        print(tmp[j])
while(1):
    pass