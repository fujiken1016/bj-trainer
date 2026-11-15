// 使い方: node verify_engine.js <index.html> <expected.json>
const fs=require('fs');
const html=fs.readFileSync(process.argv[2],'utf8');
const a=html.indexOf('/* ============ RULES ============ */'), b=html.indexOf('const actionToLetter');
if(a<0||b<0) throw new Error('engine markers not found');
const src=html.slice(a,b)+';\nmodule.exports={rules,decide,typeof_rulesVerified:(typeof rulesVerified==="function"?rulesVerified:null)};';
const m={exports:{}}; new Function('module',src)(m);
const {rules,decide,typeof_rulesVerified:rv}=m.exports;
const rows=JSON.parse(fs.readFileSync(process.argv[3],'utf8'));
let n=0,bad=0; const groups={};
for(const [c,h,d,exp] of rows){
  Object.assign(rules,{decks:c.decks,soft17:c.s17,das:c.das,surrender:c.sur,dbl:c.dbl,hole:c.hole,variant:'classic'});
  const got=decide(h,d); n++;
  if(got!==exp){bad++; const g=`${c.decks}D ${c.s17} das=${c.das} sur=${c.sur} dbl=${c.dbl} ${c.hole}`; (groups[g]=groups[g]||[]).push(`${h.isPair?'P'+h.pairVal:(h.soft?'S':'H')+h.total}${h.initial?'':'(3+)'} v${d}: ${got}≠${exp}`);}
}
const gk=Object.keys(groups);
console.log(`cells=${n} mismatch=${bad} rate=${(bad/n*100).toFixed(2)}% configs_with_mismatch=${gk.length}`);
if(process.argv[4]==='-v') gk.slice(0,200).forEach(g=>console.log(g,'|',groups[g].length,'|',groups[g].slice(0,8).join(', ')));
if(rv){ // 未検証の組み合わせは UI で選べないこと
  const blocked=[{decks:6,soft17:'S17',das:true,surrender:'late',dbl:'any',hole:'obo'},{decks:6,soft17:'S17',das:true,surrender:'late',dbl:'any',hole:'enhc'},{decks:1,soft17:'S17',das:true,surrender:'early',dbl:'any',hole:'peek'}];
  const leak=blocked.filter(r=>rv({...r,variant:'classic'}));
  const okv=rv({decks:6,soft17:'S17',das:true,surrender:'late',dbl:'any',hole:'peek',variant:'classic'});
  console.log('rulesVerified: unverified-allowed='+leak.length+' standard-allowed='+okv);
  if(leak.length||!okv) bad++;
}
process.exit(bad?1:0);
