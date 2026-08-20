const INSTA_LINK = "https://ipn.eg/S/waeldeban/instapay/3Ubbtt";
const INSTA_ID = "waeldeban@instapay";
function subscribe(plan){
  let amount = 149;
  if(plan==='khatem') amount=299;
  if(plan==='pack5') amount=500;
  if(confirm(`سيتم تحويلك للدفع ${amount}ج\nعلى ${INSTA_ID}\n\nهل تريد المتابعة؟`)){
    window.open(INSTA_LINK, '_blank');
  }
}
function buyRing(id){
  window.open(INSTA_LINK, '_blank');
}
