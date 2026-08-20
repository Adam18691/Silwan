const INSTA_LINK = "https://ipn.eg/S/waeldeban/instapay/3Ubbtt";
function subscribe(plan){
  let amount = 149;
  if(plan === 'khatem') amount = 299;
  if(plan === 'pack5') amount = 500;
  window.open(INSTA_LINK, '_blank');
}
