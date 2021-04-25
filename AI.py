# بسم الله الرحمن الرحیم
# اللّهُ لاَ إِلَهَ إِلاَّ هُوَ الْحَیُّ الْقَیُّومُ لاَ تَأْخُذُهُ سِنَهٌ وَ لاَ نَوْمٌ
# مَن ذَا الَّذِی یَشْفَعُ عِنْدَهُ إِلاَّ بِإِذْنِهِ یَعْلَمُ مَا بَیْنَ أَیْدِیهِمْ وَ مَا خَلْفَهُمْ
# وَ لاَ یُحِیطُونَ بِشَیْءٍ مِّنْ عِلْمِهِ إِلاَّ بِمَا شَاء
# وَسِعَ کُرْسِیُّهُ السَّمَاوَاتِ وَ الأَرْضَ وَ لاَ یَؤُودُهُ حِفْظُهُمَا
# وَ هُوَ الْعَلِیُّ الْعَظِیمُ
# لاَ إِکْرَاهَ فِی الدِّینِ قَد تَّبَیَّنَ الرُّشْدُ مِنَ الْغَیِّ
# فَمَنْ یَکْفُرْ بِالطَّاغُوتِ وَ یُؤمِن بِاللّهِ
# فَقَدِ اسْتَمْسَکَ بِالْعُرْوَهِ الْوُثْقَیَ لاَ انفِصَامَ لَهَا
# وَاللّهُ سَمِیعٌ عَلِیمٌ
# اللّهُ وَلِیُّ الَّذِینَ آمَنُواْ یُخْرِجُهُم مِّنَ الظُّلُمَاتِ إِلَی النُّوُرِ
# وَالَّذِینَ کَفَرُواْ أَوْلِیَآؤُهُمُ الطَّاغُوتُ
# یُخْرِجُونَهُم مِّنَ النُّورِ إِلَی الظُّلُمَات
# أُوْلَئِکَ أَصْحَابُ النَّارِ هُمْ فِیهَا خَالِدُونَ


