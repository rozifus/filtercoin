
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
        renderResults(results);
    };

    var renderResults = function(results) {
        console.log(results.length, results)
    };


    var filterResults = function() {
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
        inter.FILTERABLE = {};
        inter.ALIAS  = {};

        buildFilterable(inter.MODEL, []);
        console.log(inter.FILTERABLE, inter.ALIAS)
        cb(null);
    };

    var buildFilterable = function(node, path) {
        path.push(node.id)
        inter.ALIAS[node.id] = node.id
        for (var iA = 0; iA < node.alias.length; iA++) {
            inter.ALIAS[node.alias[iA]] = node.id
        }
        filterable = {
            name: node.name,
            path: path
        }
        inter.FILTERABLE[node.id] = filterable
        if (node.sub) {
            for (var iS = 0; iS < node.sub.length; iS++) {
                buildFilterable(node.sub[iS], path.slice() )
            }
        };

    };

    var bindControls = function(cb) {

        jebi( INPUT_FILTERS ).on("input", inter.fullUpdate);

        cb(null);
    }

    inter.init = function() {

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
