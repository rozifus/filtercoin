
(function () {

    var inter = {};

    var gebi = function(id) { return document.getElementById(id); };
    var jebi = function(id) { return $("#" + id) };

    var INPUT_FILTERS = "input_filters";
    var FILTER_LIST = "filter_list";

    inter.FILTERABLE = {};
    inter.NODE = {};
    inter.ALIAS  = {};
    inter.TEMPLATES = {};

    inter.fullUpdate = function() {
        //if (!this.loaded()) { return };

        var f      = readFilters(),
            p      = parseFilters(f),
            fables = getNodes(p);
            data   = inter.DATA,
            res    = []
            fcount = 0;
        console.log("parsed", p)
        console.log("fables", fables)
        fables.forEach(function(fable) {
            res = runFilter(data, fable, fcount)
            data = res;
            fcount += 1
        });
        if (fcount == 0) {
            resetMatches(data);
        };
        console.log(data)
        //renderResults(data);
    };

    var runFilter = function(data, fable, fcount) {
        console.log("dpf", data, fable, fcount)
        fdata = []
        data.forEach(function(d) {
            console.log("d", d)
            var tags = d.tags
            for (var f = path.length - 1; p >= 0; p-- ) {
                for (var t = 0; t < tags.length; t++ ) {
                    if (tags[t] == path[p]) {
                        if (fcount > 0) {
                            d.match = d.match * ((p+1)/path.length)
                        } else {
                            d.match = ((p+1)/path.length)
                        };
                        fdata.push(d)
                        return
                    }
                }
            }
        });
        console.log(fdata)
        return fdata;
    };

    var genFilterTree = function() {
        var fl = Handlebars.templates['filterlist'](inter.MODEL)
        jebi( FILTER_LIST ).html( fl );
    }

    var __OLD__runFilterPath = function(data, path, fcount) {
        fdata = []
        data.forEach(function(d) {
            console.log("d", d)
            var tags = d.tags
            for (var p = path.length - 1; p >= 0; p-- ) {
                for (var t = 0; t < tags.length; t++ ) {
                    if (tags[t] == path[p]) {
                        if (fcount > 0) {
                            d.match = d.match * ((p+1)/path.length)
                        } else {
                            d.match = ((p+1)/path.length)
                        };
                        fdata.push(d)
                        return
                    }
                }
            }
        });
        console.log(data)
        return fdata;
    };

    var resetMatches = function(data) {
        data.forEach(function(d) {
            d.match = 1;
        });
    };

    var renderResults = function(results) {
        console.log(results.length, results)
    };


    var filterResults = function() {
        //results = JSON.parse(JSON.stringify(inter.DATA));
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
        buildNodesAndAliases(inter.MODEL);
        console.log(inter.NODE, inter.ALIAS)
        cb(null);
    };

    var getNodes = function(aliases) {
        // simplify to only have aliases?
        var nodes = []
        aliases.forEach(function(alias) {
            var f = inter.ALIAS[alias];
            if (f) {
                nodes.push(inter.NODE[f]);
            }
        });
        return nodes
    };

    var buildNodesAndAliases = function(node) {
        // simplify to only have aliases?
        inter.ALIAS[node.id] = node.id
        for (var iA = 0; iA < node.alias.length; iA++) {
            inter.ALIAS[node.alias[iA]] = node.id
        }
        inter.NODE[node.id] = node
        if (node.sub) {
            for (var iS = 0; iS < node.sub.length; iS++) {
                buildNodesAndAliases(node.sub[iS])
            }
        };

    };

    var loadTemplates = function(node, path) {
        // not needed :3
        [
            "filterlist",
            "filterlistpartial"
        ].forEach(function(tmpl) {
            inter.TMPL[tmpl] = Handlebars.templates[tmpl + ".tmpl"]
        });
    };

    var buildFilterableOld = function(node, path) {
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
            genFilterTree,
            bindControls
        ]);

    }

    this.inter = inter;

}());