from Model import *
import random
import numpy as np
import json
from typing import *
from time import time
from operator import itemgetter, attrgetter
c_b = []
c_a = []
llll=[]
base_view = []
actual_view=[]
c_i=[]
maghsad_stra=[]
catm=[]
stra=[]
my_ants=[]
other_id=[]
turn_number=[]
maghar_harif=[]
istgah=[]
ist=[]
ist_2=[]
paygah_man=[]
paygah_por=[]
class AI:
    def __init__(self):
        self.game: Game = None
        self.message: str = None
        self.direction: int = None
        self.value: int = None
    def turn(self) -> (str, int, int):
        Height = self.game.mapHeight
        Width = self.game.mapWidth
        if len(c_b) < 1:
            for i in range(Width):
                l = []
                for j in range(Height):
                    u = []
                    for k in range(11):
                        if k == 9:
                            p = []
                            u.append(p)
                        elif k == 0:
                            u.append(-1)
                        else:
                            u.append(0)
                    l.append(u)
                base_view.append(l)
            c_b.append(0)
        if len(c_a) < 1:
            for i in range(Width):
                l = []
                for j in range(Height):
                    u = []
                    for k in range(11):
                        if k == 9:
                            p = []
                            u.append(p)
                        elif k == 0:
                            u.append(-1)
                        else:
                            u.append(0)
                    l.append(u)
                actual_view.append(l)
            c_a.append(0)
        if len(c_i) == 0:
            i = 0
            while i == 0:
                id = random.randint(0, 100)
                if id not in other_id:
                    c_i.append(id)
                    other_id.append(id)
                    i = 1
        me=A_I(self.game.ant.currentX,self.game.ant.currentY,c_i[0],self.game.ant.currentResource.type,self.game.ant.currentResource.value,self.game.ant.antType,self.game.ant.health)
        if len(my_ants)==0:
            me=A_I(self.game.ant.currentX,self.game.ant.currentY,c_i[0],self.game.ant.currentResource.type,self.game.ant.currentResource.value,self.game.ant.antType,self.game.ant.health)
            my_ants.append(me)
        else:
            for a in my_ants:
                if a.id==c_i[0]:
                    me=a
        if len(self.game.chatBox.allChats) > 0:
            t=self.game.chatBox.allChats[len(self.game.chatBox.allChats) - 1].turn
            for u in range(t):
                fkjf=0
                if len(turn_number)<(u+1):
                    for j in range(len(self.game.chatBox.allChats)):
                        if self.game.chatBox.allChats[j].turn == (u+1):
                            if len(self.game.chatBox.allChats[j].text)>1:
                                i = 0
                                r = 0
                                for chsr in self.game.chatBox.allChats[j].text:
                                    d = ord(chsr)
                                    r = r + int(bin(d)[2:]) * pow(10, i * 14)
                                    i = i + 1
                                f = str(r)
                                f = f[::-1]
                                i = 0
                                x = 0
                                y = 0
                                stratgy = 0
                                id = 0
                                h = 0
                                ant_type = 0
                                resors = 0
                                x_hadaf = 0
                                y_hadaf = 0
                                x_ist = 0
                                y_ist = 0
                                c_ist = 0
                                list_cell = []
                                cell = []
                                ant = []
                                i = 0
                                for o in f:
                                    if i < 6:
                                        x = x + int(o) * pow(2, i)
                                    if 5 < i < 12:
                                        y = y + int(o) * pow(2, i - 6)
                                    if 11 < i < 16:
                                        stratgy = stratgy + int(o) * pow(2, i - 12)
                                    if 15 < i < 17:
                                        ant_type = ant_type + int(o) * pow(2, i - 16)
                                    if 16 < i < 18:
                                        resors = resors + int(o) * pow(2, i - 17)
                                    if 17 < i < 20:
                                        h = h + int(o) * pow(2, i - 18)
                                    if 19 < i < 27:
                                        id = id + int(o) * pow(2, i - 20)
                                    if 26 < i < 33:
                                        x_hadaf = x_hadaf + int(o) * pow(2, i - 27)
                                    if 32 < i < 39:
                                        y_hadaf = y_hadaf + int(o) * pow(2, i - 33)
                                    if 38 < i < 45:
                                        x_ist = x_ist + int(o) * pow(2, i - 39)
                                    if 44 < i < 51:
                                        y_ist = y_ist + int(o) * pow(2, i - 45)
                                    if 50 < i < 54:
                                        c_ist = c_ist + int(o) * pow(2, i - 51)

                                    if i > 53:
                                        if ((i - 54) % 27) == 0:
                                            j = 0
                                            x_cell = 0
                                            y_cell = 0
                                            k = 0
                                            s = 0
                                            type_cell = 0
                                            type_res = 0
                                            val_res = 0
                                            cell = []
                                            khat = 0
                                            ccc = 0
                                            if j < 6:
                                                x_cell = x_cell + int(o) * pow(2, j)
                                        if j < 6 and j != 0:
                                            x_cell = x_cell + int(o) * pow(2, j)
                                        if 5 < j < 12:
                                            y_cell = y_cell + int(o) * pow(2, j - 6)
                                        if 11 < j < 13:
                                            k = k + int(o) * pow(2, j - 12)
                                        if 12 < j < 16:
                                            s = s + int(o) * pow(2, j - 13)
                                        if 15 < j < 18:
                                            type_cell = type_cell + int(o) * pow(2, j - 16)
                                        if 17 < j < 19:
                                            type_res = type_res + int(o) * pow(2, j - 18)
                                        if 18 < j < 23:
                                            val_res = val_res + int(o) * pow(2, j - 19)
                                        if 22 < j < 24:
                                            khat = khat + int(o) * pow(2, j - 23)
                                        if 23 < j < 27:
                                            ccc = ccc + int(o) * pow(2, j - 24)
                                        if (j % 27) == 26 or i == (len(f) - 1):
                                            cell.append(x_cell)
                                            cell.append(y_cell)
                                            cell.append(k)
                                            cell.append(s)
                                            cell.append(type_cell)
                                            cell.append(type_res)
                                            cell.append(val_res)
                                            cell.append(khat)
                                            cell.append(ccc)
                                            list_cell.append(cell)
                                        j = j + 1
                                    i = i + 1
                                ant.append(x)
                                ant.append(y)
                                ant.append(stratgy)
                                ant.append(ant_type)
                                ant.append(resors)
                                ant.append(h)
                                ant.append(id)
                                ant.append(x_hadaf)
                                ant.append(y_hadaf)
                                ant.append(x_ist)
                                ant.append(y_ist)
                                ant.append(c_ist)
                                if ant[6]==c_i[0]:
                                   catm.append([ant[7],ant[8]])
                                ty=u+1
                                for r in list_cell:
                                    xxxx = r[0]
                                    yyy = r[1]
                                    # -1 دیده نشده
                                    # 0 بیس خودی
                                    # 1 خونه خالی
                                    # 2 دیوار
                                    # 3 بیس دشمن
                                    actual_view[xxxx][yyy][0] = r[4]
                                    if r[5] == 1:
                                        if r[6] == 0:
                                            actual_view[xxxx][yyy][1] = 0
                                        if r[6] == 1:
                                            actual_view[xxxx][yyy][1] = 10
                                        if r[6] == 2:
                                            actual_view[xxxx][yyy][1] = 20
                                        if r[6] == 3:
                                            actual_view[xxxx][yyy][1] = 30
                                        if r[6] == 4:
                                            actual_view[xxxx][yyy][1] = 40
                                        if r[6] == 5:
                                            actual_view[xxxx][yyy][1] = 50
                                        if r[6] == 6:
                                            actual_view[xxxx][yyy][1] = 60
                                        if r[6] == 7:
                                            actual_view[xxxx][yyy][1] = 70
                                        if r[6] == 8:
                                            actual_view[xxxx][yyy][1] = 80
                                        if r[6] == 9:
                                            actual_view[xxxx][yyy][1] = 90
                                        if r[6] == 10:
                                            actual_view[xxxx][yyy][1] = 100
                                        if r[6] == 11:
                                            actual_view[xxxx][yyy][1] = 100
                                    elif r[5] == 0:
                                        if r[6] == 0:
                                            actual_view[xxxx][yyy][2] = 0
                                        if r[6] == 1:
                                            actual_view[xxxx][yyy][2] = 10
                                        if r[6] == 2:
                                            actual_view[xxxx][yyy][2] = 20
                                        if r[6] == 3:
                                            actual_view[xxxx][yyy][2] = 30
                                        if r[6] == 4:
                                            actual_view[xxxx][yyy][2] = 40
                                        if r[6] == 5:
                                            actual_view[xxxx][yyy][2] = 50
                                        if r[6] == 6:
                                            actual_view[xxxx][yyy][2] = 60
                                        if r[6] == 7:
                                            actual_view[xxxx][yyy][2] = 70
                                        if r[6] == 8:
                                            actual_view[xxxx][yyy][2] = 80
                                        if r[6] == 9:
                                            actual_view[xxxx][yyy][2] = 90
                                        if r[6] == 10:
                                            actual_view[xxxx][yyy][2] = 100
                                        if r[6] == 11:
                                            actual_view[xxxx][yyy][2] = 100
                                    # کارگر حریف
                                    actual_view[xxxx][yyy][4] = r[2]
                                    # سرباز حریف
                                    actual_view[xxxx][yyy][6] = r[3]
                                    actual_view[xxxx][yyy][7] = ty
                                    actual_view[xxxx][yyy][8] = r[7]
                                    actual_view[xxxx][yyy][10] = r[8]
                                if len(other_id) > 0:
                                    if ant[6] not in other_id:
                                        other_id.append(ant[6])
                                for i in actual_view:
                                    for j in i:
                                        if len(j[9]) > 0:
                                            for e in j[9]:
                                                if e.id == ant[6]:
                                                    j[9].remove(e)
                                p = 0
                                actual_view[ant[9]][ant[10]][10] = ant[11]
                                if len(my_ants) > 0:
                                    for niro in list(my_ants):
                                        if niro.id == ant[6] and niro.id != c_i[0]:
                                            niro.loc_x = ant[0]
                                            niro.loc_y = ant[1]
                                            niro.Resource_type = ant[4]
                                            niro.Resource_value = ant[4]
                                            niro.antType = ant[3]
                                            niro.health = ant[5]
                                            niro.id = ant[6]
                                            niro.maghsad = [ant[7], ant[8]]
                                            niro.strategy = ant[2]
                                            niro.tern = ty
                                            actual_view[ant[0]][ant[1]][9].append(niro)
                                            p = 1

                                    for niro in list(my_ants):
                                        if ty - niro.tern > 15:
                                            my_ants.remove(niro)
                                if p == 0 and ant[6] != c_i[0]:
                                    me = A_I(ant[0], ant[1], ant[6], ant[4], ant[4], ant[3],
                                             ant[5])
                                    me.maghsad = [ant[7], ant[8]]
                                    me.strategy = ant[2]
                                    my_ants.append(me)
                                    actual_view[ant[0]][ant[1]][9].append(me)
                                ty = u + 1
                                for r in list_cell:
                                    xxxx = r[0]
                                    yyy = r[1]
                                    # -1 دیده نشده
                                    # 0 بیس خودی
                                    # 1 خونه خالی
                                    # 2 دیوار
                                    # 3 بیس دشمن
                                    base_view[xxxx][yyy][0] = r[4]
                                    if r[5] == 1:
                                        if r[6] == 0:
                                            base_view[xxxx][yyy][1] = 0
                                        if r[6] == 1:
                                            base_view[xxxx][yyy][1] = 10
                                        if r[6] == 2:
                                            base_view[xxxx][yyy][1] = 20
                                        if r[6] == 3:
                                            base_view[xxxx][yyy][1] = 30
                                        if r[6] == 4:
                                            base_view[xxxx][yyy][1] = 40
                                        if r[6] == 5:
                                            base_view[xxxx][yyy][1] = 50
                                        if r[6] == 6:
                                            base_view[xxxx][yyy][1] = 60
                                        if r[6] == 7:
                                            base_view[xxxx][yyy][1] = 70
                                        if r[6] == 8:
                                            base_view[xxxx][yyy][1] = 80
                                        if r[6] == 9:
                                            base_view[xxxx][yyy][1] = 90
                                        if r[6] == 10:
                                            base_view[xxxx][yyy][1] = 100
                                        if r[6] == 11:
                                            base_view[xxxx][yyy][1] = 100
                                    elif r[5] == 0:
                                        if r[6] == 0:
                                            base_view[xxxx][yyy][2] = 0
                                        if r[6] == 1:
                                            base_view[xxxx][yyy][2] = 10
                                        if r[6] == 2:
                                            base_view[xxxx][yyy][2] = 20
                                        if r[6] == 3:
                                            base_view[xxxx][yyy][2] = 30
                                        if r[6] == 4:
                                            base_view[xxxx][yyy][2] = 40
                                        if r[6] == 5:
                                            base_view[xxxx][yyy][2] = 50
                                        if r[6] == 6:
                                            base_view[xxxx][yyy][2] = 60
                                        if r[6] == 7:
                                            base_view[xxxx][yyy][2] = 70
                                        if r[6] == 8:
                                            base_view[xxxx][yyy][2] = 80
                                        if r[6] == 9:
                                            base_view[xxxx][yyy][2] = 90
                                        if r[6] == 10:
                                            base_view[xxxx][yyy][2] = 100
                                        if r[6] == 11:
                                            base_view[xxxx][yyy][2] = 100
                                    # کارگر حریف
                                    base_view[xxxx][yyy][4] = r[2]
                                    # سرباز حریف
                                    base_view[xxxx][yyy][6] = r[3]
                                    base_view[xxxx][yyy][7] = ty
                                    base_view[xxxx][yyy][8] = r[7]
                                    base_view[xxxx][yyy][10] = r[8]
                                if len(other_id) > 0:
                                    if ant[6] not in other_id:
                                        other_id.append(ant[6])
                                for i in base_view:
                                    for j in i:
                                        if len(j[9]) > 0:
                                            for e in j[9]:
                                                if e.id == ant[6]:
                                                    j[9].remove(e)
                                p = 0
                                base_view[ant[9]][ant[10]][10] = ant[11]
                                if len(my_ants) > 0:
                                    for niro in list(my_ants):
                                        if niro.id == ant[6] and niro.id != c_i[0]:
                                            niro.loc_x = ant[0]
                                            niro.loc_y = ant[1]
                                            niro.Resource_type = ant[4]
                                            niro.Resource_value = ant[4]
                                            niro.antType = ant[3]
                                            niro.health = ant[5]
                                            niro.id = ant[6]
                                            niro.maghsad = [ant[7], ant[8]]
                                            niro.strategy = ant[2]
                                            niro.tern = ty
                                            base_view[ant[0]][ant[1]][9].append(niro)
                                            p = 1

                                    for niro in list(my_ants):
                                        if ty - niro.tern > 15:
                                            my_ants.remove(niro)
                                if p == 0 and ant[6] != c_i[0]:
                                    me = A_I(ant[0], ant[1], ant[6], ant[4], ant[4], ant[3],
                                             ant[5])
                                    me.maghsad = [ant[7], ant[8]]
                                    me.strategy = ant[2]
                                    my_ants.append(me)
                                    base_view[ant[0]][ant[1]][9].append(me)

                                fkjf=1
                if fkjf==1:
                   turn_number.append(1)
        t=len(turn_number)
        q = self.game.ant.visibleMap.cells
        R = []
        for h in q:
            for f in h:
                if f is not None:
                    R.append(f)
        for r in R:
            xxxx = r.x
            yyy = r.y
            # -1 دیده نشده
            # 0 بیس خودی
            # 1 خونه خالی
            # 2 دیوار
            # 3 بیس دشمن
            if r.type == 0:
                if self.game.baseX == xxxx and self.game.baseY == yyy:
                    actual_view[xxxx][yyy][0] = 0
                else:
                    actual_view[xxxx][yyy][0] = 3
            else:
                actual_view[xxxx][yyy][0] = r.type
            if r.resource_type == 2:
                actual_view[xxxx][yyy][1] = 0
                actual_view[xxxx][yyy][2] = 0

            if r.resource_type == 1:
                actual_view[xxxx][yyy][1] = r.resource_value

            elif r.resource_type == 0:
                actual_view[xxxx][yyy][2] = r.resource_value

            # کارگر خودی
            actual_view[xxxx][yyy][3] = 0
            # کارگر حریف
            actual_view[xxxx][yyy][4] = 0
            # سرباز خودی
            actual_view[xxxx][yyy][5] = 0
            # سرباز حریف
            actual_view[xxxx][yyy][6] = 0
            Ants = r.ants
            for mor in Ants:
                if mor.antType == 1:
                    if mor.antTeam == 0:
                        actual_view[xxxx][yyy][3] = actual_view[xxxx][yyy][3] + 1
                    elif mor.antTeam == 1:
                        actual_view[xxxx][yyy][4] = actual_view[xxxx][yyy][4] + 1
                elif mor.antType == 0:
                    if mor.antTeam == 0:
                        actual_view[xxxx][yyy][5] = actual_view[xxxx][yyy][5] + 1
                    elif mor.antTeam == 1:
                        actual_view[xxxx][yyy][6] = actual_view[xxxx][yyy][6] + 1
            if len(self.game.chatBox.allChats) == 0:
                actual_view[xxxx][yyy][7] = 1
            else:
                # ترن آپدیت شده
                actual_view[xxxx][yyy][7] = self.game.chatBox.allChats[len(self.game.chatBox.allChats) - 1].turn + 1
            if actual_view[xxxx][yyy][5] >= actual_view[xxxx][yyy][10]:
                actual_view[xxxx][yyy][10] = 0
        for r in R:
            xxxx = r.x
            yyy = r.y
            if dang(xxxx, yyy, self.game.ant.attackDistance, actual_view) > 0:
                actual_view[xxxx][yyy][8] = 1
        for i in actual_view:
            for j in i:
                if len(j[9]) > 0:
                    for e in j[9]:
                        if e.id == c_i[0]:
                            j[9].remove(e)
        if len(my_ants) > 0:
            for niro in my_ants:
                if niro.id == c_i[0]:
                    if len(maghsad_stra) > 0 and len(stra) > 0:
                        niro.loc_x = self.game.ant.currentX
                        niro.loc_y = self.game.ant.currentY
                        niro.id = c_i[0]
                        niro.Resource_type = self.game.ant.currentResource.type
                        niro.Resource_value = self.game.ant.currentResource.value
                        niro.antType = self.game.ant.antType
                        niro.health = self.game.ant.health
                        niro.tern = t
                        niro.maghsad = maghsad_stra[len(maghsad_stra) - 1]
                        niro.strategy = stra[len(stra) - 1]
                    else:
                        niro.loc_x = self.game.ant.currentX
                        niro.loc_y = self.game.ant.currentY
                        niro.id = c_i[0]
                        niro.Resource_type = self.game.ant.currentResource.type
                        niro.Resource_value = self.game.ant.currentResource.value
                        niro.antType = self.game.ant.antType
                        niro.health = self.game.ant.health
                    actual_view[self.game.ant.currentX][self.game.ant.currentY][9].append(niro)
        for i in actual_view:
            for j in i:
                if t - j[7] > 5:
                    j[8] = 0
                    j[3] = 0
                    # کارگر حریف
                    j[4] = 0
                    # سرباز خودی
                    j[5] = 0
                    # سرباز حریف
                    j[6] = 0
                if t - j[7] > 10:
                    j[9] = []
        actmat = actual_view
        basmat = base_view
        graph = MASIR(actmat)
        graph.run(graph.nodes[self.game.ant.currentX][self.game.ant.currentY])
        if len(istgah) == 0:
            for j in range(4):
                for i in range(4):
                    if self.game.baseX - 2 + i>=0 and self.game.baseX - 2 + i<self.game.mapWidth:
                        if self.game.baseY - 2 + j>=0 and self.game.baseY - 2 + j<self.game.mapHeight:
                            if actual_view[self.game.baseX - 2 + i][self.game.baseY - 2 + j][0] != 2 and actual_view[self.game.baseX - 2 + i][self.game.baseY - 2 + j][0] != 0:
                                if 0<len(graph.get_path(graph.nodes[self.game.baseX - 2 + i][self.game.baseY - 2 + j]))<4:
                                    istgah.append([self.game.baseX - 2 + i, self.game.baseY - 2 + j])
                                if len(istgah) > 2:
                                    break
                if len(istgah) > 2:
                    break
            if len(istgah)==0:
                istgah.append([self.game.baseX,self.game.baseY])
        if len(maghar_harif)==0:
            for i, k in enumerate(actmat):
                for j, g in enumerate(k):
                    if g[0]==3:
                        maghar_harif.append([i,j])
        p=0
        if self.game.ant.antType == 1:
            if self.game.ant.currentResource.value>4:
                x = self.game.baseX
                y = self.game.baseY
                path = graph.get_path(graph.nodes[x][y])
                if len(path)>0:
                    if len(path) == 1:
                        cc = path[0]
                    else:
                        cc = path[1]
                if len(my_ants) > 0:
                    for a in my_ants:
                        if a.id == c_i[0]:
                            a.maghsad = [self.game.baseX,self.game.baseY]
                            a.strategy = 0
                maghsad_stra.append([self.game.baseX,self.game.baseY])
                stra.append(0)
                self.direction = dirr(Width, Height, self.game.ant.currentX, self.game.ant.currentY, cc[0], cc[1]).value
                p = 1
            if p==0 :
                candids = []
                best_score = 10000
                best_candid = []
                best_path = None
                dis_of_base = graph.get_path(graph.nodes[self.game.baseX][self.game.baseY])
                current_recorse_type = self.game.ant.currentResource.type
                current_recorse_val = self.game.ant.currentResource.value
                for i, j in enumerate(actual_view):
                    for k, l in enumerate(j):
                        if l[0] != 2:
                            if current_recorse_type == 1:
                                if l[1] > 0:
                                    path = graph.get_path(graph.nodes[i][k])
                                    if len(path) > 1:
                                        g = 0
                                        for an in my_ants:
                                            if an.antType == 1 and an.maghsad == [i, k] and an.id < c_i[0]:
                                                g = g + 10
                                        if l[1] != 0:
                                            d = l[1]
                                        else:
                                            d = l[2]
                                        if g <= d:
                                            # dis = distance(self.game.mapWidth, self.game.mapHeight, i, k, self.game.baseX, self.game.baseY)*2
                                            if l[1] != 0:
                                                danger = dang(i, k, 4, actual_view) - anti_dang(i, k,4,actual_view)
                                                candid = [i, k, len(path) + len(dis_of_base), 1]
                                                if candid[2] < best_score:
                                                    best_candid = candid
                                                    best_score = candid[2]
                                                    best_path = [candid[0], candid[1]]
                                                    candids.append(candid)
                                            if l[2] != 0:
                                                danger = dang(i, k, 4, actual_view) - anti_dang(i, k,
                                                                                                           4,
                                                                                                           actual_view)
                                                candid = [i, k, len(path) + len(dis_of_base), 2]
                                                if candid[2] < best_score:
                                                    best_candid = candid
                                                    best_score = candid[2]
                                                    best_path = [candid[0], candid[1]]
                                                    candids.append(candid)
                            if current_recorse_type == 0:
                                if l[2] > 0:
                                    path = graph.get_path(graph.nodes[i][k])
                                    if len(path) > 1:
                                        g = 0
                                        for an in my_ants:
                                            if an.antType == 1 and an.maghsad == [i, k] and an.id < c_i[0]:
                                                g = g + 10
                                        if l[1] != 0:
                                            d = l[1]
                                        else:
                                            d = l[2]
                                        if g <= d:

                                            if l[1] != 0:
                                                danger = dang(i, k, 4, actual_view) - anti_dang(i, k,4,actual_view)
                                                candid = [i, k, len(path) + len(dis_of_base), 1]
                                                if candid[2] < best_score:
                                                    best_candid = candid
                                                    best_score = candid[2]
                                                    best_path = [candid[0], candid[1]]
                                                    candids.append(candid)
                                            if l[2] != 0:
                                                danger = dang(i, k, 4, actual_view) - anti_dang(i, k,
                                                                                                           4,
                                                                                                           actual_view)
                                                candid = [i, k, len(path) + len(dis_of_base), 2]
                                                if candid[2] < best_score:
                                                    best_candid = candid
                                                    best_score = candid[2]
                                                    best_path = [candid[0], candid[1]]
                                                    candids.append(candid)
                            if current_recorse_type == 2:
                                if l[1] > 0 or l[2] > 0:
                                    path = graph.get_path(graph.nodes[i][k])
                                    if len(path) > 1:
                                        g = 0
                                        for an in my_ants:
                                            if an.antType == 1 and an.maghsad == [i, k] and an.id < c_i[0]:
                                                g = g + 10
                                        if l[1] != 0:
                                            d = l[1]
                                        else:
                                            d = l[2]
                                        if g <= d:

                                            if l[1] != 0:
                                                danger = dang(i, k, 4, actual_view) - anti_dang(i, k,
                                                                                                           4,
                                                                                                           actual_view)
                                                candid = [i, k, len(path) + len(dis_of_base), 1]
                                                if candid[2] < best_score:
                                                    best_candid = candid
                                                    best_score = candid[2]
                                                    best_path = [candid[0], candid[1]]
                                                    candids.append(candid)
                                            if l[2] != 0:
                                                danger = dang(i, k, 4, actual_view) - anti_dang(i, k,
                                                                                                           4,
                                                                                                           actual_view)
                                                candid = [i, k, len(path) + len(dis_of_base), 2]
                                                if candid[2] < best_score:
                                                    best_candid = candid
                                                    best_score = candid[2]
                                                    best_path = [candid[0], candid[1]]
                                                    candids.append(candid)
                if best_path is None:
                    g_c= None
                else:
                    g_c=best_path
                if (g_c is not None):
                    path = graph.get_path(graph.nodes[g_c[0]][g_c[1]])
                    if len(path) > 0:
                        if len(path) == 1:
                            cc = path[0]
                        else:
                            cc = path[1]
                    if len(my_ants) > 0:
                        for a in my_ants:
                            if a.id == c_i[0]:
                                a.maghsad = [g_c[0], g_c[1]]
                                a.strategy = 2
                    maghsad_stra.append([g_c[0], g_c[1]])
                    stra.append(2)
                    self.direction = dirr(Width, Height, self.game.ant.currentX, self.game.ant.currentY, cc[0], cc[1]).value
                    p = 1
            if p==0 :
                best_distance = 1000
                best_cell = None
                if dang(me.loc_x, me.loc_y, self.game.attackDistance, actual_view) - anti_dang(me.loc_x, me.loc_y, 1,
                                                                                              actual_view) > 0:
                    if len(my_ants) > 0:
                        for an in my_ants:
                            if an.antType == 0 and distance(self.game.mapWidth, self.game.mapHeight, me.loc_x, me.loc_y,
                                                            an.loc_x, an.loc_y) > 3:
                                path = graph.get_path(graph.nodes[an.loc_x][an.loc_y])
                                if len(path) > 0 and len(path) < best_distance:
                                    best_distance = len(path)
                                    best_cell = [an.loc_x, an.loc_y]
                    if best_cell is not None:
                        g_c =best_cell
                    else:
                        base_cell = [self.game.baseX, self.game.baseY]
                        g_c =best_cell
                else:
                    g_c= None
                if (g_c is not None):
                    path = graph.get_path(graph.nodes[g_c[0]][g_c[1]])
                    if len(path) > 0:
                        if len(path) == 1:
                            cc = path[0]
                        else:
                            cc = path[1]
                    if len(my_ants) > 0:
                        for a in my_ants:
                            if a.id == c_i[0]:
                                a.maghsad = [g_c[0], g_c[1]]
                                a.strategy = 3
                    maghsad_stra.append([g_c[0], g_c[1]])
                    stra.append(3)
                    self.direction = dirr(Width, Height, self.game.ant.currentX, self.game.ant.currentY, cc[0], cc[1]).value
                    p = 1
            if p==0:
                r_fog = 20
                ex_c = None
                r_turn_bala = 10
                r_turn_mean = 7
                r_turn_min1 = 3
                r_turn_min2 = 1
                area_s = areas(self.game.mapHeight, self.game.mapWidth, 5, 5)
                loc_ant = loc_ants(my_ants, 5, self.game.mapHeight, self.game.mapWidth, self.game.ant.currentX,
                                   self.game.ant.currentY, c_i[0])
                best_r_area = 0
                best_cel = []
                best_area = []
                best_dis = 1000
                if len(self.game.chatBox.allChats) != 0:
                    turn = self.game.chatBox.allChats[len(self.game.chatBox.allChats) - 1].turn + 1
                else:
                    turn = 1
                for area in list(area_s):
                    r_area = 0
                    for cell in list(area):
                        r_cell = 0
                        p = 0
                        if cell in loc_ant:
                            area.remove(cell)
                            p = 1
                        if actual_view[cell[0]][cell[1]][0] == 2 and p == 0:
                            area.remove(cell)
                            p = 1
                        elif p == 0:
                            if actual_view[cell[0]][cell[1]][0] == -1:
                                r_cell = r_cell + r_fog
                            if abs(actual_view[cell[0]][cell[1]][7] - turn) > 10:
                                r_cell = r_cell + r_turn_bala
                            if abs(actual_view[cell[0]][cell[1]][7] - turn) < 10 and abs(
                                    actual_view[cell[0]][cell[1]][7] - turn) >= 7:
                                r_cell = r_cell + r_turn_mean
                            if abs(actual_view[cell[0]][cell[1]][7] - turn) < 7 and abs(
                                    actual_view[cell[0]][cell[1]][7] - turn) >= 4:
                                r_cell = r_cell + r_turn_min1
                            if abs(actual_view[cell[0]][cell[1]][7] - turn) < 4 and abs(
                                    actual_view[cell[0]][cell[1]][7] - turn) >= 3:
                                r_cell = r_cell + r_turn_min2
                            if abs(actual_view[cell[0]][cell[1]][7] - turn) < 3:
                                r_cell = 0.1
                            cell.append(r_cell)

                    if len(area) != 0:
                        for cell in area:
                            eeeee = 0
                            r_area = r_area + cell[2]

                        if best_r_area < r_area:
                            best_r_area = r_area
                            best_area = area
                        else:
                            area_s.remove(area)
                if len(best_area) == 0:
                    ex_c= None
                else:
                    for cell in best_area:

                        dis = distance(self.game.mapWidth, self.game.mapHeight, self.game.ant.currentX,
                                       self.game.ant.currentY, cell[0], cell[1])

                        if dis < best_dis:
                            best_dis = dis
                            best_cel = cell
                    c = [best_cel[0], best_cel[1]]
                    ex_c= c

                if ex_c is not None:
                    path = graph.get_path(graph.nodes[ex_c[0]][ex_c[1]])
                    if len(path) > 1:
                        cc = path[1]
                        if len(my_ants) > 0:
                            for a in my_ants:
                                if a.id == c_i[0]:
                                    a.maghsad = [ex_c[0],ex_c[1]]
                                    a.strategy = 1
                        maghsad_stra.append([ex_c[0],ex_c[1]])
                        stra.append(1)

                        self.direction=dirr(Width,Height,self.game.ant.currentX,self.game.ant.currentY,cc[0],cc[1]).value
                        p = 1
        if self.game.ant.antType==0 and p==0:
            if len(maghar_harif)==0:
                p=0
                if p == 0:
                    ex_c=None
                    candids = []
                    cell = None
                    for i, k in enumerate(actual_view):
                        for j, g in enumerate(k):
                            candid = []
                            if g[6] > 0 and distance(self.game.mapWidth, self.game.mapHeight, self.game.baseX,
                                                     self.game.baseY, i, j) < 8:
                                dis = distance(self.game.mapWidth, self.game.mapHeight, self.game.ant.currentX,
                                               self.game.ant.currentY, i, j)
                                candid = [i, j, -1 * dis]
                                candids.append(candid)
                    best_score = -10000
                    x = 0
                    y = 0
                    if len(candids) == 0:
                        ex_c= None
                    for i in candids:
                        if i[2] > best_score:
                            best_score = i[2]
                            cell = [i[0], i[1]]
                    ex_c= cell
                    if ex_c is not None:
                        path = graph.get_path(graph.nodes[ex_c[0]][ex_c[1]])
                        if len(path) == 1:
                            cc = path[0]
                        else:
                            cc = path[1]
                        if len(my_ants) > 0:
                            for a in my_ants:
                                if a.id == c_i[0]:
                                    a.maghsad = [ex_c[0], ex_c[1]]
                                    a.strategy = 5
                        maghsad_stra.append([ex_c[0], ex_c[1]])
                        stra.append(5)
                        self.direction = dirr(Width, Height, self.game.ant.currentX, self.game.ant.currentY, cc[0], cc[1]).value
                        p = 1
                kh = dang(self.game.ant.currentX, self.game.ant.currentY, self.game.attackDistance, actual_view)
                if len(paygah_man) > 0:
                    if actual_view[paygah_man[0][0]][paygah_man[0][1]][10] == 0:
                        paygah_man.remove(paygah_man[0])
                if len(paygah_man) == 0:
                    if kh - actual_view[self.game.ant.currentX][self.game.ant.currentY][5] > 0:
                        path = graph.get_path(graph.nodes[self.game.baseX][self.game.baseY])
                        if 3 + kh < len(path):
                            paygah = path[3 + kh]
                            if actual_view[paygah[0]][paygah[1]][10] < kh:
                                actual_view[paygah[0]][paygah[1]][10] = kh
                                paygah_man.append(paygah)
                        elif kh < len(path):
                            paygah = path[kh]
                            if actual_view[paygah[0]][paygah[1]][10] < kh:
                                actual_view[paygah[0]][paygah[1]][10] = kh
                                paygah_man.append(paygah)
                        elif 4 < len(path):
                            paygah = path[4]
                            if actual_view[paygah[0]][paygah[1]][10] < kh:
                                actual_view[paygah[0]][paygah[1]][10] = kh
                                paygah_man.append(paygah)
                        elif 3 < len(path):
                            paygah = path[3]
                            if actual_view[paygah[0]][paygah[1]][10] < kh:
                                actual_view[paygah[0]][paygah[1]][10] = kh
                                paygah_man.append(paygah)
                        elif 2 < len(path):
                            paygah = path[2]
                            if actual_view[paygah[0]][paygah[1]][10] < kh:
                                actual_view[paygah[0]][paygah[1]][10] = kh
                                paygah_man.append(paygah)
                        elif 1 < len(path):
                            paygah = path[1]
                            if actual_view[paygah[0]][paygah[1]][10] < kh:
                                actual_view[paygah[0]][paygah[1]][10] = kh
                                paygah_man.append(paygah)
                if p == 0:
                    cell=None
                    candids = []
                    for i, k in enumerate(actual_view):
                        for j, g in enumerate(k):
                            candid = []
                            if g[10] > 0:
                                path = graph.get_path(graph.nodes[i][j])
                                candid = [i, j, len(path)]
                                candids.append(candid)
                    best_score = 10000
                    x = 0
                    y = 0
                    if len(candids) > 0:
                        for i in candids:
                            if i[2] < best_score:
                                best_score = i[2]
                                cell = [i[0], i[1]]

                    if cell is not None:
                        path = graph.get_path(graph.nodes[cell[0]][cell[1]])
                        if len(path) > 0:
                            if len(path) == 1:
                                cc = path[0]
                            else:
                                cc = path[1]
                        if len(my_ants) > 0:
                            for a in my_ants:
                                if a.id == c_i[0]:
                                    a.maghsad = [cell[0], cell[1]]
                                    a.strategy = 6
                        maghsad_stra.append([cell[0], cell[1]])
                        stra.append(6)
                        self.direction = dirr(Width,Height, self.game.ant.currentX, self.game.ant.currentY, cc[0], cc[1]).value
                        p = 1
                if p==0 and len(ist) == 0:
                    if [self.game.ant.currentX, self.game.ant.currentY] in istgah:
                        ist.append(1)
                    else:
                        path_1 = 1000
                        path = []
                        gg=0
                        for c in istgah:
                            path_2 = graph.get_path(graph.nodes[c[0]][c[1]])
                            if actual_view[c[0]][c[1]][5] < 2 and p == 0 and len(path_2) < path_1:
                                path_1 = len(path_2)
                                path = path_2
                                gg=c
                        if len(path) != 0:
                            if len(path) == 1:
                                cc = path[0]
                            else:
                                cc = path[1]
                            if len(my_ants) > 0:
                                for a in my_ants:
                                    if a.id == c_i[0]:
                                        a.maghsad = [gg[0], gg[1]]
                                        a.strategy = 4
                            maghsad_stra.append([gg[0], gg[1]])
                            stra.append(4)
                            self.direction = dirr(Width, Height, self.game.ant.currentX, self.game.ant.currentY, cc[0],
                                                   cc[1]).value
                            p = 1
                if len(ist) > 0 and len(ist_2) == 0:
                    if actual_view[self.game.ant.currentX][self.game.ant.currentY][5] > 1 and p == 0:
                        ist_2.append(1)
                if p == 0 and len(ist_2) > 0:
                    ex_c=None
                    candids = []
                    cell = None
                    for i, k in enumerate(actual_view):
                        for j, g in enumerate(k):
                            candid = []
                            if dang(i, j, self.game.attackDistance, actual_view) > 0 and g[0] != 2:
                                candid.append(i)
                                candid.append(j)

                                candid.append(len(graph.get_path(graph.nodes[i][j])))
                                candids.append(candid)
                    if len(candids) > 0:
                        max_value = 1000
                        value = 0
                        for c in candids:
                            value = c[2]
                            if value < max_value:
                                max_value = value
                                cell = [c[0], c[1]]
                        ex_c= cell
                    if ex_c is not None:
                        path = graph.get_path(graph.nodes[ex_c[0]][ex_c[1]])
                        if len(path) == 1:
                            cc = path[0]
                        else:
                            cc = path[1]
                        if len(my_ants) > 0:
                            for a in my_ants:
                                if a.id == c_i[0]:
                                    a.maghsad = [ex_c[0], ex_c[1]]
                                    a.strategy =7
                        maghsad_stra.append([ex_c[0], ex_c[1]])
                        stra.append(7)
                        self.direction = dirr(Width, Height, self.game.ant.currentX, self.game.ant.currentY, cc[0], cc[1]).value
                        p = 1
                if p == 0 and len(ist_2) > 0:
                    r_fog = 20
                    ex_c = None
                    r_turn_bala = 10
                    r_turn_mean = 7
                    r_turn_min1 = 3
                    r_turn_min2 = 1
                    area_s = areas(self.game.mapHeight, self.game.mapWidth, 5, 5)
                    loc_ant =[]
                    best_r_area = 0
                    best_cel = []
                    best_area = []
                    best_dis = 1000
                    if len(self.game.chatBox.allChats) != 0:
                        turn = self.game.chatBox.allChats[len(self.game.chatBox.allChats) - 1].turn + 1
                    else:
                        turn = 1
                    for area in list(area_s):
                        r_area = 0
                        for cell in list(area):
                            r_cell = 0
                            p = 0
                            if actual_view[cell[0]][cell[1]][0] == 2 and p == 0:
                                area.remove(cell)
                                p = 1
                            elif p == 0:
                                if actual_view[cell[0]][cell[1]][0] == -1:
                                    r_cell = r_cell + r_fog
                                if abs(actual_view[cell[0]][cell[1]][7] - turn) > 10:
                                    r_cell = r_cell + r_turn_bala
                                if abs(actual_view[cell[0]][cell[1]][7] - turn) < 10 and abs(
                                        actual_view[cell[0]][cell[1]][7] - turn) >= 7:
                                    r_cell = r_cell + r_turn_mean
                                if abs(actual_view[cell[0]][cell[1]][7] - turn) < 7 and abs(
                                        actual_view[cell[0]][cell[1]][7] - turn) >= 4:
                                    r_cell = r_cell + r_turn_min1
                                if abs(actual_view[cell[0]][cell[1]][7] - turn) < 4 and abs(
                                        actual_view[cell[0]][cell[1]][7] - turn) >= 3:
                                    r_cell = r_cell + r_turn_min2
                                if abs(actual_view[cell[0]][cell[1]][7] - turn) < 3:
                                    r_cell = 0.1
                                cell.append(r_cell)

                        if len(area) != 0:
                            for cell in area:
                                eeeee = 0
                                r_area = r_area + cell[2]

                            if best_r_area < r_area:
                                best_r_area = r_area
                                best_area = area
                            else:
                                area_s.remove(area)
                    if len(best_area) == 0:
                        ex_c = None
                    else:
                        for cell in best_area:

                            dis = distance(self.game.mapWidth, self.game.mapHeight, self.game.ant.currentX,
                                           self.game.ant.currentY, cell[0], cell[1])

                            if dis < best_dis:
                                best_dis = dis
                                best_cel = cell
                        c = [best_cel[0], best_cel[1]]
                        ex_c = c
                    if ex_c is not None:
                        path = graph.get_path(graph.nodes[ex_c[0]][ex_c[1]])
                        if len(path) >1:

                            cc = path[1]
                            if len(my_ants) > 0:
                                for a in my_ants:
                                    if a.id == c_i[0]:
                                        a.maghsad = [ex_c[0], ex_c[1]]
                                        a.strategy = 1
                            maghsad_stra.append([ex_c[0], ex_c[1]])
                            stra.append(1)
                            self.direction = dirr(Width, Height, self.game.ant.currentX, self.game.ant.currentY, cc[0], cc[1]).value
                            p = 1
            if len(maghar_harif)>0:
                p=0
                if p == 0 and distance(w,h,self.game.ant.currentX,self.game.ant.currentY,maghar_harif[0][0],maghar_harif[0][1])>7:
                    if p==0:
                        ex_c = None
                        candids = []
                        cell = None
                        for i, k in enumerate(actual_view):
                            for j, g in enumerate(k):
                                candid = []
                                if g[6] > 0 and distance(self.game.mapWidth, self.game.mapHeight, self.game.baseX,
                                                         self.game.baseY, i, j) < 8:
                                    dis = distance(self.game.mapWidth, self.game.mapHeight, self.game.ant.currentX,
                                                   self.game.ant.currentY, i, j)
                                    candid = [i, j, -1 * dis]
                                    candids.append(candid)
                        best_score = -10000
                        x = 0
                        y = 0
                        if len(candids) == 0:
                            ex_c = None
                        for i in candids:
                            if i[2] > best_score:
                                best_score = i[2]
                                cell = [i[0], i[1]]
                        ex_c = cell
                        if ex_c is not None:
                            path = graph.get_path(graph.nodes[ex_c[0]][ex_c[1]])
                            if len(path) == 1:
                                cc = path[0]
                            else:
                                cc = path[1]
                            if len(my_ants) > 0:
                                for a in my_ants:
                                    if a.id == c_i[0]:
                                        a.maghsad = [ex_c[0], ex_c[1]]
                                        a.strategy = 5
                            maghsad_stra.append([ex_c[0], ex_c[1]])
                            stra.append(5)
                            self.direction = dirr(Width, Height, self.game.ant.currentX, self.game.ant.currentY, cc[0], cc[1]).value
                            p = 1
                    kh = dang(self.game.ant.currentX, self.game.ant.currentY, self.game.attackDistance, actual_view)
                    if len(paygah_man) > 0:
                        if actual_view[paygah_man[0][0]][paygah_man[0][1]][10] == 0:
                            paygah_man.remove(paygah_man[0])
                    if len(paygah_man) == 0:
                        if kh - actual_view[self.game.ant.currentX][self.game.ant.currentY][5] > 0:
                            path = graph.get_path(graph.nodes[self.game.baseX][self.game.baseY])
                            if 3 + kh < len(path):
                                paygah = path[3 + kh]
                                if actual_view[paygah[0]][paygah[1]][10] < kh:
                                    actual_view[paygah[0]][paygah[1]][10] = kh
                                    paygah_man.append(paygah)
                            elif kh < len(path):
                                paygah = path[kh]
                                if actual_view[paygah[0]][paygah[1]][10] < kh:
                                    actual_view[paygah[0]][paygah[1]][10] = kh
                                    paygah_man.append(paygah)
                            elif 4 < len(path):
                                paygah = path[4]
                                if actual_view[paygah[0]][paygah[1]][10] < kh:
                                    actual_view[paygah[0]][paygah[1]][10] = kh
                                    paygah_man.append(paygah)
                            elif 3 < len(path):
                                paygah = path[3]
                                if actual_view[paygah[0]][paygah[1]][10] < kh:
                                    actual_view[paygah[0]][paygah[1]][10] = kh
                                    paygah_man.append(paygah)
                            elif 2 < len(path):
                                paygah = path[2]
                                if actual_view[paygah[0]][paygah[1]][10] < kh:
                                    actual_view[paygah[0]][paygah[1]][10] = kh
                                    paygah_man.append(paygah)
                            elif 1 < len(path):
                                paygah = path[1]
                                if actual_view[paygah[0]][paygah[1]][10] < kh:
                                    actual_view[paygah[0]][paygah[1]][10] = kh
                                    paygah_man.append(paygah)
                    if p == 0:
                        cell = None
                        candids = []
                        for i, k in enumerate(actual_view):
                            for j, g in enumerate(k):
                                candid = []
                                if g[10] > 0:
                                    path = graph.get_path(graph.nodes[i][j])
                                    candid = [i, j, len(path)]
                                    candids.append(candid)
                        best_score = 10000
                        x = 0
                        y = 0
                        if len(candids) > 0:
                            for i in candids:
                                if i[2] < best_score:
                                    best_score = i[2]
                                    cell = [i[0], i[1]]

                        if cell is not None:
                            path = graph.get_path(graph.nodes[cell[0]][cell[1]])
                            if len(path) > 0:
                                if len(path) == 1:
                                    cc = path[0]
                                else:
                                    cc = path[1]
                            if len(my_ants) > 0:
                                for a in my_ants:
                                    if a.id == c_i[0]:
                                        a.maghsad = [cell[0], cell[1]]
                                        a.strategy = 6
                            maghsad_stra.append([cell[0], cell[1]])
                            stra.append(6)
                            self.direction = dirr(Width,Height, self.game.ant.currentX, self.game.ant.currentY, cc[0],
                                                  cc[1]).value
                            p = 1
                    if p==0 and len(ist) == 0:
                        if [self.game.ant.currentX, self.game.ant.currentY] in istgah:
                            ist.append(1)
                        else:
                            path_1 = 1000
                            path = []
                            gg=0
                            for c in istgah:
                                path_2 = graph.get_path(graph.nodes[c[0]][c[1]])
                                if actual_view[c[0]][c[1]][5] < 2 and p == 0 and len(path_2) < path_1:
                                    path_1 = len(path_2)
                                    path = path_2
                                    gg=c
                            if len(path) != 0:
                                if len(path) == 1:
                                    cc = path[0]
                                else:
                                    cc = path[1]
                                if len(my_ants) > 0:
                                    for a in my_ants:
                                        if a.id == c_i[0]:
                                            a.maghsad = [gg[0], gg[1]]
                                            a.strategy = 4
                                maghsad_stra.append([gg[0], gg[1]])
                                stra.append(4)
                                self.direction = dirr(Width,Height, self.game.ant.currentX, self.game.ant.currentY, cc[0],
                                                       cc[1]).value
                                p = 1
                    if len(ist) > 0 and len(ist_2) == 0:
                        if actual_view[self.game.ant.currentX][self.game.ant.currentY][5] > 1 and p == 0:
                            ist_2.append(1)
                    if p == 0 and len(ist_2) > 0:
                        ex_c = None
                        candids = []
                        cell = None
                        for i, k in enumerate(actual_view):
                            for j, g in enumerate(k):
                                candid = []
                                if dang(i, j, self.game.attackDistance, actual_view) > 0 and g[0] != 2:
                                    candid.append(i)
                                    candid.append(j)

                                    candid.append(len(graph.get_path(graph.nodes[i][j])))
                                    candids.append(candid)
                        if len(candids) > 0:
                            max_value = 1000
                            value = 0
                            for c in candids:
                                value = c[2]
                                if value < max_value:
                                    max_value = value
                                    cell = [c[0], c[1]]
                            ex_c = cell
                        if ex_c is not None:
                            path = graph.get_path(graph.nodes[ex_c[0]][ex_c[1]])
                            if len(path) == 1:
                                cc = path[0]
                            else:
                                cc = path[1]
                            if len(my_ants) > 0:
                                for a in my_ants:
                                    if a.id == c_i[0]:
                                        a.maghsad = [ex_c[0], ex_c[1]]
                                        a.strategy = 7
                            maghsad_stra.append([ex_c[0], ex_c[1]])
                            stra.append(7)
                            self.direction = dirr(Width, Height, self.game.ant.currentX, self.game.ant.currentY, cc[0],
                                                  cc[1]).value
                            p = 1
                    if p == 0 and len(ist_2) > 0:
                        path = graph.get_path(graph.nodes[maghar_harif[0][0]][maghar_harif[0][1]])
                        if len(path) == 1:
                            cc = path[0]
                        else:
                            cc = path[1]
                        if len(my_ants) > 0:
                            for a in my_ants:
                                if a.id == c_i[0]:
                                    a.maghsad = [maghar_harif[0][0], maghar_harif[0][1]]
                                    a.strategy = 8
                        maghsad_stra.append([maghar_harif[0][0], maghar_harif[0][1]])
                        stra.append(8)
                        self.direction = dirr(Width, Height, self.game.ant.currentX, self.game.ant.currentY, cc[0],
                                               cc[1]).value
                        p = 1
                if p == 0 and distance(w, h, self.game.ant.currentX, self.game.ant.currentY, maghar_harif[0][0],maghar_harif[0][1]) <8:
                    path = graph.get_path(graph.nodes[maghar_harif[0][0]][maghar_harif[0][1]])
                    if len(path) == 1:
                        cc = path[0]
                    else:
                        cc = path[1]
                    if len(my_ants) > 0:
                        for a in my_ants:
                            if a.id == c_i[0]:
                                a.maghsad = [maghar_harif[0][0], maghar_harif[0][1]]
                                a.strategy = 8
                    maghsad_stra.append([maghar_harif[0][0], maghar_harif[0][1]])
                    stra.append(8)
                    self.direction = dirr(Width, Height, self.game.ant.currentX, self.game.ant.currentY, cc[0],
                                           cc[1]).value
                    p = 1
        candids = []
        candid = []
        reward_of_candids = 0
        reward_of_candid = 0
        r_base = 1000
        r_divar = 1
        r_grass = 0.5
        r_bread = 0.5
        r_kargar_harif = 5
        r_sarbaz_harif = 20
        meghyas = r_divar + (r_grass * 20) + (r_sarbaz_harif * 4) + (r_kargar_harif * 3)  # 106
        r_turn_update = 0.05
        r_dang = 1
        reward_of_strategy = 3
        dangg = actual_view[me.loc_x][me.loc_y][8]
        flag1 = False
        flag2 = False
        x = 0
        y = 0
        r_ist = 10
        for i in actual_view:
            y = 0
            for j in i:
                flag1 = False
                reward_of_candid = 0

                if base_view[x][y][10] > actual_view[x][y][10]:
                    reward_of_candid = r_ist + 10
                if actual_view[x][y][0] == 3 and base_view[x][y][0] != 3:
                    reward_of_candid = r_base
                    flag1 = True
                    flag2 = True
                if actual_view[x][y][0] == 2 and base_view[x][y][0] != 2:
                    reward_of_candid = reward_of_candid + r_divar
                    flag1 = True
                if actual_view[x][y][1] != base_view[x][y][1]:
                    reward_of_candid = reward_of_candid + r_grass * (abs(actual_view[x][y][1] - base_view[x][y][1]))
                    flag1 = True
                if actual_view[x][y][2] != base_view[x][y][2]:
                    reward_of_candid = reward_of_candid + r_bread * (abs(actual_view[x][y][2] - base_view[x][y][2]))
                    flag1 = True
                if actual_view[x][y][4] != base_view[x][y][4]:
                    reward_of_candid = reward_of_candid + r_kargar_harif * (
                        abs(actual_view[x][y][4] - base_view[x][y][4]))
                    flag1 = True
                if actual_view[x][y][6] != base_view[x][y][6]:
                    reward_of_candid = reward_of_candid + r_sarbaz_harif * (
                        abs(actual_view[x][y][6] - base_view[x][y][6]))
                    flag1 = True
                if actual_view[x][y][7] - base_view[x][y][7] > 0:
                    reward_of_candid = reward_of_candid + r_turn_update * (
                        abs(actual_view[x][y][7] - base_view[x][y][7]))
                candid = []
                if flag1 == True:
                    candid.append(x)
                    candid.append(y)
                    candid.append(reward_of_candid)
                    candids.append(candid)
                y = y + 1
            x = x + 1
        if len(paygah_man) > 0:
            if actual_view[paygah_man[0][0]][paygah_man[0][1]][10] > base_view[paygah_man[0][0]][paygah_man[0][1]][10]:
                reward_of_candids = reward_of_candids + 10
        if len(candids) != 0:
            candids = sorted(candids, key=itemgetter(2), reverse=True)
            if flag2 == True:
                reward_of_candids = 10
            else:
                for i in candids:
                    reward_of_candids = reward_of_candids + i[2]
                reward_of_candids = ((reward_of_candids / len(candids)) / meghyas) * 10  # reward kol bein 0,4.2
        if me.antType == 1:
            if len(catm) > 0 and len(maghsad_stra) > 0:
                if maghsad_stra[len(maghsad_stra) - 1] != catm[len(catm) - 1]:  # hamle be base
                    reward_of_candids = reward_of_candids + reward_of_strategy + (128 - me.id) / 128
            else:
                reward_of_candids = reward_of_candids + reward_of_strategy + (128 - me.id) / 128
        if dangg > 0:
            reward_of_candids = reward_of_candids + r_dang
        reward_of_candids = reward_of_candids
        list_cell= candids
        b=reward_of_candids
        if len(maghsad_stra) > 0 and len(stra) > 0:
            me = A_I(self.game.ant.currentX, self.game.ant.currentY, c_i[0],
                         self.game.ant.currentResource.value, self.game.ant.currentResource.type, self.game.ant.antType,
                         self.game.ant.health)
            me.maghsad = maghsad_stra[len(maghsad_stra) - 1]
            me.strategy = stra[len(stra) - 1]
        else:
            me = A_I(self.game.ant.currentX, self.game.ant.currentY, c_i[0],
                         self.game.ant.currentResource.value, self.game.ant.currentResource.type, self.game.ant.antType,
                         self.game.ant.health)
        r=0
        if me.Resource_value>0:
            r=1
        if me.antType==0:
             h=int((me.health/self.game.healthSarbaaz)*3)
        if me.antType==1:
             h=int((me.health/self.game.healthKargar)*3)
        if len(maghsad_stra) > 0:
            magh_x=maghsad_stra[len(maghsad_stra)-1][0]
            magh_y=maghsad_stra[len(maghsad_stra)-1][1]
        else:
            magh_x = me.loc_x
            magh_y = me.loc_y
        if len(paygah_man)>0:
            if base_view[paygah_man[0][0]][paygah_man[0][1]][10] !=actual_view[paygah_man[0][0]][paygah_man[0][1]][10]:
                cc=actual_view[paygah_man[0][0]][paygah_man[0][1]][10]
                if cc>7:
                    cc=7
                c=paygah_man[0]
            else:
                cc = 0
                c = [self.game.baseX, self.game.baseY]

        else:
            cc=0
            c=[self.game.ant.currentX,self.game.ant.currentY]

        p=int(bin(me.loc_x)[2:])+int(bin(me.loc_y*pow(2,6))[2:])+int(bin(me.strategy*pow(2,12))[2:])+int(bin(me.antType*pow(2,16))[2:])+int(bin(r*pow(2,17))[2:])+int(bin(h*pow(2,18))[2:])+int(bin(me.id*pow(2,20))[2:])+int(bin(magh_x*pow(2,27))[2:])+int(bin(magh_y*pow(2,33))[2:])+int(bin(c[0]*pow(2,39))[2:])+int(bin(c[1]*pow(2,45))[2:])+int(bin(cc*pow(2,51))[2:])
        j=0
        type_res=0
        val_res = 0
        for l in list_cell:
            if actual_view[l[0]][l[1]][10]>7:
                ccc=7
            else:
                ccc = actual_view[l[0]][l[1]][10]
            if actual_view[l[0]][l[1]][4]>0:
                k=1
            else:
                 k=0
            if actual_view[l[0]][l[1]][6]>7:
                s=7
            else:
                s=actual_view[l[0]][l[1]][6]
            if actual_view[l[0]][l[1]][0]==-1:
                type_cell=1
            else:
                type_cell=actual_view[l[0]][l[1]][0]
            if actual_view[l[0]][l[1]][1]>0:
                type_res=1
                if  actual_view[l[0]][l[1]][1] <3:
                    val_res=0
                elif 2<actual_view[l[0]][l[1]][1] <11:
                    val_res=1
                elif 10<actual_view[l[0]][l[1]][1] <21:
                    val_res=2
                elif 20 < actual_view[l[0]][l[1]][1] <31:
                    val_res = 3
                elif  30<actual_view[l[0]][l[1]][1] <41:
                    val_res=4
                elif 40<actual_view[l[0]][l[1]][1] <51:
                    val_res=5
                elif 50<actual_view[l[0]][l[1]][1] <61:
                    val_res=6
                elif 60 < actual_view[l[0]][l[1]][1] <71:
                    val_res = 7
                elif  70<actual_view[l[0]][l[1]][1] <81:
                    val_res=8
                elif 80<actual_view[l[0]][l[1]][1] <91:
                    val_res=9
                elif 90<actual_view[l[0]][l[1]][1] <101:
                    val_res=10
                elif 100 < actual_view[l[0]][l[1]][1] :
                    val_res = 11
            if actual_view[l[0]][l[1]][2]>0:
                type_res=0
                if actual_view[l[0]][l[1]][2] < 3:
                    val_res = 0
                elif 2 < actual_view[l[0]][l[1]][2] < 11:
                    val_res = 1
                elif 10 < actual_view[l[0]][l[1]][2] < 21:
                    val_res = 2
                elif 20 < actual_view[l[0]][l[1]][2] < 31:
                    val_res = 3
                elif 30 < actual_view[l[0]][l[1]][2] < 41:
                    val_res = 4
                elif 40 < actual_view[l[0]][l[1]][2] < 51:
                    val_res = 5
                elif 50 < actual_view[l[0]][l[1]][2] < 61:
                    val_res = 6
                elif 60 < actual_view[l[0]][l[1]][2] < 71:
                    val_res = 7
                elif 70 < actual_view[l[0]][l[1]][2] < 81:
                    val_res = 8
                elif 80 < actual_view[l[0]][l[1]][2] < 91:
                    val_res = 9
                elif 90 < actual_view[l[0]][l[1]][2] < 101:
                    val_res = 10
                elif 100 < actual_view[l[0]][l[1]][2]:
                    val_res = 11
            t=int(bin(l[0])[2:])+int(bin(l[1]*pow(2,6))[2:])+int(bin(k*pow(2,12))[2:])+int(bin(s*pow(2,13))[2:])+int(bin(type_cell*pow(2,16))[2:])+int(bin(type_res*pow(2,18))[2:])+int(bin(val_res*pow(2,19))[2:])+int(bin(actual_view[l[0]][l[1]][8]*pow(2,23))[2:])+int(bin(ccc*pow(2,24))[2:])
            if j<15:
                p=p+t*pow(10,(54+(j*27)))
            j=j+1
            if j>14:
                break
        string=str(p)
        string=string[::-1]
        i=0
        payam=''
        r=0
        for ii in range(len(string)):
            if (ii %14)==0:
                i=0
                r=0
            r=r+pow(2,i)*int(string[ii])
            if ii == 13:
                payam=chr(r)
            elif (ii %14)==13 or ii == (len(string)-1) :
                payam=payam+chr(r)
            i=i+1
        if len(payam)==0:
            self.message = 'd'
        else:
            self.message = payam
        self.value = int(b)
        return (self.message, self.value, self.direction)
