
(function () {

    var inter = {};

    var gebi = function(id) { return document.getElementById(id); };
    var jebi = function(id) { return $("#" + id) };

    var FILTER_LIST     = "filter_list",
        FILTER_MENU     = "filter_menu",
        INPUT_FILTERS   = "input_filters",
        DETECTED_LIST   = "filter_detected",
        RESULT_LIST     = "result_list";

    inter.FILTERABLE = {};
    inter.NODE = {};
    inter.ALIAS  = {};
    inter.TEMPLATES = {};

    inter.fullUpdate = function() {
        //if (!this.loaded()) { return };

        var f      = readFilters(),
            p      = parseFilters(f),
            fables = getNodes(p),
            data   = inter.DATA,
            res    = [],
            det    = [],
            fcount = 0;
        //console.log("parsed", p)
        //console.log("fables", fables)
        fables.forEach(function(fable) {
            if (fable != null) {
                res = runFilter(data, fable, fcount)
                data = res;
                det.push({ name: fable.n,
                           count: data.length,
                           step: det.length
                });
                fcount += 1;
            } else {
                det.push({ name: "???",
                           unknown: true,
                           step: det.length
                });
            }
        });
        data.sort(sortPop);
        //console.log('fcount', fcount);
        if (fcount == 0) {
            resetMatches(data);
            displayResults([]);
        } else {
            displayResults(data);
        }
        displayDetected(det);
    };

    var sortPop = function(a,b) {
        if (b.m != a.m) {
            return b.m - a.m
        }
        return b.p - a.p
    }

    var displayDetected = function(det) {
        var dl = Handlebars.templates['detectlist'](det);
        jebi( DETECTED_LIST).html( dl );
    };

    var runFilter = function(data, fable, fcount) {
        //console.log("dpf", data, fable, fcount)
        fdata = []
        data.forEach(function(d) {
            //console.log("d", d)
            var tags = d.t
            for (var t = 0; t < tags.length; t++ ) {
                if (tags[t] == fable.i) {
                    fdata.push(d)
                    return
                }
            }
        });
        //console.log(fdata)
        return fdata;
    };

    var genFilterTree = function(cb) {
        var fl = Handlebars.templates['filterlist'](inter.MODEL);
        jebi( FILTER_MENU ).html( fl );
        cb(null);
    }

    var displayResults = function(results, conf) {
        var rl = Handlebars.templates['resultlist'](results);
        jebi( RESULT_LIST ).html( rl );
    }

    var displayFilterDetected = function(filters) {
        var fd = Handlebars.templates['filterdetected'](filters)
        jebi( FILTER_DETECTED ).html( fd );
    }

    var __OLD__runFilterPath = function(data, path, fcount) {
        fdata = []
        data.forEach(function(d) {
            //console.log("d", d)
            var tags = d.t
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
        //console.log(data)
        return fdata;
    };

    var resetMatches = function(data) {
        data.forEach(function(d) {
            d.match = 1;
        });
    };

    var renderResults = function(results) {
        //console.log(results.length, results)
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
        //console.log(filters)
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
            } else {
                nodes.push(null);
            };
        });
        return nodes
    };

    var buildNodesAndAliases = function(node) {
        // simplify to only have aliases?
        inter.ALIAS[node.i] = node.i
        for (var iA = 0; iA < node.a.length; iA++) {
            inter.ALIAS[node.a[iA]] = node.i
        }
        inter.NODE[node.i] = node
        if (node.s) {
            for (var iS = 0; iS < node.s.length; iS++) {
                buildNodesAndAliases(node.s[iS])
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
        path.push(node.i)
        inter.ALIAS[node.i] = node.i
        for (var iA = 0; iA < node.a.length; iA++) {
            inter.ALIAS[node.a[iA]] = node.i
        }
        filterable = {
            name: node.n,
            path: path
        }
        inter.FILTERABLE[node.i] = filterable
        if (node.s) {
            for (var iS = 0; iS < node.s.length; iS++) {
                buildFilterable(node.s[iS], path.slice() )
            }
        };

    };

    var bindControls = function(cb) {

        jebi( INPUT_FILTERS ).on("input", inter.fullUpdate);

        $('div.add-filter').click(function(event) {
            if (event.stopPropagation) {
                event.stopPropagation();
            }
            if (event && event.currentTarget) {
                addFilter($(event.currentTarget).attr('data-filter-id'));

                //$('.ui.accordion').first().accordion('close', 0);
                $('.ui.sidebar').sidebar('hide');
                jebi( INPUT_FILTERS ).focus()

                inter.fullUpdate()

            } else {
                console.log(":S!!! No event.currentTarget");
            }
        })

        cb(null);
    };

    var addFilter = function(fid) {

        var infil = jebi( INPUT_FILTERS ),
            cur   = infil.val().trim();

        if (cur != "") {
            infil.val(infil.val() + " ");
        }

        infil.val(infil.val() + fid);

    };

    var initSemanticModules = function(cb) {

        $('.filter.menu .item')
          .tab()
        ;

        $('.ui.sidebar')
          .sidebar('attach events', '#button_addfilter')
        ;

        $('.ui.accordion').first()
          .accordion({
            'selector': {
              title: '.title.subs'
            }
          })
        ;

        cb(null);
    };

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
            initSemanticModules,
            bindControls
        ]);

    }

    this.inter = inter;

}());
