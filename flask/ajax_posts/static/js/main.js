$(document).ready(function(){
  console.log('jQuery running!');
  // The folling is AJAX for retrieval.
  $.get("/note/html_index", function(res){
    //console.log(res);
    $('#notes').html(res);
  });

  $('#new').submit(function(){
    $.post('/note/create', $(this).serialize(), function(res){
      $('#notes').html(res);
    });
    return false;
  });
  
  $(document).on( 'submit', '#delete', function(){
    //console.log('delete!');
    $.post('/note/delete', $(this).serialize(), function(res){
      $('#notes').html(res);
    });
    return false;
  });

  $(document).on('submit', '#update', function(){
    $.post('/note/update', $(this).serialize(), function(res){
      $('#notes').html(res);
    });
    return false;
  });

});
