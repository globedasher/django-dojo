$(document).ready(function(){
    console.log('jQuery running!');

    
    $('form').submit(function(){
        $.post('/quotes/create', $(this).serialize(), function(res){
            $('#quotes').html(res);
        });
        //console.log('AJAX post!');
        return false;
    });

    $('#get_button').click(function(){
        $.get("/quotes/index_json", function(res){
            var res_len = res.quotes.length;
            console.log(res_len);
            console.log(res);
            var htmlStr = "";
            for(var i=0; i < res_len; i++){
                htmlStr += "<div class='quote'>";
                htmlStr += "<h2>" + res.quotes[i].author + "</h2>";
                htmlStr += "<p>" + res.quotes[i].quote + "</p>";
                htmlStr += "</div>";
            } 
            console.log(htmlStr);
            $('#quotes').append(htmlStr);
        }, "json");
        return false;
    });
});
