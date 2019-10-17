// при добавление адреса автоматически записывать его координаты в БД
// в разработке

ymaps.ready(init);

var myMap;

function init() {
    var cord = $('#coords').text() // адрес
    myMap = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 7
    });
    ymaps.geocode(cord, {results: 1}).then(function (res) {
            // Выбираем первый результат геокодирования
            var firstGeoObject = res.geoObjects.get(0);
            var cords = firstGeoObject.geometry.getCoordinates();
            console.log('dfd', cords)
        });
};