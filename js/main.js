// Minimal JS: menu toggle and year injection
document.addEventListener('DOMContentLoaded',function(){
  var btn=document.getElementById('menuToggle');
  var nav=document.getElementById('mainNav');
  if(btn && nav){
    btn.addEventListener('click',function(){
      var expanded = this.getAttribute('aria-expanded') === 'true';
      this.setAttribute('aria-expanded', String(!expanded));
      if(nav.style.display === 'block') nav.style.display = '';
      else nav.style.display = 'block';
    });
  }
  var year = new Date().getFullYear();
  ['year','year-about','year-depts','year-staff','year-adm','year-news','year-contact'].forEach(function(id){
    var el = document.getElementById(id);
    if(el) el.textContent = year;
  });
});
