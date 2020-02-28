function remover_categoria(indice) {
    let span_categorias_selecionadas = $("#span_" + indice.data);

    span_categorias_selecionadas.remove();

    if ($("#menu-categorias-selecionadas").children().length == 0) {
        $("#menu-categorias-selecionadas").remove();
        $("#categorias-selecionadas").remove();
    }

    console.log(span_categorias_selecionadas);
    // let input_categorias_selecionadas = $("#form-adicionar-produto form input[name = 'categorias_selecionadas']");
}