$(document).ready(function() {
    let span_adicionar_categoria = $("#menu-adicionar-categoria span");
    let input_categorias_selecionadas = $("#form-adicionar-produto form input[name = 'categorias_selecionadas']");

    span_adicionar_categoria.each(function(index) {
        $(this).children("button").click(function() {
            input_categorias_selecionadas.val(
                input_categorias_selecionadas.val() +
                span_adicionar_categoria.children("input").eq(index).attr("name") + "_" + 
                span_adicionar_categoria.children("input").eq(index).val() + ";"
            );
            
            $(span_adicionar_categoria).eq(index).remove();

            if (input_categorias_selecionadas.val() != "") {
                let categoria = input_categorias_selecionadas.val().split(";");

                if ($("#categorias-selecionadas").length == 0) {
                    let h4 = $("<h4 id='categorias-selecionadas' class='text-center'>Categorias selecionadas</h4>");
                    let div = $("<div id='menu-categorias-selecionadas' class='nav espaco-interno justify-content-center espaco-abaixo-10'></div>");

                    $(h4).insertBefore($("#todas-categorias"));
                    $(div).insertAfter($("#categorias-selecionadas"));
                }

                if (categoria.length != 0) {
                    $("#menu-categorias-selecionadas").children().remove()

                    categoria.forEach(element => {
                        if (element != "") {
                            let item = element.split("_");

                            let span = $("<span class='badge-pill bg-warning espaco-interno espaco-externo'><span>");
                            let button = $("<button type='button' name='remover' class='badge badge-light bg-light'>X</button>");
                            
                            span.attr("id", "span_" + item[1]);
                            button.click(indice = item[1], remover_categoria);

                            span.text(item[0] + " ");
                            $(span).append(button);

                            $("#menu-categorias-selecionadas").append(span);
                        }
                    });
                }
            }
        });
    });
});