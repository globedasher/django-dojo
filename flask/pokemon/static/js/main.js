// I didn't include images because the API site seemed mad about image use.
// Also, the display is terrible, but I spent a lot of time getting the AJAX
// function to work, so I'm turning it in as is. I'm sorry about the condition
// of the interface. -Richard Morley
$(document).ready(function(){
    console.log("We're in folks. Javascript is running.");
    // When page is loaded, get data from pokeapi.co about the pokemon up to
    // index 151
    for(var index=1; index<=151; index++){
        $("#pokemon").append("<h4 id=" + index + "> </h4>");
        $.get("http://pokeapi.co/api/v2/pokemon/" + index, function(pokemon){
            $("#" + pokemon.id).append(pokemon.name);
        }, "json");
    }

    // When the p tags are clicked
    // Place the pokemon name in the pokedex
    $(document).on('click', 'h4', function(){
        console.log('click');
        console.log($(this).attr('id'));
        $('#pokedex').append("<h2>" + $(this).attr('id') + "</h2>"); 
        $.get("http://pokeapi.co/api/v2/pokemon/" + $(this).attr('id'), function(pokemon){
        console.log('get');
        console.log(pokemon.types);
        $('#pokedex').append("<h2>" + pokemon.name + "</h2>"); 
        $('#pokedex').append("<h2>Types:</h2>"); 
        $('#pokedex').append('<ul>');
            for(var type_index=0; type_index<pokemon.types.length; type_index++){
                $('#pokedex').append("<li>" + pokemon.types[type_index].type.name + "</li>"); 
                console.log(pokemon.types[type_index].type.name);
            }
        $('#pokedex').append('</ul>');
        $('#pokedex').append("<h2>Height:</h2>"); 
        $('#pokedex').append("<p>" + pokemon.height + "</p>"); 
        $('#pokedex').append("<h2>Weight:</h2>"); 
        $('#pokedex').append("<p>" + pokemon.weight + "</p>"); 
        }, "json");
    });
});
