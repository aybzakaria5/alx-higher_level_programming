$.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    method: "GET",
    dataType: "json",
    success: (data) => {
        $("DIV#hello").text(data.hello)
    }
});