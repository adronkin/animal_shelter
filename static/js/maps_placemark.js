// отображение меток на карте по координатам из БД
// метки подгружаются из json - заменить на БД
ymaps.ready(init);

function init() {
    // создание карты
    var myMap = new ymaps.Map("map", {
            center: [55.76, 37.64],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        }),

        // основа метки
        objectManager = new ymaps.ObjectManager({
            // Чтобы метки начали кластеризоваться, выставляем опцию.
            clusterize: true,
            // ObjectManager принимает те же опции, что и кластеризатор.
            gridSize: 32,
            clusterDisableClickZoom: true,

        });

    myMap.geoObjects
        .add(objectManager);


    $.ajax({
        // В файле data.json заданы геометрия, опции и данные меток .
        url: "/static/js/json/maps_data.json"
    }).done(function (data) {
        objectManager.add(data);
    });
}

