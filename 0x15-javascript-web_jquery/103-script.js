$("document").ready(() => {
    $("INPUT#btn_translate").click(translateHello);

    $("INPUT#language_code").focus(() => {
        $("INPUT#language_code").on("keydown", function (event) {
            if (event.which === 13) {
                translateHello();
            }
        });
    })
});

function translateHello() {
    var countryCode = $("INPUT#language_code");
    $.ajax({
        url: "https://hellosalut.stefanbohacek.dev/?lang=" + countryCode.val(),
        method: "GET",
        dataType: "json",
        success: (data) =>  {
            $("DIV#hello").html(data.hello);
        }
    });
}