def reverse(lst):
    return [ele for ele in reversed(lst)]
def distance(width, height, x_mabda, y_mabda, x_maghsad, y_maghsad):
    x1 = abs(x_mabda - x_maghsad)
    y1 = abs(y_mabda - y_maghsad)
    num_x = 0
    num_y = 0
    y2=0
    x2=0
    if abs((width - 1) - x_mabda) < x_mabda:
        x2 = abs(width - 1 - x_mabda) + x_maghsad
    elif abs((width - 1) - x_mabda) > x_mabda:
        x2 = x_mabda + x_maghsad
    elif abs((width - 1) - x_mabda) == x_mabda:
        num_x = 1
        x2 = x_mabda
    if abs((height - 1) - y_mabda) < y_mabda:
        y2 = abs(height - 1 - y_mabda) + y_maghsad
    elif abs((height - 1) - y_mabda) > y_mabda:
        y2 = y_mabda + y_maghsad
    elif abs((height - 1) - y_mabda) == y_mabda:
        num_y = 1
        y2 = y_mabda
    if num_x == 0 and x2 > x1:
        num_x = x1
    else:
        num_x = x2
    if num_y == 0 and y2 > y1:
        num_y = y1
    else:
        num_y = y2
    return num_x + num_y
def dang(loc_x, loc_y, c, matrix):  # تابع خطر باید تعریف
    r = 0
    x = 0
    while x < c + 1:
        y = 0
        while y < c + 1:
            if x + y < c + 1:
                xx = loc_x + x
                if xx > len(matrix) - 1:
                    xx = loc_x + x - len(matrix)
                yy = loc_y + y
                if yy > len(matrix[0]) - 1:
                    yy = loc_y + y - len(matrix[0])
                r = r + matrix[xx][yy][6]
            y = y + 1
        x = x + 1
    x = -1
    while -x < c + 1:
        y = 0
        while y < c + 1:
            if y - x < c + 1:
                xx = loc_x + x
                if xx < 0:
                    xx = loc_x + x + len(matrix)
                yy = loc_y + y
                if yy > len(matrix[0]) - 1:
                    yy = loc_y + y - len(matrix[0])
                r = r + matrix[xx][yy][6]
            y = y + 1
        x = x - 1
    x = -1
    while -x < c + 1:
        y = -1
        while -y < c + 1:
            if -(x + y) < c + 1:
                xx = loc_x + x
                if xx < 0:
                    xx = loc_x + x + len(matrix)
                yy = loc_y + y
                if yy < 0:
                    yy = loc_y + y + len(matrix[0])
                r = r + matrix[xx][yy][6]
            y = y - 1
        x = x - 1
    x = 0
    while x < c + 1:
        y = -1
        while -y < c + 1:
            if x - y < c + 1:
                yy = loc_y + y
                if yy < 0:
                    yy = loc_y + y + len(matrix[0])
                xx = loc_x + x
                if xx > len(matrix) - 1:
                    xx = loc_x + x - len(matrix)
                r = r + matrix[xx][yy][6]
            y = y - 1
        x = x + 1
    return r
