var Output = data;
var tbody = d3.select("tbody");
function Button() {
  d3.event.preventDefault();
  var date = d3.select("#datetime").property("value");
  let FILTERED = Output;
  if (date) {FILTERED = FILTERED.filter(row => row.datetime === date);}
  TABLE(FILTERED);}
function TABLE(Output) {
  tbody.html("");
  Output.forEach((dataRow) => {
    var row = tbody.append("tr");
    Object.values(dataRow).forEach((val) => {
      var cell = row.append("td");
        cell.text(val);});});}
d3.selectAll("#filter-btn").on("click", Button);
TABLE(Output);
