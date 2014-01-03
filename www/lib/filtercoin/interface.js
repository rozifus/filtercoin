
var Interface = function() {};
var gebi = function(id) { return document.getElementById(id); };
var jebi = function(id) { return $("#" + id) };

Interface.EMPTY_IMG = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7";
Interface.EMPTY_TEXT = "";

Interface.DATA = null;

POST_LIST = "messages";

SEND_FORM = "send-form";
SEND_IMG_PREVIEW = "send-img-preview";
SEND_TEXT_INPUT = "send-message";
SEND_IMG_INPUT = "send-img-input";
SEND_BUTTON = "send-button"

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
        console.log(data)
    });
}

Interface.renderCoin = function(json) {

}

Interface.prototype.init = function() {
    var t = this;

    Interface.DATA = t.loadData()
    jebi( SEND_FORM ).submit(function() {
        t.sendMessage()
        return false;
    })

    jebi( SEND_BUTTON ).click(this.SendMessage);
}