def anti_dang(loc_x, loc_y, c, matrix):  # تابع خطر باید تعریف
    r = 0
    x = 0
    while x < c + 1:
        y = 0
        while y < c + 1:
            if x + y < c + 1:
                xx = loc_x + x
                if xx > len(matrix) - 1:
                    xx = loc_x + x - len(matrix)
                yy = loc_y + y
                if yy > len(matrix[0]) - 1:
                    yy = loc_y + y - len(matrix[0])
                if len( matrix[xx][yy][9])>0:
                    for an in matrix[xx][yy][9]:
                        if an.antType==0:
                            r = r + 1
            y = y + 1
        x = x + 1
    x = -1
    while -x < c + 1:
        y = 0
        while y < c + 1:
            if y - x < c + 1:
                xx = loc_x + x
                if xx < 0:
                    xx = loc_x + x + len(matrix)
                yy = loc_y + y
                if yy > len(matrix[0]) - 1:
                    yy = loc_y + y - len(matrix[0])
                if len(matrix[xx][yy][9]) > 0:
                    for an in matrix[xx][yy][9]:
                        if an.antType == 0:
                            r = r + 1
            y = y + 1
        x = x - 1
    x = -1
    while -x < c + 1:
        y = -1
        while -y < c + 1:
            if -(x + y) < c + 1:
                xx = loc_x + x
                if xx < 0:
                    xx = loc_x + x + len(matrix)
                yy = loc_y + y
                if yy < 0:
                    yy = loc_y + y + len(matrix[0])
                if len(matrix[xx][yy][9]) > 0:
                    for an in matrix[xx][yy][9]:
                        if an.antType == 0:
                            r = r + 1
            y = y - 1
        x = x - 1
    x = 0
    while x < c + 1:
        y = -1
        while -y < c + 1:
            if x - y < c + 1:
                yy = loc_y + y
                if yy < 0:
                    yy = loc_y + y + len(matrix[0])
                xx = loc_x + x
                if xx > len(matrix) - 1:
                    xx = loc_x + x - len(matrix)
                if len(matrix[xx][yy][9]) > 0:
                    for an in matrix[xx][yy][9]:
                        if an.antType == 0:
                            r = r + 1
            y = y - 1
        x = x + 1
    return r
