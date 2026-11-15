# 期待値（Wizard of Odds の表と凡例・早期サレンダーの文章リストを、そのまま規則として適用）
import json,itertools,woo_tables as W
DEALERS=[2,3,4,5,6,7,8,9,10,11]
def verified(c):
  if c['hole']=='obo': return False
  if c['hole']=='enhc': return c['decks']==6 and c['s17']=='S17' and c['dbl']=='9-11' and c['das'] and c['sur']=='none'
  if c['sur']=='early': return c['decks']==6
  return True
def configs():
  out=[]
  for decks,s17,das,sur,dbl,hole in itertools.product([1,2,6],['S17','H17'],[True,False],['none','late','early'],['any','9-11','10-11'],['peek','enhc','obo']):
    c=dict(decks=decks,s17=s17,das=das,sur=sur,dbl=dbl,hole=hole)
    if verified(c): out.append(c)
  return out
def hands():
  hs=[]
  for t in range(5,21): hs.append(dict(isPair=False,pairVal=0,soft=False,total=t,initial=True,fromSplit=False))
  for t in range(13,21): hs.append(dict(isPair=False,pairVal=0,soft=True,total=t,initial=True,fromSplit=False))
  for p in range(2,12): hs.append(dict(isPair=True,pairVal=p,soft=(p==11),total=(12 if p==11 else 2*p),initial=True,fromSplit=False))
  for t in range(4,22): hs.append(dict(isPair=False,pairVal=0,soft=False,total=t,initial=False,fromSplit=False))
  for t in range(13,22): hs.append(dict(isPair=False,pairVal=0,soft=True,total=t,initial=False,fromSplit=False))
  return hs
def can_double(c,h):
  if not h['initial']: return False
  if h['fromSplit'] and not c['das']: return False
  if c['dbl']=='any': return True
  st={'9-11':[9,10,11],'10-11':[10,11]}[c['dbl']]
  return (not h['soft']) and h['total'] in st
def can_surr(c,h): return c['sur']!='none' and h['initial'] and not h['fromSplit']
def code(c,h,d):
  tb=W.T['EURO'] if c['hole']=='enhc' else W.T[f"{c['decks']}{c['s17'][0]}"]
  i=DEALERS.index(d)
  if h['isPair'] and h['pairVal'] in tb['pair']: return tb['pair'][h['pairVal']][i]
  if h['soft']: return tb['soft'][h['total']][i]
  return tb['hard'][h['total']][i]
def expected(c,h,d):
  if c['sur']=='early' and can_surr(c,h):
    if d==11:
      if h['isPair'] and (h['pairVal'] in (3,6,7,8) or (h['pairVal']==2 and c['s17']=='H17')): return 'surrender'
      if not h['isPair'] and not h['soft'] and (5<=h['total']<=7 or 12<=h['total']<=17): return 'surrender'
    if d==10:
      if h['isPair'] and h['pairVal'] in (7,8): return 'surrender'
      if not h['isPair'] and not h['soft'] and 14<=h['total']<=16: return 'surrender'
  k=code(c,h,d); dbl=can_double(c,h); sur=can_surr(c,h); das=c['das']
  dh='double' if dbl else 'hit'
  return {'H':'hit','S':'stand','D':dh,'Ds':'double' if dbl else 'stand','P':'split',
   'Ph':'split' if das else 'hit','Pd':'split' if das else dh,'Ps':'split' if das else 'stand',
   'Rh':'surrender' if sur else 'hit','Rs':'surrender' if sur else 'stand','Rp':'surrender' if sur else 'split',
   'Rp2':'surrender' if (sur and not das) else 'split'}[k]
if __name__=='__main__':
  rows=[]
  for c in configs():
    for h in hands():
      for d in DEALERS: rows.append([c,h,d,expected(c,h,d)])
  json.dump(rows,open('expected.json','w'))
  print('configs',len(configs()),'cells',len(rows))
