
(function () {

    var inter = {};

    var gebi = function(id) { return document.getElementById(id); };
    var jebi = function(id) { return $("#" + id) };

    var INPUT_FILTERS = "input_filters";

    inter.fullUpdate = function() {
        //if (!this.loaded()) { return };

        var f = readFilters(),
            p = parseFilters(f);
        var results = [];
        inter.DATA.forEach(function(item) {
            results.push(item);
        });
        this.renderResults(results);
    };

    inter.renderResults = function(results) {
        console.log(results.length, results)
    };


    inter.filterResults = function() {
        results = JSON.parse(JSON.stringify(inter.DATA));
    };

    var readFilters = function() {
        var f = jebi( INPUT_FILTERS )
                .val().trim().toLowerCase().split(" ");
        return f.filter(function(item) { return item != "" });
    }

    var parseFilters = function(filters) {
        console.log(filters)
        return filters
    }

    var genPathsAndAliases = function(callback) {

    }

    var loadData = function(cb) {
        console.log("loading data..")
        $.getJSON("data/data.json", function(data) {
            inter.DATA = data;
            console.log("loaded data!");
            cb(null);
        });
    }

    var loadModel = function(cb) {
        console.log("loading model..")
        $.getJSON("data/model.json", function(model) {
            inter.MODEL = model;
            console.log("loaded model!");
            cb(null);
        });
    }

    var genPathsAndAliases = function(cb) {
        console.log("gen");
        cb();
    }

    var bindControls = function(cb) {

        jebi( INPUT_FILTERS ).on("input", inter.fullUpdate);

        cb(null);
    }

    inter.init = function() {

        var t = this;

        async.series([
            function(scb) {
                async.parallel(
                    [ loadData, loadModel ],
                    function(err, results) { scb(err); }
                );
            },
            genPathsAndAliases,
            bindControls
        ]);

    }

    this.inter = inter;

}());
