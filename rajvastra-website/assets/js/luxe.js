(function(){
  function toast(m){var t=document.createElement('div');t.className='rv-toast';t.textContent=m;document.body.appendChild(t);setTimeout(function(){t.classList.add('show')},20);setTimeout(function(){t.classList.remove('show');setTimeout(function(){t.remove()},500)},4500);}
  document.querySelectorAll('.newsletter-form').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();toast('Thank you for subscribing to the Rajvastra newsletter.');f.reset();});});
  document.querySelectorAll('.rv-form').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();toast(f.getAttribute('data-msg')||'Thank you!');f.reset();});});
  var q=new URLSearchParams(location.search);
  var enq=document.getElementById('enquiry');
  if(enq){var s=q.get('subject'),p=q.get('product');if(s){var sel=enq.querySelector('select');for(var i=0;i<sel.options.length;i++){if(sel.options[i].text===s){sel.selectedIndex=i}}}
    if(p){enq.querySelector('textarea').value='I would like to enquire about: '+p+'.\n\nQuantity / requirement: '}}
  var grid=document.getElementById('rv-grid');
  if(grid){var btns=document.querySelectorAll('.filter-btn');function f(t){btns.forEach(function(b){b.classList.toggle('active',b.dataset.filter===t)});grid.querySelectorAll('.rv-item').forEach(function(i){i.classList.toggle('hide',t!=='all'&&i.dataset.type!==t)})}
    btns.forEach(function(b){b.addEventListener('click',function(){f(b.dataset.filter)})});if(q.get('type'))f(q.get('type'));}
  var res=document.getElementById('sres');
  if(res){var term=(q.get('q')||'').trim().toLowerCase();document.getElementById('sq').value=q.get('q')||'';
    var hits=(window.SITE_INDEX||[]).filter(function(p){return term&&(p.t+' '+p.d+' '+p.k).toLowerCase().indexOf(term)>-1});
    document.getElementById('sinfo').textContent=term?(hits.length+' result(s) for “'+q.get('q')+'”'):'Type something to search.';
    res.innerHTML=hits.map(function(p){return '<div class="col-lg-4 col-md-6"><div class="rv-card">'+(p.img?'<a href="'+p.u+'" class="rv-img" style="aspect-ratio:3/2"><img src="'+p.img+'" alt=""><span class="rv-tag">'+p.k+'</span></a>':'')+'<div class="rv-body"><h3><a href="'+p.u+'">'+p.t+'</a></h3><p>'+p.d+'</p><a class="link-btn" href="'+p.u+'">Open →</a></div></div></div>'}).join('');}
})();
