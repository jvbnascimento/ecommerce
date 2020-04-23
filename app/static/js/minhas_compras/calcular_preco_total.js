$(document).ready(function () {
    let compras = $("#lista_compras").children("div");
    
    compras.each(function() {
        let preco_total = $(this).children().children().children().children("h6[name='preco_total']");
        let preco_unitario = $(this).children().children().children().children("h6[name='preco_unitario']");
        let quantidade_item = $(this).children().children().children().children("h6[name='quantidade_item']");

        preco_total.each(function(index) {
            $(this).text("R$ " + 
                (
                    parseInt($(quantidade_item[index]).text()) *
                    parseFloat($(preco_unitario[index]).text().split("R$ ")[1].replace(",", "."))
                ).toFixed(2).replace(".", ",")
            );
        });
    });
});