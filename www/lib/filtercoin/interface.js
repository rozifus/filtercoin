
var Interface = function() {};
var gebi = function(id) { return document.getElementById(id); };
var jebi = function(id) { return $("#" + id) };

Interface.EMPTY_IMG = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7";
Interface.EMPTY_TEXT = "";

Interface.DATA = null;
Interface.LOADING = 1;

POST_LIST = "messages";

INPUT_FILTERS = "input_filters";

Interface.prototype.displayMessage = function(message) {
    var text_data   = message.text || Interface.EMPTY_TEXT,
        img_data    = message.img || Interface.EMPTY_IMG,
        text_elem   = $("</p>", {text: text_data}),
        img_elem    = $("</img>", {src: img_data}),
        post        = $("</div>").append(img_elem).append(text_elem);

    jebi( POST_LIST ).append("<div class='ui segment'><img src=" + img_data +
                          "></img><p>" + text_data +
                          "</p></div>");
};

Interface.prototype.uploadImgSelected = function() {
    this.previewImg();
};

Interface.prototype.update = function() {
    if (Interface.LOADING) { return };

    var f = this.readFilters(),
        p = this.parseFilters(f);

}

Interface.filterResults = function() {
    results = JSON.parse(JSON.stringify(Interface.data))
}

Interface.prototype.readFilters = function() {
    var f = jebi( INPUT_FILTERS )
            .val().trim().toLowerCase().split(" ");
    return f.filter(function(item) { return item != "" });
}

Interface.prototype.parseFilters = function(filters) {
    console.log(filters)
    return filters
}

Interface.prototype.previewImg = function() {
    var preview     = gebi( SEND_IMG_PREVIEW ),
        input       = gebi( SEND_IMG_INPUT ),
        file        = input && input.files && input.files[0],
        reader      = new FileReader();

    if (file) {
        reader.onloadend = function() {
            preview.src = reader.result;
        };
        reader.readAsDataURL(file);
    } else {
        preview.src = Interface.EMPTY_IMG;
    };
}

Interface.prototype.buildMessage = function(text, img) {

}

Interface.prototype.sendMessage = function() {
    var room      = '/' + $('#send-room').val(),
        text_data = jebi( SEND_TEXT_INPUT ).val() || Interface.EMPTY_TEXT,
        img_input = gebi( SEND_IMG_INPUT ),
        img_file  = img_input && img_input.files && img_input.files[0],
        reader    = new FileReader();

    if (img_file) {
        reader.onloadend = function() {
            chat && chat.sendMessage(room, {text: text_data,
                                            img: reader.result});
        }
        reader.readAsDataURL(img_file);
    } else {
        chat && chat.sendMessage(room, {text: text_data} );
    };
    // clear file upload + textbox
    return false;
}

Interface.prototype.loadData = function() {
    $.getJSON("data/data.json", function(data) {
        Interface.DATA = data;
    });
}

Interface.prototype.loadModel = function() {
    $.getJSON("data/model.json", function(data) {
        Interface.DATA = data;
    });
}



Interface.renderCoin = function(json) {

}

Interface.prototype.init = function() {
    var t = this;

    Interface.DATA  = t.loadData()
    Interface.MODEL = t.loadModel()

    jebi( SEND_BUTTON ).click(t.SendMessage);

    jebi( INPUT_FILTERS ).on("input", $.proxy(this.update, this));
}

