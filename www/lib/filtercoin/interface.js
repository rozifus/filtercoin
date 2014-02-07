
var Interface = function() {};
var gebi = function(id) { return document.getElementById(id); };
var jebi = function(id) { return $("#" + id) };

Interface.EMPTY_IMG = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7";
Interface.EMPTY_TEXT = "";

Interface.DATA = null;
Interface.LOADING = 1;

POST_LIST = "messages";

INPUT_FILTERS = "input_filters";

Interface.prototype.fullUpdate = function() {
    if (!this.loaded()) { return };

    var f = this.readFilters(),
        p = this.parseFilters(f);
    var results = [];
    Interface.DATA.forEach(function(item) {
        results.push(item);
    });
    this.renderResults(results);
};

Interface.prototype.renderResults = function(results) {
    console.log(results.length, results)
};


Interface.filterResults = function() {
    results = JSON.parse(JSON.stringify(Interface.DATA));
};

Interface.prototype.readFilters = function() {
    var f = jebi( INPUT_FILTERS )
            .val().trim().toLowerCase().split(" ");
    return f.filter(function(item) { return item != "" });
}

Interface.prototype.parseFilters = function(filters) {
    console.log(filters)
    return filters
}

Interface.prototype.loadData = function() {
    console.log("loading data..")
    $.getJSON("data/data.json", function(data) {
        Interface.DATA = data;
        console.log("loaded data!")
        callback()
    });
}

Interface.prototype.loadModel = function() {
    console.log("loading model..")
    $.getJSON("data/model.json", function(model) {
        Interface.MODEL = model;
        console.log("loaded model!")
    });
}

Interface.prototype.getPathsAndAliases



Interface.renderCoin = function(json) {

}

Interface.prototype.genPathsAndAliases = function() {

}


Interface.prototype.init = function() {
    var t = this;

    t.loadData(t.loadModel())
    t.loadData()
    t.loadModel()

    t.genPathsAndAliases()

    jebi( INPUT_FILTERS ).on("input", $.proxy(this.update, this));
}

