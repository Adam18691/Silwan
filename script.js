let rings=[];
try{
 rings=JSON.parse(localStorage.getItem('silwan_rings'))||[];
}catch(e){}
if(rings.length===0){
 // لو مفيش rings.json هيعمل 1000 وهمي زي الصورة
 for(let i=1;i<=1000;i++){
   let rarity=i===1||i===7||i===8?'Legendary':i===11?'Epic':i===2?'Rare':'Common';
   rings.push({id:i,rarity,power:Math.floor(Math.random()*100)+1});
 }
}
function render(){
 const container=document.getElementById('rings');
 const struct=document.getElementById('structDetails');
 if(!container) return;
 container.innerHTML='';
 let counts={Legendary:0,Epic:0,Rare:0,Common:0,totalPower:0};
 rings.slice(0,100).forEach(r=>{
   counts[r.rarity]++;
   counts.totalPower+=r.power;
   const div=document.createElement('div');
   div.className=`ring-card ${r.rarity.toLowerCase()}`;
   div.innerHTML=`<b>Ring #${r.id}</b><br>${r.rarity}<br>${r.power} ⚡<br><button class='btn btn-gold' style='margin-top:8px;width:100%' onclick='buyRing(${r.id})'>شراء</button>`;
   div.onclick=(e)=>{ if(e.target.tagName!=='BUTTON') buyRing(r.id); };
   container.appendChild(div);
 });
 if(struct){
   struct.innerHTML=`Legendary: ${counts.Legendary} | Epic: ${counts.Epic} | Rare: ${counts.Rare} | Common: ${counts.Common}<br>إجمالي الطاقة (أول 100): ${counts.totalPower} ⚡<br>إجمالي الخواتم: ${rings.length}`;
 }
}
render();
