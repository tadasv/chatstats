/*
 * -Get data from MongoDB
 * -Turn into flot-friendly data
 * -plot that shit
 *
 */
/*
var testData = {
    "speakersnames" : ["af", "hf", "ak", "ll"],
    "speakerstats" : [
    { "name": "af", "stats" : {"vb" : 14, "total": 139, "rt": 71} },
    { "name": "af", "stats" : {"hf" : "vb" : 12, "total": 535, "rt": 21} },
    { "name": "af", "stats" : {"ak" : "vb" : 31, "total": 159, "rt": 14} },
    { "name": "af", "stats" : {"ll" : "vb" : 26, "total": 333, "rt": 4}}
    ]
};
*/

var testData = {
    "dataName" : "frequency/rawtotal/verbose",
    "data" : { "af" : 23, "hw" : 44, "ta" : 32}
};

$(function () {
    /*
     * Settings
     */
    var updateInterval = 4000; //4 second updates

    //options for flot
    var options = {
        series : {shadowsize :0},
        yaxis : { min:0, max: 100 },
        xaxis: { show: false },
    };

    /*
     * End Settings
     */

    function getData(){
        //JSON retrieval
        //dataToPlot = //interpretation of Json
        //will want to iterate over api calls and construct a large list of all 3

        //temp test
        var flotData = [];
        console.log("getData");
        console.log(testData);
        console.log(testData.dataName);
        console.log(testData.data);
        for( var key in testData.data ){
            var name = key;
            var value = testData.data[key];
            console.log(name, value);
            flotData.push([name, value])
        }
        console.log(flotData);
        return flotData;
    }

    function update(){
        plot.setData( [getData()] );
        plot.setupGrid();
        plot.draw()

        setTimeout(update, updateInterval);
    }

    //update();
    getData();
    console.log("asdf");
    var plot = $.plot($("#placeholder", [getData() ], options));
    update();

});




