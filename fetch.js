fetch('http://127.0.0.1:5000/api/checkins')
.then(response => response.json())
.then(json => {
  var datadiv = document.getElementById("data");
  var tbl = document.createElement("table");
  var tblHead = document.createElement("thead");
  var tblBody = document.createElement("tbody");
  var keys = ['Datum', 'ID', 'Gevoel'];
  var header = document.createElement("tr");
  keys.forEach(function (key) {
    //Object.keys(checkin).forEach(function (key) {
    // do something with obj[key]
  var cell = document.createElement("th");
  var cellText = document.createTextNode(key);
  cell.appendChild(cellText);
  header.appendChild(cell);
 });  
 tblHead.appendChild(header);
 tbl.appendChild(tblHead);



  json.forEach(checkin => {
    // creates a table row
    var row = document.createElement("tr");
    keys.forEach(function (key) {
      //Object.keys(checkin).forEach(function (key) {
      // do something with obj[key]
    var cell = document.createElement("td");
    var cellText = document.createTextNode(checkin[key]);
    cell.appendChild(cellText);
    row.appendChild(cell);
   });  

    // add the row to the end of the table body
    tblBody.appendChild(row);
  });
  tbl.appendChild(tblBody);
  // appends <table> into <body>
  datadiv.appendChild(tbl);
  // sets the border attribute of tbl to 2;
  tbl.setAttribute("border", "2");
})
