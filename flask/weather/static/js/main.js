// I didn't include images because the API site seemed mad about image use.
// Also, the display is terrible, but I spent a lot of time getting the AJAX
// function to work, so I'm turning it in as is. I'm sorry about the condition
// of the interface. -Richard Morley
$(document).ready(function(){
    console.log("We're in folks. Javascript is running.");
    console.log("Weather App");
    
    $("form").submit(function(){
        var loc = $('#location').val();
        $.get("http://api.openweathermap.org/data/2.5/weather?q=" + loc + "&units=imperial&APPID=d763e62035fbff16b2f7f7240807faa8", function(data){
            //console.log(data);
            $('#weather').append("<p>" + data.name + "</p>");
            $('#weather').append("<p>" + data.main.temp + " Degrees F</p>");
        });
        return false;
    });
});
