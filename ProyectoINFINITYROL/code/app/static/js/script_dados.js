function lanzarDado() {
    let dado = document.querySelector('input[name="options"]:checked').id;
    let resultado = document.getElementById('resultado');
    let numeros = [];
    
    switch(dado) {
        case 'dado6':
            numeros = [1, 2, 3, 4, 5, 6];
            break;
        case 'dado10':
            numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
            break;
        case 'dado12':
            numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
            break;
        case 'dado24':
            numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24];
            break;
    }

    console.log('Numeros posibles: ', numeros);

    let duration = 5000; // Duración total en milisegundos (5 segundos)
    let intervalTime = 100; // Tiempo entre iteraciones en milisegundos
    let iterations = duration / intervalTime; // Número de iteraciones para completar los 5 segundos

    let i = 0;
    let interval = setInterval(function() {
        resultado.textContent = numeros[Math.floor(Math.random() * numeros.length)];
        i++;
        console.log('Iteración ' + i + ': ' + resultado.textContent);
        if (i >= iterations) {
            clearInterval(interval);
            // Mostrar el resultado final aleatorio
            resultado.textContent = numeros[Math.floor(Math.random() * numeros.length)];
            console.log('Resultado final: ' + resultado.textContent);
        }
    }, intervalTime);
}