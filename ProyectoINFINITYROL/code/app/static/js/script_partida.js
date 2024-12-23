/*
{% extends 'layout.html' %}
{% block title %}{{ data.titulo }}{% endblock %}
{% block body %}
    <h1>{{ data.titulo }}</h1>
    <p>{{ data.mensaje }}</p>
{% endblock %}

{% block content %}
    <h2>Plataforma de Partida</h2>
    <p>Aquí va la plataforma</p>
    
    <form onsubmit="crearPartida(); return false;">
        <div class="form-group">
            <label for="nombrePartida">Nombre de la Partida:</label>
            <input type="text" class="form-control" id="nombrePartida" name="nombrePartida" required>
        </div>

        <div class="form-group">
            <label>Tipo de Partida:</label>
            <div class="form-check">
                <input class="form-check-input" type="radio" id="publica" name="tipoPartida" value="publica" required>
                <label class="form-check-label" for="publica">Pública</label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" id="privada" name="tipoPartida" value="privada" required>
                <label class="form-check-label" for="privada">Privada</label>
            </div>
            <!-- se muestra el codigo de sala y acceso generado por js -->
            <div class="form-group">
                <label for="codigoSala">Código de Sala:</label>
                <input type="text" class="form-control" id="codigoSala" name="codigoSala" readonly>

                <label for="codigoAcceso">Código de Acceso:</label>
                <input type="text" class="form-control" id="codigoAcceso" name="codigoAcceso" readonly>
            </div>
            <!--mesaje predefinido con los codigos para realizar una invitacion  -->
            <div>
                <textarea name="mensaje" id="invitacion" cols="50" rows="6" readonly>

                </textarea>
            </div>

    </div>

        <button type="submit" class="btn btn-primary">Crear Partida</button>
    </form>

    <br>

    <table class="table table-striped">
        <caption>Historial de Partidas</caption>
        <thead>
            <tr>
                <th scope="col">Nombre Partida</th>
                <th scope="col">Tipo</th>
                <th scope="col">Código Sala</th>
                <th scope="col">Código Acceso</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td>
                    <button type="button" class="btn btn-primary" onclick="unirsePartida('{{ partida.id }}')">Unirse</button>
                    <button type="button" class="btn btn-danger" onclick="eliminarPartida('{{ partida.id }}')">Eliminar</button>
                </td>
            </tr>
        </tbody>
    </table>
{% endblock %}




*/



// Función para generar un código aleatorio de longitud específica
function generarCodigo(longitud) {
    var codigo = "";
    var caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    for (var i = 0; i < longitud; i++) {
        codigo += caracteres.charAt(Math.floor(Math.random() * caracteres.length));
    }
    return codigo;
}

// Función para actualizar los códigos de sala y acceso en el formulario
function actualizarCodigos() {
    var publica = document.getElementById("publica").checked;
    var codigoSala = generarCodigo(10); // Generar un código de 6 caracteres para la sala
    var codigoAcceso = "";
    
    if (!publica) {
        codigoAcceso = generarCodigo(10); // Generar un código de 4 caracteres para el acceso si es privada
    }
    
    document.getElementById("codigoSala").value = codigoSala;
    document.getElementById("codigoAcceso").value = codigoAcceso;
    
    // Actualizar el mensaje de invitación
    var mensajeInvitacion = "Envía el siguiente código de sala y acceso a tus amigos:   \n\n";
    mensajeInvitacion += "  El código de sala es: " + codigoSala + "\n";
    mensajeInvitacion += "  El código de acceso es: " + codigoAcceso;
    document.getElementById("invitacion").innerText = mensajeInvitacion;
}


// Función para crear una partida (puedes manejar el envío al servidor aquí)
function crearPartida() {
    // Aquí podrías enviar los datos del formulario al servidor utilizando fetch o axios
    // Por ejemplo, capturando los valores de nombrePartida, tipoPartida, codigoSala, codigoAcceso
    var nombrePartida = document.getElementById("nombrePartida").value;
    var tipoPartida = document.querySelector('input[name="tipoPartida"]:checked').value;
    var codigoSala = document.getElementById("codigoSala").value;
    var codigoAcceso = document.getElementById("codigoAcceso").value;

    console.log("Nombre de la partida:", nombrePartida);
    console.log("Tipo de partida:", tipoPartida);
    console.log("Código de sala:", codigoSala);
    console.log("Código de acceso:", codigoAcceso);
        // Aquí puedes crear un objeto con los datos de la partida
        var partida = {
            id: generarCodigo(6), // Generar un ID único para la partida (ejemplo)
            nombre: nombrePartida,
            tipo: tipoPartida,
            codigoSala: codigoSala,
            codigoAcceso: codigoAcceso
        };
            // Mostrar la partida en la tabla
    mostrarPartidaEnTabla(partida);

    // Guardar la partida en el Local Storage
    guardarPartida(partida);
    // Limpiar el formulario y actualizar los códigos
    document.getElementById("nombrePartida").value = "";
    document.getElementById("publica").checked = true;
    actualizarCodigos();

}


// Función para eliminar una partida y actualizar la tabla
function eliminarPartida() {
// Eliminar desde la tabla
    var fila = this.event.target.parentNode.parentNode;
    fila.parentNode.removeChild(fila);
    // Eliminar desde el Local Storage
    var id = this.event.target.getAttribute("data-id");
    var partidas = JSON.parse(localStorage.getItem("partidas")) || [];
    partidas = partidas.filter(partida => partida.id !== id);
    localStorage.setItem("partidas", JSON.stringify(partidas));
}

// Asociar la función actualizarCodigos al cambio en los radios de tipo de partida
document.querySelectorAll('input[name="tipoPartida"]').forEach(radio => {
    radio.addEventListener('change', actualizarCodigos);
});

// Llamar a actualizarCodigos al cargar la página para inicializar los códigos
actualizarCodigos();


// mostramos los datos en la tabla de partidas y los guardamos en local storagefunction mostrarPartidaEnTabla(partida) {
function mostrarPartidaEnTabla(partida) {

    var tabla = document.querySelector("table tbody");
    var fila = document.createElement("tr");
    fila.innerHTML = `
        <td>${partida.nombre}</td>
        <td>${partida.tipo}</td>
        <td>${partida.codigoSala}</td>
        <td>${partida.codigoAcceso}</td>
        <td>
            <button type="button" class="btn btn-primary" onclick="unirsePartida('${partida.id}')">Unirse</button>
            <button type="button" class="btn btn-danger" onclick="eliminarPartida('${partida.id}')">Eliminar</button>
        </td>
    `;
    tabla.appendChild(fila);
}

// Función para guardar una partida en el Local Storage
function guardarPartida(partida) {
    // Obtener partidas existentes del Local Storage
    var partidas = JSON.parse(localStorage.getItem("partidas")) || [];
    // Agregar la nueva partida
    partidas.push(partida);
    // Guardar las partidas actualizadas en el Local Storage
    localStorage.setItem("partidas", JSON.stringify(partidas));
}

// Función para cargar y mostrar las partidas guardadas al cargar la página
function cargarPartidasGuardadas() {
    var partidas = JSON.parse(localStorage.getItem("partidas")) || [];
    partidas.forEach(partida => {
        mostrarPartidaEnTabla(partida);
    });
}






// Llamar a cargarPartidasGuardadas al cargar la página para inicializar la tabla
window.onload = cargarPartidasGuardadas;