$(document).ready(function () {
    let compras = $("#lista_compras").children("div");

    compras.each(function() {
        let data_antiga = $(this).find("h5[name='data_compra']").text().split("Data da compra: ")[1].split(" ");

        let data = data_antiga[0].split("-");
        let hora = data_antiga[1].split(":");

        data_aux = data[0];
        data[0] = data[2]
        data[2] = data_aux;

        hora[2] = hora[2].split(".")[0]

        let nova_data = "Data da compra: " + data[0] + "/" + data[1] + "/" + data[2] + " às " + hora[0] + ":" + hora[1] + ":" + hora[2];

        $(this).find("h5[name='data_compra']").text(nova_data);
    });
});