
var Data = function() {
    this.conns = {};
    this.rooms = {};
}

Data.prototype.loadData = function(server, room) {
    var t = this;
    if (!this.conns[server]) {
        this.connectToServer(server);
    };
    var sub = this.conns[server].subscribe(room, function(message) {
        interface && interface.displayMessage(message);
        console.log('got message', message)
    });
    sub.then(function() {
        t.rooms[room] = {room:room, server:server, sub:sub};
        console.log('added room', room, sub);
    });
};

