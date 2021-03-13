document.querySelector(".year").innerHTML = new Date().getFullYear();

// Enable Search button once boro is selected from dropdown
let boro_select_map = document.getElementById('boro_station');
let equip_select_filter = document.getElementById('equip_filter_type');
let boro_station_map = ''
let equip_filter_map = ''

if (boro_select_map) {
    boro_select_map.onchange = function (params) {
        boro_station_map = boro_select_map.value
        document.querySelector('.btn_filter_map').removeAttribute('disabled')
    }
    equip_filter_map = equip_select_filter.value

}

/*
 Leaflet Map
    create a map of the "center" of New York City 
    add a tile layer to add to our map
*/
var subwaymap = L.map('mapid', {
    'center': [40.712772, -74.006058],
    'zoom': 13,
    'layers': [
        L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
            maxZoom: 18,
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
                'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            id: 'mapbox/streets-v11',
            tileSize: 512,
            zoomOffset: -1
        })
    ]
});

$('button.btn_filter_map').on('click', function (e) {
    url = ''
    if (boro_station_map != '' && equip_filter_map != '') {
        url = '/stations_with_equip/' + boro_station_map + '/' + equip_filter_map + '/'
    } else {
        // default value
        url = '/stations_with_equip/MN/All/'
    }
    fetch(url)
        .then(function (response) {
            response.json().then(function (dataFilter) {
                console.log('dataFilter',dataFilter);
            }).catch(function (error) {
                console.log(error);
                console.log("Err: Station Map Filter Data");
            });
    })      
});          
$(document).ready(function () {
 
});