#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:26:59 2020

@author: vadim
"""
from json import load

FNAME='../test.dat'

input_m=[]

min_x, min_y, max_x, max_y = 100000,100000,0,0
for pline in load(open(FNAME)):
    for stroke in pline:
        input_m.append(stroke)
        for point in stroke:
            if min_x > point[0]:    
                min_x = point[0]
            if min_y > point[1]:    
                min_y = point[1]
            if max_x < point[0]:    
                max_x = point[0]
            if max_y < point[1]:    
                max_y = point[1]
print(min_x, min_y, max_x, max_y)
real_min_x =  280
real_min_y = -155
real_max_x =  480
real_max_y =  155

dx = real_min_x - min_x
dy = real_min_y - min_y

sx = (real_max_x - real_min_x)/(max_x - min_x)
sy = (real_max_y - real_min_y)/(max_y - min_y)

s = sx if sx < sy else sy



x=0
y=0
z=0
xp=0

x_len=[]
y_len=[]
z_len=[]


# ввод через консоль
'''
print('введите координаты(x):')
x_len=input().split()
print('введите координаты (y):')
y_len=input().split()
print('введите координаты(z):')
z_len=input().split()
'''

for i in range(len(input_m)):
    x_len.append(input_m[i][0][0])
    x_len.append(input_m[i][1][0])
    
for i in range(len(input_m)):
    y_len.append(input_m[i][0][1]) 
    y_len.append(input_m[i][1][1])
    
'''
#-17.64 косание стола маркером 
#-15 поднятый маркер 
c=1
for i in range(len(x_len)):
    if(c == 1):
        z_len.append(-17.64)
    if(c == 2):
        z_len.append(-17.64)
    if(c == 3):
        z_len.append(-15)
    if(c == 4):
        z_len.append(-15)
        c=0
    c+=1
'''

print(z_len)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#dat
head_dat = '''&ACCESS RVP
&REL 5
&PARAM EDITMASK = *
&PARAM TEMPLATE = C:\KRC\Roboter\Template\\vorgabe
&PARAM DISKPATH = KRC:\R1\\user programm\demonstration
DEFDAT  test_face
;FOLD EXTERNAL DECLARATIONS;%{PE}%MKUKATPBASIS,%CEXT,%VCOMMON,%P
;FOLD BASISTECH EXT;%{PE}%MKUKATPBASIS,%CEXT,%VEXT,%P
EXT  BAS (BAS_COMMAND  :IN,REAL  :IN )
DECL INT SUCCESS
;ENDFOLD (BASISTECH EXT)
;FOLD USER EXT;%{E}%MKUKATPUSER,%CEXT,%VEXT,%P
;Make your modifications here
;ENDFOLD (USER EXT)
;ENDFOLD (EXTERNAL DECLARATIONS)
 '''

def first_point_dat(xp,x,y,z):
    
    first_point_dat = '''
    
DECL E6POS XP'''+str(xp)+'''={X '''+str(x)+''',Y '''+str(y)+''',Z '''+str(z)+''',A -180,B 0,C 180,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
DECL FDAT FP'''+str(xp)+'''={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " "}
DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 500.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 100.000,EXAX_IGN 0}
DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "Kuka.PointName=P'''+str(total_xp)+'''; Kuka.FrameData.base_no=0; Kuka.FrameData.tool_no=1; Kuka.FrameData.ipo_frame=#BASE; Kuka.isglobalpoint=False; Kuka.MoveDataName=CPDAT4; Kuka.MovementData.apo_fac=50; Kuka.MovementData.apo_dist=500; Kuka.MovementData.axis_acc=100; Kuka.MovementData.axis_vel=100; Kuka.MovementData.circ_typ=#BASE; Kuka.MovementData.jerk_fac=50; Kuka.MovementData.ori_typ=#VAR; Kuka.MovementData.vel=2; Kuka.MovementData.acc=100; Kuka.MovementData.exax_ign=0; Kuka.VelocityPath=2; Kuka.BlendingEnabled=False; Kuka.CurrentCDSetIndex=0      "}
'''
    return first_point_dat


def point_dat(xp,x,y,z):
    point_dat = '''
    
DECL E6POS XP'''+str(xp)+'''={X '''+str(x)+''',Y '''+str(y)+''',Z '''+str(z)+''',A -180,B 0,C 180,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
DECL FDAT FP'''+str(xp)+'''={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " "}
DECL LDAT LCPDAT'''+str(xp)+ '''={VEL 2.00000,ACC 100.000,APO_DIST 500.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 100.000,EXAX_IGN 0}
    '''
    return point_dat

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#src
head_src ='''&ACCESS RVP
&REL 5
&PARAM EDITMASK = *
&PARAM TEMPLATE = C:\KRC\Roboter\Template\\vorgabe
&PARAM DISKPATH = KRC:\R1\\user programm\demonstration
DEF test_face( )
;FOLD INI;%{PE}
  ;FOLD BASISTECH INI
    GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
    INTERRUPT ON 3 
    BAS (#INITMOV,0 )
  ;ENDFOLD (BASISTECH INI)
  ;FOLD USER INI
    ;Make your modifications here

  ;ENDFOLD (USER INI)
;ENDFOLD (INI)
'''


start_home_src ='''
;FOLD SPTP HOME Vel=100 % DEFAULT ;%{PE}
;FOLD Parameters ;%{h}
;Params IlfProvider=kukaroboter.basistech.inlineforms.movement.spline; Kuka.IsGlobalPoint=False; Kuka.PointName=HOME; Kuka.BlendingEnabled=False; Kuka.MoveDataPtpName=DEFAULT; Kuka.VelocityPtp=100; Kuka.VelocityFieldEnabled=True; Kuka.CurrentCDSetIndex=0; Kuka.MovementParameterFieldEnabled=True; IlfCommand=SPTP
;ENDFOLD
SPTP XHOME WITH $VEL_AXIS[1] = SVEL_JOINT(100.0), $TOOL = STOOL2(FHOME), $BASE = SBASE(FHOME.BASE_NO), $IPO_MODE = SIPO_MODE(FHOME.IPO_FRAME), $LOAD = SLOAD(FHOME.TOOL_NO), $ACC_AXIS[1] = SACC_JOINT(PDEFAULT), $APO = SAPO_PTP(PDEFAULT), $GEAR_JERK[1] = SGEAR_JERK(PDEFAULT), $COLLMON_TOL_PRO[1] = USE_CM_PRO_VALUES(0)
;ENDFOLD
'''


def point_src(xp):
    point_src = '''
    
;FOLD LIN P'''+str(xp)+''' Vel=2 m/s CPDAT'''+str(xp)+''' Tool[1]:marker Base[0] ;%{PE}
;FOLD Parameters ;%{h}
;Params IlfProvider=kukaroboter.basistech.inlineforms.movement.old; Kuka.IsGlobalPoint=False; Kuka.PointName=P'''+str(xp)+'''; Kuka.BlendingEnabled=False; Kuka.MoveDataName=CPDAT1; Kuka.VelocityPath=2; Kuka.CurrentCDSetIndex=0; Kuka.MovementParameterFieldEnabled=True; IlfCommand=LIN
;ENDFOLD
$BWDSTART = FALSE
LDAT_ACT = LCPDAT'''+str(xp)+'''
FDAT_ACT = FP'''+str(xp)+'''
BAS(#CP_PARAMS, 2.0)
SET_CD_PARAMS (0)
LIN XP'''+str(xp)+'''
;ENDFOLD
'''
    return point_src

 
finish_home_src ='''

;FOLD SPTP HOME Vel=100 % DEFAULT ;%{PE}
;FOLD Parameters ;%{h}
;Params IlfProvider=kukaroboter.basistech.inlineforms.movement.spline; Kuka.IsGlobalPoint=False; Kuka.PointName=HOME; Kuka.BlendingEnabled=False; Kuka.MoveDataPtpName=DEFAULT; Kuka.VelocityPtp=100; Kuka.VelocityFieldEnabled=True; Kuka.CurrentCDSetIndex=0; Kuka.MovementParameterFieldEnabled=True; IlfCommand=SPTP
;ENDFOLD
SPTP XHOME WITH $VEL_AXIS[1] = SVEL_JOINT(100.0), $TOOL = STOOL2(FHOME), $BASE = SBASE(FHOME.BASE_NO), $IPO_MODE = SIPO_MODE(FHOME.IPO_FRAME), $LOAD = SLOAD(FHOME.TOOL_NO), $ACC_AXIS[1] = SACC_JOINT(PDEFAULT), $APO = SAPO_PTP(PDEFAULT), $GEAR_JERK[1] = SGEAR_JERK(PDEFAULT), $COLLMON_TOL_PRO[1] = USE_CM_PRO_VALUES(0)
;ENDFOLD

END
'''
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    

xp_len=[]
total_xp=[]
for i in range(len(x_len)):
    xp_len.append(i+1)
total_xp=len(xp_len)    


print('x='+str(x_len))
print('y='+str(y_len))
print('z='+str(z_len))
print('xp='+str(xp_len))
print('total_xp='+ str(total_xp))


for i in range(total_xp-1):
    x = x_len[i] * s + dx
    y = y_len[i] * s + dy

    
    if round(x_len[i]) == round(x_len[i+1]) and round(y_len[i]) == round(y_len[i+1]) :
        z = -15
    else:
        z = -17.64
    

    xp = xp_len[i]
    if xp==1:    
        photo_dat = open('photo.dat', 'w')
        photo_dat.write("%s%s" % (head_dat,first_point_dat(xp,x,y,z)))
        photo_dat.close()
        photo_src = open('photo.src','w')
        photo_src.write("%s%s%s" % (head_src,start_home_src,point_src(xp=xp)))
        photo_src.close()
    elif xp==0:
        pass
    else:
        photo_dat = open('photo.dat', 'a')
        photo_dat.write((point_dat(xp,x,y,z)))
        photo_dat.close()
        photo_src = open('photo.src','a')
        photo_src.write((point_src(xp=xp)))
        photo_src.close()


photo_dat = open('photo.dat', 'a')
photo_dat.write('ENDDAT')
photo_dat.close()
print('DAT файл создан :)')
photo_src = open('photo.src','a')
photo_src.write((finish_home_src))
photo_src.close()
print('SRC файл создан :)')


#else:
#    print ('ERROR:количество введенных координат не совпадает')
    
    
    
