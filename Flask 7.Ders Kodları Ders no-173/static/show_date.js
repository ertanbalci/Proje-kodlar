function show_date() {

  var tarih = new Date();

  var d = tarih.getDate();

  var m = tarih.getMonth()+1;

  var y = tarih.getFullYear();

  bugun = d+"-"+m+"-"+y;

  alert(bugun)

}