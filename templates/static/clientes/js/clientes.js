function add_carro() {
    const container = document.getElementById("form-carro");

    if (container) {
        // Obtendo o ano atual dinamicamente
        const anoAtual = new Date().getFullYear();

        // Gerando opções de anos de 1950 até o ano atual
        let opcoesAnos = "";
        for (let ano = 1950; ano <= anoAtual; ano++) {
            opcoesAnos += `<option value="${ano}">${ano}</option>`;
        }

        // Adicionando o HTML com o seletor de anos
        const html = `
            <br>
            <div class='row' style='width: 35rem; margin-left: 1px'>
                <div style='width: 18rem; margin-left: 0px'>
                    <input type='text' placeholder='Carro' class='form-control' name='carro'>
                </div>
                <div style='width: 12rem; margin-left: 1rem'>
                    <input type='text' placeholder='Placa' class='form-control' name='placa'>
                </div>
            </div>
            <div style='width: 6rem; margin-left: 32rem; margin-top: -38px'>
                <select class='form-control' name='ano'>
                    <option value="" disabled selected>Ano</option>
                    ${opcoesAnos}
                </select>
            </div>
        `;

        container.innerHTML += html;
    } else {
        console.error("Elemento com id 'form-carro' não encontrado.");
    }
}

function exibir_form(tipo) {
    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att_cliente')

    if (tipo == 1) {
        att_cliente.style.display= "none";
        add_cliente.style.display= "block";
    }else if (tipo == 2){
        att_cliente.style.display= "block";
        add_cliente.style.display= "none";}
    }

function dados_cliente() {
    cliente = document.getElementById('cliente-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value

    id_cliente=cliente.value
    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualiza_cliente/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data
    }).then(function (result) {
        return result.json()
    }).then(function (data) {

    })
}