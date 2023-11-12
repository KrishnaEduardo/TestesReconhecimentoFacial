function fazerChamada() {
    var NumeroTelefone = document.getElementById('telefone').value;
    var MensagemTexto = document.getElementById('mensagem').value;
    
    var data = new Date(),
        dia  = data.getDate(),
        mes  = data.getMonth()+1, 
        ano  = data.getFullYear();
        hora = data.getHours()
        minutos = data.getMinutes()
    var d = dia+"/"+mes+"/"+ano+" "+hora+":"+minutos;

    var apiUrl = 'https://api.callmebot.com/whatsapp.php?phone=' + NumeroTelefone + '&text=' + MensagemTexto + '%20' + d + '&apikey=2212690#' ;

    var script = document.createElement('script');
    script.src = apiUrl;
    document.head.appendChild(script);
    document.head.removeChild(script);

    alert('Enviado com Sucesso')
}
