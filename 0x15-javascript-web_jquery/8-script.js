$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: (data) => {
        var list = ""
        data.results.forEach(element => {
            list=list.concat("<li>", element.title , "</li>") 
        });
        $("UL#list_movies").html(list)

    }
});
