const SILWAN_SECRETS={
 36:"النمط الإدراكي الشفائي - أمواج ذهبية حسب التنفس",
 37:"الهارمونية الفارغة - فراغ مقدس 3 ثواني",
 38:"الريح المرئية - جزيئات ذهب",
 39:"محراب الضوء - ظلال حية جيروسكوب",
 40:"التناغم الهندسي المقدس - 3% ألفا"
};
const PACKAGES={
  rih:{name:"الريح",price:"0$",features:["3 جلسات/أسبوع","3 تمارين نقلة","200 لغة قراءة","طوارئ"]},
  jinn:{name:"الجن",price:"49.99$ / 499$ سنوي",features:["غير محدود","محكمة النفس العميقة","تحليل صوت/فيديو","تقارير أسبوعية"]},
  khatem:{name:"الخاتم",price:"69.99$ / 699$ سنوي",features:["جلسة فيديو مع معالج","تخصيص Qwen","الإرث الحي 33","الوعي المتوازي 35"]}
};
const SECRET_KEY="Silwan_1000_Kingdom";
function enc(t){return btoa(SECRET_KEY+"::"+t)} function dec(e){try{return atob(e).split("::")[1]}catch{return""}}
function saveQwenKey(){const k=document.getElementById('qwenKeyInput').value.trim();if(!k){alert('ادخل المفتاح');return}localStorage.setItem('qwen_key_enc',enc(k));alert('🔐 تم حفظ المفتاح مشفر - Qwen أونلاين جاهز');checkKey()}
function getQwenKey(){const e=localStorage.getItem('qwen_key_enc');return e?dec(e):""}
function checkKey(){const h=!!getQwenKey();document.getElementById('keyStatus').innerHTML=h?'🔐 Qwen أونلاين 🧞 جاهز | الأوفلاين 🔐 جاهز':'⚠️ ضع مفتاح Qwen لتفعيل الجن العربي'}
async function askUnified(){
  const key=getQwenKey(); const p=document.getElementById('prompt').value.trim(); const out=document.getElementById('output');
  if(!p){alert('اكتب نيتك');return}
  const local=`👑 سِلْوَان: ${p}\nتم اختيار العالم: ${p.includes('صمت')?'مثوى الصمت':p.includes('نقلة')?'مقام النقلة':'محكمة النفس'}\nالسر المفعل: ${Object.values(SILWAN_SECRETS).join(' | ')}`;
  if(!key){out.innerText=local+"\n(يعمل أوفلاين - الخاتم الصامت)";return}
  out.innerText="⏳ الجن العربي 🧞 يفكر مع الريح 🌪️...";
  try{
    const r=await fetch("https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions",{method:"POST",headers:{"Content-Type":"application/json","Authorization":"Bearer "+key},body:JSON.stringify({model:"qwen-plus",messages:[{role:"system",content:`انت سِلْوَان - خاتم سليمان. عوالمك: مثوى الصمت، مقام النقلة، محكمة النفس. أسرارك 40 سر. باقاتك: ريح 0$، جن 49.99$، خاتم 69.99$. دفع: waeldeban@instapay. نبرة: مهيبة حازمة روحانية. شعارك: لست مريضاً بل ملك لم يكتشف خاتمه بعد.`},{role:"user",content:p}]})});
    const d=await r.json(); out.innerText=d.choices?.[0]?.message?.content||local;
  }catch(e){out.innerText=local}
}
