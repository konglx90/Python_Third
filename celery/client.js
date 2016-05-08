// redis 链接
var redis   = require('redis');
var client  = redis.createClient('6379', '127.0.0.1');

// redis 链接错误
client.on("error", function(error) {
    console.log(error);
});


client.select('15', function(error){
    if(error) {
        console.log(error);
    } else {
        // set
        client.set('str_key_0', '0', function(error, res) {
            if(error) {
                console.log(error);
            } else {
                console.log(res);
            }

            // 关闭链接
            client.end();
        });
    }
});
