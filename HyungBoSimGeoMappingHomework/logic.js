


var api_key = "pk.eyJ1IjoiZGFubnlvc2ltIiwiYSI6ImNqb2plaGNuMzA0YnIzdm1vd3EzcnZjdmoifQ.6TYl3HsLXhUzxU_zPRvWbA";

var Grey = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
  maxZoom: 100,
  id: "mapbox.streets",
  accessToken: api_key
});
var map = L.map("TheMap", {
  center: [
    0, 0
  ],
  zoom: 1
});
Grey.addTo(map);
d3.json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson", function(data) {
  function Visual(feature) {
    return {
      fillOpacity: 1,
      fillColor: COLOR(feature.properties.mag),
      color: "#000000",
      radius: CircleSize(feature.properties.mag),
      weight: 1
    };
  }
  function CircleSize(EarthquakeMagnitude) {
    return EarthquakeMagnitude * 4;
  }
  L.geoJson(data, {
  
  pointToLayer: function(feature, latlng) {
    return L.circleMarker(latlng); },
    style: Visual,
    onEachFeature: function(feature, layer) {
      layer.bindPopup("EarthquakeMagnitude: " + feature.properties.mag + "<br>Location: " + feature.properties.place);
    }}).addTo(map);
  var Legend = L.control({
    position: "bottomright"
  });
  Legend.onAdd = function() {
    var levels = L.DomUtil.create("levels", "info legend");
    var LegendMagnitudes = [0, 1, 2, 3, 4, 5];
    var ColorScale = [
      "#AD33F1",
      "#BD5CF4",
      "#CA7DF6",
      "#D597F8",
      "#DDACF9",
      "#E4BDFA"
    ];
    for (var i = 0; i < LegendMagnitudes.length; i++) {
      levels.innerHTML +=
        "<i style='background: " + ColorScale[i] + "'></i> " +
        LegendMagnitudes[i] + (LegendMagnitudes[i + 1] ? "&ndash;" + LegendMagnitudes[i + 1] + "<br>" : "+");
    }
    return levels;
  };

  Legend.addTo(map);
});
  function COLOR(EarthquakeMagnitude) {
    switch (true) {
    case EarthquakeMagnitude > 5:
      return "#E4BDFA";
    case EarthquakeMagnitude > 4:
      return "#DDACF9";
    case EarthquakeMagnitude > 3:
      return "#D597F8";
    case EarthquakeMagnitude > 2:
      return "#CA7DF6";
    case EarthquakeMagnitude > 1:
      return "#BD5CF4";
    default:
      return "#AD33F1";}}

  function CircleSize(EarthquakeMagnitude) {return EarthquakeMagnitude * 4;
  }
  L.geoJson(data, {
    pointToLayer: function(feature, latlng) {
      return L.circleMarker(latlng);
    },style: Visual,
    onEachFeature: function(feature, layer) {
      layer.bindPopup("EarthquakeMagnitude: " + feature.properties.mag + "<br>Location: " + feature.properties.place);
    }}).addTo(map);
  var Legend = L.control();