class A_I:
    id: int
    loc_x: int
    loc_y: int
    Resource_type: int
    Resource_value: int
    antType: int
    health: int
    strategy: int
    maghsad : list
    tern: int
    def __init__(self, loc_x: int, loc_y: int, id: int,Resource_type: int,Resource_value: int,antType: int,health: int):
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.id = id
        self.Resource_type=Resource_type
        self.Resource_value=Resource_value
        self.antType= antType
        self.health= health
        self.strategy= 0
        self.tern = 0
        self.maghsad= [0,0]
def areas(height, width, height_c, width_c):
    cell = []
    area = []
    areas = []
    flag_height = False
    flag_width = False
    if height % height_c != 0:
        flag_height = True
    if width % width_c != 0:
        flag_width = True

    for i in range(0, (height // height_c)):
        for j in range(0, (width // width_c)):
            area = []
            for k in range(i * height_c, ((i + 1) * height_c)):
                for l in range(j * width_c, ((j + 1) * width_c)):
                    cell = [l, k]
                    area.append(cell)
            areas.append(area)

    if flag_height == True and flag_width == False:

        for j in range(0, (width // width_c)):
            area = []
            for k in range((height // height_c) * height_c, height):
                for l in range(j * width_c, ((j + 1) * width_c)):
                    cell = [l, k]
                    area.append(cell)
            areas.append(area)

    if flag_height == False and flag_width == True:

        for i in range(0, (height // height_c)):
            area = []
            for l in range((width // width_c) * width_c, width):
                for k in range(i * height_c, ((i + 1) * height_c)):
                    cell = [l, k]
                    area.append(cell)
            areas.append(area)
    if flag_height == True and flag_width == True:
        for j in range(0, (width // width_c)):
            area = []
            for k in range((height // height_c) * height_c, height):
                for l in range(j * width_c, ((j + 1) * width_c)):
                    cell = [l, k]
                    area.append(cell)
            areas.append(area)
        for i in range(0, (height // height_c)):
            area = []
            for l in range((width // width_c) * width_c, width):
                for k in range(i * height_c, ((i + 1) * height_c)):
                    cell = [l, k]
                    area.append(cell)
            areas.append(area)
        area = []
        for k in range((height // height_c) * height_c, height):
            for l in range((width // width_c) * width_c, width):
                cell = [l, k]
                area.append(cell)
        areas.append(area)

    return areas
def loc_ants(list_of_ants, c, height, width,x,y,my_id):
    locs = []
    if len(list_of_ants) == 0:
        return locs
    for an in list_of_ants:
        if an.id<my_id :
            loc = [an.maghsad[0], an.maghsad[1]]
            locs.append(loc)
            for i in range(-(c // 2), (c // 2) + 1):
                for j in range(-(c // 2), (c // 2) + 1):
                    loc = [(an.maghsad[0] + i) % height, (an.maghsad[1] + j) % width]
                    if loc not in locs:
                        locs.append(loc)
    return locs
def dirr(width, height, x_mabda, y_mabda, x_maghsad, y_maghsad):
    curve = 0
    x1 = abs(x_mabda - x_maghsad)
    if x1 ==0:
        dirr_x = Direction.CENTER
    y1 = abs(y_mabda - y_maghsad)
    if y1 ==0:
        dirr_y = Direction.CENTER
    if x_mabda == 0 and x_maghsad == width - 1:
        dirr_x = Direction.LEFT
        dirr_y = Direction.CENTER
        curve = 1
    if x_mabda == width - 1 and x_maghsad == 0:
        dirr_x = Direction.RIGHT
        dirr_y = Direction.CENTER
        curve = 1
    if y_mabda == 0 and y_maghsad == height - 1:
        dirr_y = Direction.UP
        dirr_x = Direction.CENTER
        curve = 1
    if y_mabda == height - 1 and y_maghsad == 0:
        dirr_y = Direction.DOWN
        dirr_x = Direction.CENTER
        curve = 1
    if curve == 0:
        if x_mabda > x_maghsad:
            dirr_x = Direction.LEFT
        elif x_mabda == x_maghsad:
            dirr_x = Direction.CENTER
        elif x_maghsad > x_mabda:
            dirr_x = Direction.RIGHT
        if y_mabda > y_maghsad:
            dirr_y = Direction.UP
        elif y_mabda == y_maghsad:
            dirr_y = Direction.CENTER
        elif y_maghsad > y_mabda:
            dirr_y = Direction.DOWN
    if dirr_x == Direction.CENTER:
        if dirr_y != Direction.CENTER:
            # print(dirr_y)
            return dirr_y
    if dirr_y == Direction.CENTER:
        if dirr_x != Direction.CENTER:
            # print(dirr_x)
            return dirr_x
    if dirr_x == Direction.CENTER and  dirr_y == Direction.CENTER:
        return Direction.CENTER
class Node:
    loc_x: int
    loc_y: int
    h: int
    g: int
    neighbours: list
    danger: int

    def __init__(self, loc_x: int, loc_y: int, danger=0):
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.h = 0
        self.g = 0
        self.parent = None
        self.neighbours = []
        self.danger = 0
        self.resource = [0, 0]  # [grass =1/bread = 2,value]
class MASIR:
    nodes: list
    matrix: list

    def __init__(self, matrix):
        self.matrix = matrix
        self.nodes = []
        self.width = len(matrix)
        self.height = len(matrix[0])
        self.matrix_to_graph()

    def matrix_to_graph(self, flag=0):
        # sakht node ha
        if flag == 0:
            for x in range(0, self.width):
                self.nodes.append([])
                for y in range(0, self.height):
                    if self.matrix[x][y][0] != 2:  # divar nabashad
                        node = Node(loc_x=x, loc_y=y)  #
                        self.nodes[x].append(node)
                    else:
                        self.nodes[x].append(None)
            for x in range(0, self.width):
                for y in range(0, self.height):
                    if self.nodes[x][y] is not None:
                        if self.nodes[(x + 1) % self.width][y % self.height] is not None:
                            self.nodes[x % self.width][y % self.height].neighbours.append(
                                self.nodes[(x + 1) % self.width][y % self.height])
                        if self.nodes[(x - 1) % self.width][y % self.height] is not None:
                            self.nodes[x % self.width][y % self.height].neighbours.append(
                                self.nodes[(x - 1) % self.width][y % self.height])
                        if self.nodes[x % self.width][(y + 1) % self.height] is not None:
                            self.nodes[x % self.width][y % self.height].neighbours.append(
                                self.nodes[x % self.width][(y + 1) % self.height])
                        if self.nodes[x % self.width][(y - 1) % self.height] is not None:
                            self.nodes[x % self.width][y % self.height].neighbours.append(
                                self.nodes[x % self.width][(y - 1) % self.height])
    def run(self, start_node):

        frontier = []
        explore = []

        frontier.append(start_node)
        while len(frontier) > 0:
            min_f = 10000000
            head = None
            for node in frontier:
                if node.g < min_f:
                    min_f = node.g
                    head = node
            for child in head.neighbours:
                if child not in explore and child not in frontier:
                    child.parent = head
                    child.g = abs(1 + head.g)
                    frontier.append(child)
                else:
                    if child.g > 1 + head.g:
                        child.parent = head
                        child.g = 1 + head.g
                        if child in explore:
                            frontier.append(child)
                            explore.remove(child)
            explore.append(head)
            frontier.remove(head)

    def get_path(self, goal_node):
        path = []
        itr = goal_node
        while itr is not None:
            path.append((itr.loc_x, itr.loc_y))
            itr = itr.parent

        return reverse(path)
    def calculate_h(self, goal_node, node, flag=0):
        if flag == 1:
            c1 = 1
            c2 = -2
            h = -1
            if (node is not None) and (goal_node is not None):
                h = abs(c1 * distance(self.width, self.height, node.loc_x, node.loc_y, goal_node.loc_x,
                                      goal_node.loc_y) + c2 * node.danger)
            return h
        if flag == 0:
            if (node is not None) and (goal_node is not None):
                h = distance(self.width, self.height, node.loc_x, node.loc_y, goal_node.loc_x, goal_node.loc_y)
            return h

    def a_star(self, start_node, goal_node, flag=0, resource=0, c3=0.5):
        if flag == 0:
            frontier = []
            explore = []

            frontier.append(start_node)
            while len(frontier) > 0:
                min_f = 10000000
                head = None
                c1 = 1
                c2 = -2
                for node in frontier:
                    node.h = self.calculate_h(goal_node, node)
                    if node.h + node.g < min_f:
                        min_f = node.h + node.g
                        head = node

                #
                if head.loc_x == goal_node.loc_x and head.loc_y == goal_node.loc_y:
                    path = []
                    itr = head
                    while itr is not None:
                        path.append((itr.loc_x, itr.loc_y))
                        itr = itr.parent

                    return reverse(path)

                for child in head.neighbours:
                    if child not in explore and child not in frontier:
                        child.parent = head
                        child.g = abs(1 + head.g)
                        frontier.append(child)
                    else:
                        if child.g > 1 + head.g:
                            child.parent = head
                            child.g = 1 + head.g
                            if child in explore:
                                frontier.append(child)
                                explore.remove(child)
                explore.append(head)
                frontier.remove(head)

            return None
