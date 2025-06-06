# Python_hacking
let logEnable = false;

function logArguments(...args){
    if(logEnable){
        console.log("log", ...args);
    }
}

async function getHeadersANdBody(request) {
    
    function getHeaders(request){
        const headers ={};
        
        // Correção: forEach para Map (request.headers) usa (value, key)
        request.headers.forEach((value, key) => { 
            headers[key] = value;
        });

        logArguments('headers:', headers);
        return headers;
    }   

    async function getBody(request) {
        const bodyArray = await request.arrayBuffer();
        const body = new TextDecoder('utf-8').decode(bodyArray);
        logArguments('Body:', body);

        // --- Início da Identificação com Regex ---

        // Regex para CPF: identifica formatos XXX.XXX.XXX-XX ou XXXXXXXXXXX
        const cpfRegex = /(\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})/g;
        const cpfsEncontrados = body.match(cpfRegex);
        if (cpfsEncontrados) {
            logArguments('CPFs encontrados:', cpfsEncontrados);
        }

        // Regex para E-mail: identifica padrões comuns de endereços de e-mail
        const emailRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g;
        const emailsEncontrados = body.match(emailRegex);
        if (emailsEncontrados) {
            logArguments('E-mails encontrados:', emailsEncontrados);
        }

        // Regex para Cartão de Crédito: tenta identificar padrões de números de cartão (Visa, Mastercard, Amex, Discover)
        // ATENÇÃO: Esta Regex é para detecção básica. Para validação de segurança, use bibliotecas específicas.
        const creditCardRegex = /(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12})/g;
        const cartoesEncontrados = body.match(creditCardRegex);
        if (cartoesEncontrados) {
            logArguments('Dados de Cartão encontrados:', cartoesEncontrados);
        }

        // --- Fim da Identificação com Regex ---

        return body;
    }

    const headers = getHeaders(request);
    const body = await getBody(request);

    return {
        headers,
        body
    }
}

addEventListener('fetch', (event) => {
    event.passThroughOnException();
    try {
        
        logArguments('Iniciando Worker CloudFlare', logEnable);

        event.respondWith(async function() {
            const request = event.request;
            logArguments('Nova Requisição', request.url);
            
            try {
                const result = await getHeadersANdBody(request);
                logArguments('Dados da requisição processados');
            } catch (error) {
                logArguments('Erro ao processar requisição', error);
            }
        });
    } catch (error) {
        logArguments('Erro no Workers', error);
    }
});
