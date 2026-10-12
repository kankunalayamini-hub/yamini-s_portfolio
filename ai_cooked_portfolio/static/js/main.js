(function(){
var bar=document.getElementById('bar');
function sc(){var h=document.documentElement;bar.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100||0)+'%'}
addEventListener('scroll',sc,{passive:true});sc();
var els=document.querySelectorAll('section>.wrap>h2,.proj,.skills>div,.two>div');
els.forEach(function(e,i){e.classList.add('rv');e.style.transitionDelay=((i%4)*90)+'ms'});
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('on');(function(e){setTimeout(function(){e.style.transitionDelay='0ms'},1200)})(x.target);io.unobserve(x.target)}})},{threshold:.12});els.forEach(function(e){io.observe(e)})}else{els.forEach(function(e){e.classList.add('on')})}
var t=document.getElementById('t'),w=['Django web apps','REST APIs','MySQL databases','AI agents (learning)'],wi=0,ci=0,del=false;
if(matchMedia('(prefers-reduced-motion:reduce)').matches){t.textContent=w[0]}else{(function tick(){var x=w[wi];ci+=del?-1:1;t.textContent=x.slice(0,ci);var d=del?35:70;if(!del&&ci===x.length){del=true;d=1400}else if(del&&ci===0){del=false;wi=(wi+1)%w.length;d=300}setTimeout(tick,d)})()}
var mb=document.getElementById('menu'),ml=document.getElementById('links');
function setMenu(o){ml.classList.toggle('open',o);mb.classList.toggle('open',o);mb.setAttribute('aria-expanded',o);mb.setAttribute('aria-label',o?'Close menu':'Open menu')}
mb.addEventListener('click',function(e){e.stopPropagation();setMenu(!ml.classList.contains('open'))});
ml.addEventListener('click',function(e){if(e.target.tagName==='A')setMenu(false)});
document.addEventListener('click',function(e){if(!ml.contains(e.target))setMenu(false)});
addEventListener('keydown',function(e){if(e.key==='Escape')setMenu(false)});
addEventListener('resize',function(){if(innerWidth>760)setMenu(false)});
})();