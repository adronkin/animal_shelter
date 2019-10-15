ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
            center: [55.76, 37.64],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        }),

        // Создаем геообъект с типом геометрии "Точка".
        myGeoObject = new ymaps.GeoObject({
            type: "Feature",
            id: 0,
            // Описание геометрии.
            geometry: {
                type: "Point",
                coordinates: [55.8, 37.8]
            },
            // Свойства.
            properties: {
                // Контент метки.
                iconContent: 'Я тащусь',
                hintContent: 'Ну давай уже тащи'
            }
        }, {
            // Опции.
            // Иконка метки будет растягиваться под размер ее содержимого.
            preset: 'islands#blackStretchyIcon',
            // Метку нельзя перемещать.
            draggable: false
        }),

        objectManager = new ymaps.ObjectManager({
            // Чтобы метки начали кластеризоваться, выставляем опцию.
            clusterize: true,
            // ObjectManager принимает те же опции, что и кластеризатор.
            gridSize: 32,
            clusterDisableClickZoom: true
        })
//    ,
//        myPieChart = new ymaps.Placemark([
//            55.847, 37.6
//        ], {
//            // Данные для построения диаграммы.
//            data: [
//                {weight: 8, color: '#0E4779'},
//                {weight: 6, color: '#1E98FF'},
//                {weight: 4, color: '#82CDFF'}
//            ],
//            iconCaption: "Диаграмма"
//        }, {
//            // Зададим произвольный макет метки.
//            iconLayout: 'default#pieChart',
//            // Радиус диаграммы в пикселях.
//            iconPieChartRadius: 30,
//            // Радиус центральной части макета.
//            iconPieChartCoreRadius: 10,
//            // Стиль заливки центральной части.
//            iconPieChartCoreFillStyle: '#ffffff',
//            // Cтиль линий-разделителей секторов и внешней обводки диаграммы.
//            iconPieChartStrokeStyle: '#ffffff',
//            // Ширина линий-разделителей секторов и внешней обводки диаграммы.
//            iconPieChartStrokeWidth: 3,
//            // Максимальная ширина подписи метки.
//            iconPieChartCaptionMaxWidth: 200
//        })
    ;

    myMap.geoObjects
        .add(myGeoObject)
        //        .add(myPieChart)
        .add(new ymaps.Placemark([55.687086, 37.529789], {
            balloonContent: 'цвет <strong>влюбленной жабы</strong>'
        }, {
            preset: 'islands#circleIcon',
            iconColor: '#843caa'
        }));

    myMap.geoObjects
        .add(objectManager);


    $.ajax({
        // В файле data.json заданы геометрия, опции и данные меток .
        url: "/static/js/json/data.json"
    }).done(function (data) {
        objectManager.add(data);
    });
}