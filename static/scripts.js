$(function() {
    $( "#check-button" ).click(function() {

        $( "#check-result" ).html("<img src='static/ajax-loader.gif'><h5>Training language model...(This might take a while online...)</h5>");
        var num_words = $( "#num_words" ).val();
        var word = $( "#word" ).val();
        $.get( "/generate?num_words=" + num_words + "&word=" + word, function( data ) {
            $( "#check-result" ).html( "<h3>" + data + "</h3>" );
        }).fail( function( error ) {
            console.log( error );
        });
    });
});
