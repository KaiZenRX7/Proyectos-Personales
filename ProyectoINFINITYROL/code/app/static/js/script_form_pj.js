$(document).ready(function() {
    $('#raza').on('change', function() {
        let raza = $(this).val();
        $.ajax({
            type: 'GET',
            url: '/descripcionRaza/' + raza,
            success: function(response) {
                $('#descripcion-raza').text(response.descripcion);
            },
            error: function(response) {
                $('#descripcion-raza').text('Error al obtener la descripción de la raza');
            }
        });
    });

    $('#profesion').on('change', function() {
        let profesion = $(this).val();
        $.ajax({
            type: 'GET',
            url: '/descripcionProfesion/' + profesion,
            success: function(response) {
                $('#descripcion-profesion').text(response.descripcion);
            },
            error: function(response) {
                $('#descripcion-profesion').text('Error al obtener la descripción de la profesión');
            }
        });
    });

    $('#formulario').on('submit', function(event) {
        event.preventDefault();
        let nombrepersonaje = $('#nombrepersonaje').val();
        let nombrejugador = $('#nombrejugador').val();
        let raza = $('#raza').val();
        let profesion = $('#profesion').val();

        $.ajax({
            type: 'POST',
            url: '/enviaDatosForm',
            data: {
                nombrejugador: nombrejugador,
                nombrepersonaje: nombrepersonaje,
                raza: raza,
                profesion: profesion
            },
            success: function(response) {
                alert('Datos enviados correctamente');
                $('#formulario')[0].reset();
                $('#descripcion-raza').text('');
                $('#descripcion-profesion').text('');
            },
            error: function(response) {
                alert('Error al enviar los datos: ' + response.responseJSON.error);
            }
        });
    });
});