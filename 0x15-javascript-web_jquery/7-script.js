$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    datatype: 'json',
    success: (data) => {
        $('DIV#character').text(data.name);
        // $(br).addClass('height');
        // $('.height').text(data.height);
        // this two lines above just to test if the height is being printed
        console.log(data.height);
    }
});