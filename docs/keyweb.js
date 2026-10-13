// The Key Web: keys.json + pages.json as a force-directed graph, letters pulled towards their year on the x axis.
// Keys coloured by who made them (period / scholar / rebuilt here), sized by the letters they read; failed tests as red
// dashed edges behind a filter; zoom and pan; a key card with its image; a link per key (keys.html#k-balbases).
(async()=>{
  const root=document.getElementById('kw'); if(!root || !window.d3) return;
  const [K,pages]=await Promise.all([fetch('keys.json').then(r=>r.json()),fetch('pages.json').then(r=>r.json())]);
  const page=Object.fromEntries(pages.map(p=>[p.slug,p]));
  const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const yr=y=>y==null?'':Math.floor(y);
  const BANDS=[['period','Keys of the period'],['scholar',"Scholars' keys"],['here','Rebuilt here']];
  const band=k=>k.kind==="scholar's key"?'scholar':k.kind==='rebuilt here'?'here':'period';
  const EDGES=[['rebuilt','rebuilt from',h=>/rebuilt/.test(h)],['unchanged','read unchanged',h=>/unchanged|explained/.test(h)],
               ['adapted','adapted or partial',h=>/adapt|partial/.test(h)],['tried','tried, did not fit',h=>h==='tried']];
  const ecls=h=>(EDGES.find(e=>e[2](h))||EDGES[1])[0];
  const W=1100,H=760;

  // nodes: keys, letters, sources; edges: read links, tried links, source links
  const nodes=[], byId={}, add=n=>(byId[n.id]=n,nodes.push(n),n);
  K.keys.forEach(k=>add({...k,type:'key',band:band(k),reads:[],tried:[],srcs:[]}));
  (K.sources||[]).forEach(s=>add({...s,type:'src'}));
  const letter=slug=>{ const p=page[slug]; if(!p) return null;
    return byId['t:'+slug]||add({id:'t:'+slug,type:'t',slug,label:p.label,y:typeof p.y==='number'?p.y:null,st:p.st,stt:p.stt,reads:[],tried:[]}); };
  const links=[];
  K.links.forEach(l=>{ const k=byId[l.key], t=letter(l.target); if(!k||!t) return;
    const e={source:k,target:t,how:l.how||'',note:l.note||'',e:ecls(l.how||'')}; links.push(e); k.reads.push(e); t.reads.push(e); });
  (K.tried||[]).forEach(l=>{ const k=byId[l.key], t=letter(l.target); if(!k||!t) return;
    const e={source:k,target:t,how:'tried',note:l.note||'',e:'tried'}; links.push(e); k.tried.push(e); t.tried.push(e); });
  (K.source_links||[]).forEach(l=>{ const s=byId[l.source], k=byId[l.key]; if(!s||!k) return; links.push({source:s,target:k,how:'src',e:'src',me:s.id==='s-cyphersolver'}); if(s.id!=='s-cyphersolver') k.srcs.push(s.label); });
  for(let i=nodes.length-1;i>=0;i--){ const n=nodes[i]; if(n.type==='key'&&!n.reads.length&&!n.tried.length){ delete byId[n.id]; nodes.splice(i,1); } }
  nodes.forEach(n=>{
    if(n.type==='key'){ n.letters=new Set(n.reads.map(e=>e.target.slug)).size; n.tonly=!n.letters; }
    if(n.type==='t') n.tonly=!n.reads.length;
    n.hay=(n.type==='key'?[n.id,n.label,n.by,n.kind,n.note,n.year,n.found,...n.srcs,...[...n.reads,...n.tried].flatMap(e=>[e.target.slug,e.target.label,e.note])]
         :n.type==='t'?[n.slug,n.label,...[...n.reads,...n.tried].flatMap(e=>[e.source.label,e.note])]:[n.label]).join(' ').toLowerCase();
  });
  const keys=nodes.filter(n=>n.type==='key');

  // stats
  const lset=new Set(K.links.map(l=>l.target).filter(s=>page[s])), ntried=(K.tried||[]).length;
  document.getElementById('kwstats').innerHTML=[[keys.filter(k=>k.letters).length,'keys that read a letter'],[lset.size,'letters and series read with them'],
    [keys.filter(k=>k.letters>=2).length,'keys that read more than one'],[keys.filter(k=>k.band==='here'&&k.letters).length,'keys rebuilt here'],[ntried,'tests of a key that did not fit']]
    .map(([n,t])=>`<span><b>${n}</b>${t}</span>`).join('');

  // layout: years on x, computed once from a fixed seed so the web looks the same on every visit
  const kyear=k=>{ const ys=[...k.reads,...(k.letters?[]:k.tried)].map(e=>e.target.y).filter(y=>y!=null); return ys.length?d3.mean(ys):(k.year||1600); };
  nodes.forEach(n=>{ n.y0=n.type==='t'?(n.y??1600):n.type==='key'?kyear(n):null; });
  nodes.filter(n=>n.type==='src').forEach(s=>{ const ks=links.filter(l=>l.source===s).map(l=>l.target.y0); s.y0=ks.length?d3.mean(ks):1600; });
  const ext=d3.extent(nodes,n=>n.y0), x=d3.scaleLinear().domain([Math.floor(ext[0]/50)*50,Math.ceil(ext[1]/50)*50]).range([70,W-70]);
  const rnd=d3.randomLcg(0.4242);
  nodes.forEach(n=>{ n.x=x(n.y0)+(rnd()-.5)*20; n.y=H/2+(rnd()-.5)*320; });
  const deg=n=>n.type==='key'?n.letters:0;
  const sim=d3.forceSimulation(nodes).randomSource(rnd)
    .force('link',d3.forceLink(links).distance(l=>l.e==='src'?110:l.e==='tried'?60:40).strength(l=>l.e==='src'?.12:l.e==='tried'?(l.source.tonly?.6:.05):.75))
    .force('charge',d3.forceManyBody().strength(n=>n.type==='t'?-60:n.type==='src'?-300:-120-deg(n)*30).distanceMax(260))
    .force('x',d3.forceX(n=>x(n.y0)).strength(n=>n.type==='src'?.03:.2))
    .force('y',d3.forceY(H/2).strength(.1))
    .force('collide',d3.forceCollide(n=>n.type==='t'?9:n.type==='src'?30:12+deg(n)*2))
    .stop();
  for(let i=0;i<420;i++) sim.tick();
  nodes.forEach(n=>{ n.x=Math.max(30,Math.min(W-30,n.x)); n.y=Math.max(30,Math.min(H-60,n.y)); });

  // drawing
  const svg=d3.select(root).insert('svg',':first-child').attr('viewBox',`0 0 ${W} ${H}`).attr('role','img')
    .attr('aria-label','Network of cipher keys and the letters they read');
  const view=svg.append('g');
  const ax=view.append('g').attr('class','axis');
  x.ticks(8).forEach(t=>{ ax.append('line').attr('x1',x(t)).attr('x2',x(t)).attr('y1',10).attr('y2',H-40);
    ax.append('text').attr('x',x(t)).attr('y',H-26).attr('text-anchor','middle').text(t); });
  const lk=view.append('g').selectAll('path').data(links).join('path').attr('class',l=>'lk '+l.e+(l.me?' me':''));
  const nd=view.append('g').selectAll('g').data(nodes).join('g')
    .attr('class',n=>['nd',n.type,n.band?'b-'+n.band:'',n.st||'',n.tonly?'tonly':'',n.id==='s-cyphersolver'?'me':''].join(' '))
    .attr('tabindex',0).attr('role','button').attr('aria-label',n=>n.label);
  const KEYPATH='M-3,-2.5a4.5,4.5 0 1,1 0,5h10l2,-2.5l-2,-2.5z';          // a small key: bow and blade
  nd.filter(n=>n.type==='key').append('path').attr('d',KEYPATH).attr('transform',n=>`scale(${1.05+Math.min(n.letters,8)*.32})`);
  nd.filter(n=>n.type==='src').append('circle').attr('r',n=>9+Math.sqrt(links.filter(l=>l.source===n).length)*2.2);
  nd.filter(n=>n.type==='t').append('circle').attr('r',n=>3.5+Math.min(n.reads.length+n.tried.length,4));
  const short=s=>s.length>38?s.slice(0,36)+'…':s;
  nd.append('text').attr('dy',n=>n.type==='t'?'-.9em':n.type==='src'?'2.3em':'1.9em').attr('text-anchor','middle')
    .text(n=>short(n.type==='t'?n.label.replace(/\s*\(.*?\)\s*/g,' ').trim():n.label));
  const arc=l=>{ const dx=l.target.x-l.source.x, dy=l.target.y-l.source.y, dr=Math.hypot(dx,dy)*1.6;
    return `M${l.source.x},${l.source.y}A${dr},${dr} 0 0,1 ${l.target.x},${l.target.y}`; };
  const draw=()=>{ lk.attr('d',arc); nd.attr('transform',n=>`translate(${n.x},${n.y})`); };
  draw();

  // standing labels: keys that read several letters and the sources, greedily, biggest first, skipping overlaps
  const boxes=[];
  nodes.filter(n=>n.type==='src'||(n.type==='key'&&n.letters>=2)).sort((a,b)=>deg(b)-deg(a)).forEach(n=>{
    const w=Math.min(n.label.length,38)*6.2, b={x0:n.x-w/2,x1:n.x+w/2,y0:n.y+8,y1:n.y+24};
    if(!boxes.some(o=>b.x0<o.x1&&b.x1>o.x0&&b.y0<o.y1&&b.y1>o.y0)){ boxes.push(b); n.lab=true; } });
  nd.classed('lab',n=>!!n.lab);

  // zoom and pan; labels keep their size as you zoom in
  const zoom=d3.zoom().scaleExtent([.6,8]).on('zoom',e=>{ view.attr('transform',e.transform);
    nd.selectAll('text').attr('transform',`scale(${1/Math.sqrt(e.transform.k)})`); });
  svg.call(zoom).on('dblclick.zoom',null);
  // on a phone the svg is taller than the web and crops its sides (slice), so fitting works on the visible part
  const narrow=()=>root.clientWidth<700;
  svg.attr('preserveAspectRatio',narrow()?'xMidYMid slice':'xMidYMid meet');
  const vis=()=>{ const r=svg.node().getBoundingClientRect(), s=narrow()?Math.max(r.width/W,r.height/H):Math.min(r.width/W,r.height/H);
    return [Math.min(W,r.width/s)||W,Math.min(H,r.height/s)||H]; };
  const fit=(ns,dur=600,kmax=8)=>{ const xs=ns.map(n=>n.x), ys=ns.map(n=>n.y); if(!ns.length) return;
    const [vw,vh]=vis(), [x0,x1]=d3.extent(xs), [y0,y1]=d3.extent(ys), k=Math.min(kmax,.85/Math.max((x1-x0+80)/vw,(y1-y0+80)/vh));
    const to=d3.zoomIdentity.translate(W/2,H/2).scale(Math.max(.6,k)).translate(-(x0+x1)/2,-(y0+y1)/2);
    if(matchMedia('(prefers-reduced-motion: reduce)').matches||document.hidden) svg.call(zoom.transform,to);
    else svg.transition().duration(dur).call(zoom.transform,to); };
  document.getElementById('kwfit').addEventListener('click',()=>fit(nodes.filter(n=>!hidden(n)),500));
  const lb=document.getElementById('kwlabels');
  lb.addEventListener('click',()=>{ const on=!root.classList.contains('all'); root.classList.toggle('all',on); lb.setAttribute('aria-pressed',on); });

  // drag a node (a light reheat of the layout)
  sim.on('tick',draw);
  nd.call(d3.drag().on('start',(e,n)=>{ if(!e.active) sim.alpha(.15).restart(); n.fx=n.x; n.fy=n.y; })
    .on('drag',(e,n)=>{ n.fx=e.x; n.fy=e.y; }).on('end',(e,n)=>{ if(!e.active) sim.alphaTarget(0); n.fx=null; n.fy=null; }));

  // filters: bands, edge kinds and a search. Failed tests start hidden; the rest dims rather than disappears
  const st={q:'',bands:new Set(BANDS.map(b=>b[0])),edges:new Set(['rebuilt','unchanged','adapted'])};
  const chips=(el,list,set,cls)=>{ el.innerHTML=list.map(([id,label])=>`<button type="button" class="kw-chip ${cls(id)}" data-v="${id}" aria-pressed="${set.has(id)}">${cls(id).startsWith('e-')?'<i></i>':''}${esc(label)}</button>`).join('');
    el.addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; const v=b.dataset.v;
      set.has(v)?set.delete(v):set.add(v); b.setAttribute('aria-pressed',set.has(v)); apply(); }); };
  chips(document.getElementById('kwband'),BANDS,st.bands,id=>'b-'+id);
  chips(document.getElementById('kwedge'),EDGES,st.edges,id=>'e-'+id);
  const q=document.getElementById('kwq');
  q.addEventListener('input',()=>{ st.q=q.value.trim().toLowerCase(); apply(); });
  q.addEventListener('keydown',e=>{ if(e.key==='Enter'){ const m=nodes.filter(n=>n.type!=='src'&&!hidden(n)&&matches(n)); if(m.length) fit(m.length>40?m.slice(0,40):m); } });
  const showE=l=>l.e==='src'||st.edges.has(l.e);
  const hidden=n=>n.type==='key'?![...n.reads,...n.tried].some(showE):n.type==='t'?![...n.reads,...n.tried].some(showE):false;
  const matches=n=>(!st.q||st.q.split(/\s+/).every(w=>n.hay.includes(w)));
  const keyOn=k=>st.bands.has(k.band)&&matches(k);
  const lit=n=>n.type==='key'?keyOn(n):n.type==='t'?(matches(n)||[...n.reads,...n.tried].some(l=>showE(l)&&keyOn(l.source))):!st.q;
  function apply(){
    nd.style('display',n=>hidden(n)?'none':null).classed('dim',n=>!lit(n));
    lk.style('display',l=>showE(l)&&!hidden(l.source)&&!hidden(l.target)?null:'none').classed('dim',l=>l.e==='src'?!!st.q:!(keyOn(l.source)));
    const shown=keys.filter(k=>!hidden(k)&&keyOn(k)).length;
    document.getElementById('kwcount').textContent=`${shown} of ${keys.length} keys`;
    renderTried();
  }

  // focus: a node, its edges and neighbours; a click pins it and opens its card
  const side=document.getElementById('kwside'), card=document.getElementById('kwcard'), idle=card.innerHTML;
  const nb=n=>links.filter(l=>(l.source===n||l.target===n)&&showE(l));
  function focus(n){
    root.classList.toggle('focus',!!n);
    if(!n){ nd.classed('hot',false); lk.classed('hot',false); return; }
    const ls=nb(n), set=new Set([n]); ls.forEach(l=>{ set.add(l.source); set.add(l.target); });
    nd.classed('hot',d=>set.has(d)); lk.classed('hot',l=>ls.includes(l));
  }
  const decode=k=>{ const m=(k.kind==='DECODE key record')&&(k.label.match(/\bR(\d{2,5})\b/)||k.id.match(/^k-r(\d{2,5})$/)); return m?`https://de-crypt.org/decrypt-web/RecordsView/${m[1]}`:null; };
  const tli=e=>`<li><a href="${e.target.slug}.html">${esc(e.target.label)}</a><small>${esc(e.how)}${e.note?' · '+esc(e.note):''}${e.target.y!=null?' · '+yr(e.target.y):''} · ${esc(e.target.stt)}</small></li>`;
  const kli=e=>`<li><button type="button" class="kn" data-key="${esc(e.source.id)}">${esc(e.source.label)}</button><small>${esc(e.how)}${e.note?' · '+esc(e.note):''}</small></li>`;
  function cardFor(n){
    if(n.type==='key'){ const bl=BANDS.find(b=>b[0]===n.band)[1], dl=decode(n);
      return `<p class="k">${esc(n.kind)} · ${bl}</p><h3>${esc(n.label)}</h3>
      <p class="by">${[n.by,n.year&&('key of '+n.year),n.found&&((n.band==='scholar'?'published ':'found ')+n.found)].filter(Boolean).map(esc).join(' · ')}${n.srcs.length?'<br>Held or published by '+n.srcs.map(esc).join(', '):''}</p>
      ${n.image?`<figure data-credit="${esc(n.image.credit)}"><a href="${esc(n.image.page)}.html"><img src="${esc(n.image.src)}" alt="${esc(n.image.caption||n.label)}" loading="lazy"></a><figcaption>${esc((n.image.caption||'').slice(0,160))}${(n.image.caption||'').length>160?'…':''} <span class="credit">Image: ${esc(n.image.credit)}</span></figcaption></figure>`:''}
      <p>${esc(n.note)}</p>
      ${n.reads.length?`<h4>Read ${n.letters} letter${n.letters>1?'s':''}</h4><ul>${n.reads.map(tli).join('')}</ul>`:''}
      ${n.tried.length?`<h4>Tried, did not fit</h4><ul>${n.tried.map(tli).join('')}</ul>`:''}
      <div class="acts"><button type="button" data-copy>Copy link</button>${dl?`<a href="${dl}" rel="noopener">DECODE record &#8599;</a>`:''}</div>`; }
    if(n.type==='t') return `<p class="k">Letter · ${esc(n.stt)}${n.y!=null?' · '+yr(n.y):''}</p><h3><a href="${n.slug}.html">${esc(n.label)}</a></h3>
      ${n.reads.length?`<h4>Read with</h4><ul>${n.reads.map(kli).join('')}</ul>`:''}${n.tried.length?`<h4>Tried, did not fit</h4><ul>${n.tried.map(kli).join('')}</ul>`:''}
      <div class="acts"><a href="${n.slug}.html">Open the write-up &rarr;</a></div>`;
    const ks=links.filter(l=>l.source===n).map(l=>l.target);
    return `<p class="k">Source</p><h3>${esc(n.label)}</h3><ul>${ks.map(k=>`<li><button type="button" class="kn" data-key="${esc(k.id)}">${esc(k.label)}</button><small>${k.letters} letter${k.letters===1?'':'s'}</small></li>`).join('')}</ul>`;
  }
  let pinned=null;
  function pin(n,{zoomTo=false,push=true}={}){
    pinned=n||null; nd.classed('pin',d=>d===pinned); focus(pinned);
    if(!n){ card.innerHTML=idle; side.classList.remove('open'); if(push) history.replaceState(null,'',location.pathname+location.search); return; }
    if(n.type==='key'&&!st.edges.has('tried')&&n.tonly){ st.edges.add('tried'); document.querySelector('#kwedge [data-v="tried"]').setAttribute('aria-pressed','true'); apply(); focus(n); }
    card.innerHTML=cardFor(n); side.classList.add('open'); side.scrollTop=0;
    if(push&&n.type==='key') history.replaceState(null,'','#'+n.id);
    if(zoomTo){ const ns=[n,...nb(n).filter(l=>l.e!=='src').map(l=>l.source===n?l.target:l.source)]; fit(ns,600,4); }
  }
  nd.on('pointerenter',(e,n)=>{ if(!pinned&&e.pointerType!=='touch') focus(n); }).on('pointerleave',()=>{ if(!pinned) focus(null); })
    .on('focus',(e,n)=>{ if(!pinned) focus(n); }).on('blur',()=>{ if(!pinned) focus(null); })
    .on('click',(e,n)=>{ e.stopPropagation(); pin(pinned===n?null:n); })
    .on('keydown',(e,n)=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); pin(n); } });
  svg.on('click',e=>{ if(e.defaultPrevented) return; if(pinned) pin(null); });
  document.addEventListener('click',e=>{
    const b=e.target.closest('[data-key]'); if(b){ const n=byId[b.dataset.key]; if(n){ pin(n,{zoomTo:true}); root.scrollIntoView({block:'nearest'}); } return; }
    if(e.target.closest('[data-copy]')){ const u=location.href; (navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(()=>{ e.target.textContent='Link copied'; },()=>prompt('Link to this key',u)); }
  });
  side.querySelector('.x').addEventListener('click',()=>pin(null));
  document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&pinned&&!document.querySelector('#search:not([hidden])')) pin(null); });

  // keys tried and ruled out, grouped by letter; twelve until asked for all, or while a search or band filter is on
  let showAll=false;
  document.getElementById('triedlist').insertAdjacentHTML('afterend','<button type="button" class="kw-chip" id="triedmore" hidden></button>');
  const more=document.getElementById('triedmore'); more.addEventListener('click',()=>{ showAll=true; renderTried(); });
  function renderTried(){
    const ts=nodes.filter(n=>n.type==='t'&&n.tried.some(e=>keyOn(e.source))).sort((a,b)=>(a.y??0)-(b.y??0));
    const filtered=st.q||st.bands.size<BANDS.length, list=showAll||filtered?ts:ts.slice(0,12);
    more.hidden=list.length===ts.length; more.textContent=`Show all ${ts.length} letters`;
    document.getElementById('triedlist').innerHTML=list.map(t=>`<li><div class="tgt"><a href="${t.slug}.html">${esc(t.label)}</a><small>${t.y!=null?yr(t.y)+' · ':''}${esc(t.stt)}</small></div>
      <ul>${t.tried.filter(e=>keyOn(e.source)).map(e=>`<li><button type="button" class="kn" data-key="${esc(e.source.id)}">${esc(e.source.label)}</button>${e.note?' — '+esc(e.note):''}</li>`).join('')}</ul></li>`).join('')
      ||'<li class="kw-help">No ruled-out key matches.</li>';
  }

  const fromHash=()=>{ const h=decodeURIComponent(location.hash.slice(1));
    if(h.startsWith('q=')){ q.value=h.slice(2); st.q=h.slice(2).toLowerCase(); apply(); }
    else if(byId[h]){ pin(byId[h],{zoomTo:true,push:false}); window.scrollTo({top:root.getBoundingClientRect().top+scrollY-90,behavior:'instant'}); } };
  window.addEventListener('hashchange',fromHash);
  apply(); setTimeout(fromHash,80);   // after the layout settles, or the scroll to the web lands short
})();
