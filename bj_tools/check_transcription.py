from PIL import Image
import woo_tables as W
def cls_of(px,euro):
  if px==(255,0,0):return'H'
  if px==(255,255,0):return'S'
  if px==(0,255,0):return'P'
  if px==(0,0,255):return'D'
  if px[2]==255 and px[0]<130 and px[1]<130: return 'D' if euro else 'Ds'
  if px==(255,255,255):return'R?'
  if px[1]==255 and px[2]==255 and px[0]>150:return'P?'
  return str(px)
def code_cls(c):
  return {'Ph':'P?','Pd':'P?','Ps':'P?','Rh':'R?','Rs':'R?','Rp':'R?','Rp2':'R?'}.get(c,c)
G={
 '1S':('bj_1d_s17.png',46,25,17,[(61,'hard',[5,8,9,10,11,12,13,14,15,16,17]),(265,'soft',[13,14,15,16,17,18,19,20]),(418,'pair',[2,3,4,6,7,8,9,11])]),
 '1H':('bj_1d_h17.png',46,25,17,[(61,'hard',[5,8,9,10,11,12,13,14,15,16,17,18]),(282,'soft',[13,14,15,16,17,18,19,20]),(435,'pair',[2,3,4,6,7,8,9,11])]),
 '2S':('bj_2d_s17.png',57,25.8,18,[(85,'hard',[5,9,10,11,12,13,14,15,16,17]),(265,'soft',[13,14,15,16,17,18,19]),(391,'pair',[2,3,4,6,7,8,9,11])]),
 '2H':('bj_2d_h17.png',44,25.8,18,[(64,'hard',[5,9,10,11,12,13,14,15,16,17,18]),(262,'soft',[13,14,15,16,17,18,19,20]),(406,'pair',[2,3,4,6,7,8,9,11])]),
 '6S':('bj_4d_s17.png',45,25.8,18,[(65,'hard',[5,9,10,11,12,13,14,15,16,17]),(263,'soft',[13,14,15,16,17,18,19]),(407,'pair',[2,3,4,6,7,8,9,11])]),
 '6H':('bj_4d_h17.png',53,25.8,18,[(65,'hard',[5,9,10,11,12,13,14,15,16,17,18]),(281,'soft',[13,14,15,16,17,18,19,20]),(443,'pair',[2,3,4,6,7,8,9,11])]),
 'EURO':('bj_euro.png',55,26,17,[(100,'hard',[5,9,10,11,12,13,14,15,16,17]),(287,'soft',[13,18,19]),(355,'pair',[2,3,4,5,6,7,8,9,10,11])]),
}
tot=bad=0
for k,(f,x0,cw,rh,secs) in G.items():
  im=Image.open(__import__('os').path.join(__import__('os').path.dirname(__file__),'woo_images',f)).convert('RGB')
  for y0,kind,keys in secs:
    for i,key in enumerate(keys):
      y=int(y0+i*rh+4)
      for c in range(10):
        x=int(x0+c*cw+4)
        got=cls_of(im.getpixel((x,y)),k=='EURO'); exp=code_cls(W.T[k][kind][key][c])
        tot+=1
        if got!=exp: bad+=1; print('MISMATCH',k,kind,key,'col',c,'img',got,'tbl',W.T[k][kind][key][c])
print('cells checked',tot,'mismatch',bad)
