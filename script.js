function createParticles(){
 const c=document.getElementById('particles');
 for(let i=0;i<30;i++){let p=document.createElement('div');p.className='particle';p.style.left=Math.random()*100+'%';p.style.top=Math.random()*100+'%';p.style.animationDuration=(Math.random()*8+6)+'s';p.style.animationDelay=Math.random()*10+'s';c.appendChild(p)}
}
function simulateLoading(){
 const bar=document.getElementById('loadingBar'),txt=document.getElementById('loadingText');
 const msgs=['جاري تجهيز مملكتك...','فتح خزائن الحكمة...','استدعاء الجنود الذكية...','ترجمة 200 لسان...','تجهيز محكمتك...','عالمك ينتظرك...'];
 let prog=0,idx=0;
 let intv=setInterval(()=>{prog+=Math.random()*2+1;if(prog>=100){prog=100;clearInterval(intv);setTimeout(transitionToApp,600)}bar.style.width=prog+'%';if(prog>idx*20&&idx<msgs.length-1){idx++;txt.textContent=msgs[idx]}},200);
}
function transitionToApp(){
 document.getElementById('splash-screen').style.opacity='0';
 setTimeout(()=>{
  document.getElementById('splash-screen').style.display='none';
  document.getElementById('kingdom').style.display='block';
  document.body.style.overflow='auto';
  loadRings();
 },1000);
}
function loadRings(){
 fetch('rings.json').then(r=>r.json()).then(rings=>{
  const g=document.getElementById('rings-grid');
  g.innerHTML=rings.slice(0,100).map(r=>`<div class="card ${r.rarity}"><h4>${r.name}</h4><p>${r.rarity}</p><small>⚡ ${r.power}</small></div>`).join('')+`<p style="grid-column:1/-1;text-align:center;margin-top:20px;color:#C9A96E">و ${rings.length-100} خاتم آخر مخفي في مملكتك... تم البناء بواسطة Adam18691 على Termux</p>`;
 });
}
document.addEventListener('DOMContentLoaded',()=>{createParticles();simulateLoading();document.getElementById('skipBtn').onclick=transitionToApp});
