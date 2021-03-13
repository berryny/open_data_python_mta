document.querySelector(".year").innerHTML = new Date().getFullYear();

// Enable Search button once boro is selected from dropdown
let boro_select_map = document.getElementById('boro_station');
let boro_station_map = ''

if (boro_select_map) {
    boro_select_map.onchange = function (params) {
        boro_station_map = boro_select_map.value
        document.querySelector('.btn_filter_map').removeAttribute('disabled')
    }
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

function clearMapMarkers() {
    subwaymap.eachLayer(function (layer) {
        if (layer instanceof L.Marker) {
            // remove layer
            subwaymap.removeLayer(layer);
        }
    })
}

$('button.btn_filter_map').on('click', function (e) {
    url = ''
    let equip_select_filter = document.getElementById('equip_filter_type');
    equip_filter_map = equip_select_filter.value

    if (boro_station_map != '' && equip_filter_map != '') {
        url = '/stations_with_equip/' + boro_station_map + '/' + equip_filter_map + '/'
    } else {
        // default value
        url = '/stations_with_equip/MN/All/'
    }
    fetch(url)
        .then(function (response) {
            response.json().then(function (dataFilter) {
                clearMapMarkers();

                for (const property in dataFilter) {
                    dataFilter[property].forEach(element => {
                    //    console.log('ele',element);
                        L.marker([element['Coordinates'][0], element['Coordinates'][1]]).addTo(subwaymap)
                            .on('click', onMarkerMapClick)
                            .bindPopup("<b>" + element['Station']['station'] + "</b><br />Train: " + element['Station']['trainno']).openPopup();
                   });
                }
                var popup = L.popup();

                function onMarkerMapClick(e) {
                    var curPos = e.latlng;
                    curPosArr = [curPos.lat, curPos.lng]
                    // console.log(curPos.lat, curPos.lng);
                    for (const property in dataFilter) {
                        dataFilter[property].forEach(element => {
                            console.log(element['Coordinates'], curPosArr);
                            for (let i = 0; i < curPosArr.length; i++) {
                                if (curPosArr[i] == element['Coordinates'][i]) {
                                    console.log("yes",element);
                                 }
                            }
                        });
                    }
                }
                function onMapClick(e) {
                    popup
                        .setLatLng(e.latlng)
                        .setContent("You clicked the map at " + e.latlng.toString())
                        .openOn(subwaymap);
                }

                subwaymap.on('click', onMapClick);
            })
        }).catch(function (error) {
            console.log("Err: Station Map Filter Data");
            console.log(error);
        });
});          
$(document).ready(function () {
 
});