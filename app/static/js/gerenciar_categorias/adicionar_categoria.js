$(document).ready(function () {
    if ($("#menu-adicionar-categoria").children().length == 0) {
        $("#todas-categorias").remove();
    }

    $("#menu-adicionar-categoria span button").each(function() {
        $(this).click($(this).attr("id"), adicionar_categoria);
    });
});

function adicionar_categoria(opcoes) {
    let input_categorias_selecionadas = $("form input[name = 'categorias_selecionadas']");

    let input_categoria = $("#menu-adicionar-categoria span #" + opcoes.data).parent().children("input");

    input_categorias_selecionadas.val(
        input_categorias_selecionadas.val() +
        input_categoria.attr("name") + "_" +
        input_categoria.val() + ";"
    );

    $("#menu-adicionar-categoria span #"  + opcoes.data).parent().remove();

    if ($("#menu-adicionar-categoria").children().length == 0) {
        $("#todas-categorias").remove();
    }

    if (input_categorias_selecionadas.val() != "") {
        let categoria = input_categorias_selecionadas.val().split(";");

        if ($("#categorias-selecionadas").length == 0) {
            let h4 = $("<h4 id='categorias-selecionadas' class='text-center'>Categorias selecionadas</h4>");
            let div = $("<div id='menu-categorias-selecionadas' class='nav justify-content-center espaco-interno-10 espaco-abaixo-10'></div>");

            $(h4).insertBefore($("#todas-categorias"));
            $(div).insertAfter($("#categorias-selecionadas"));
        }

        if (categoria.length != 0) {
            $("#menu-categorias-selecionadas").children().remove()

            categoria.forEach(element => {
                if (element != "") {
                    let item = element.split("_");

                    let span = $("<span class='badge-pill bg-warning espaco-interno-10 espaco-externo-horizontal-10'><span>");
                    let button = $("<button type='button' name='remover' class='badge badge-light bg-light'>X</button>");
                    let input = $("<input type='hidden'>")

                    input.attr("name", item[0]);
                    input.attr("value", item[1]);

                    span.attr("id", "span_" + item[1]);
                    button.attr("id", "botao_" + item[1]);

                    button.click(item[1], remover_categoria);

                    span.text(item[0] + " ");

                    $(span).append(button);
                    $(span).append(input);

                    $("#menu-categorias-selecionadas").append(span);
                }
            });
        }
    }
}