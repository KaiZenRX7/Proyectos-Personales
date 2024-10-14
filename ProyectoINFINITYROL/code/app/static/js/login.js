document.addEventListener("DOMContentLoaded", function() {
    const forminicio = document.getElementById("form-inicio");
    const formregistro = document.getElementById("form-registro");
    const contraseñaolvidada = document.getElementById("contraseña-olvidada");
    const linkregistro = document.getElementById("link-registro");
    const contraseñaolvlink = document.getElementById("contraseña-olv-link");
    const botonvolverreg = document.getElementById("boton-volver-reg");
    const botonvolvercon = document.getElementById("boton-volver-con");

    function UsuarioValido(usuario) {
        const usuarioRegex = /^[a-zA-Z0-9]{4,16}$/;
        return usuarioRegex.test(usuario);
    }

    function ContraseñaValida(contraseña) {
        const contraseñaRegex = /^[a-zA-Z0-9]{4,16}$/;
        return contraseñaRegex.test(contraseña);
    }

    if (forminicio) {
        forminicio.addEventListener("submit", function(event) {
            event.preventDefault();

            const usuario = document.getElementById("usuario").value;
            const contraseña = document.getElementById("contraseña").value;
            const recuerdame = document.getElementById("recuerdame").checked;

            if (!UsuarioValido(usuario)) {
                this.innerHTML = "Usuario Invalido";
                console.log("Usuario Invalido");
                return;
            }

            if (!ContraseñaValida(contraseña)) {
                this.innerHTML = "Contraseña Invalida";
                console.log("Contraseña Invalida");
                return;
            }

            axios.post('http://127.0.0.1:5000/login', {
                usuario: usuario,
                contraseña: contraseña,
                recuerdame: recuerdame
            })
            .then(function (response) {
                if (response.data.login) {
                    if (recuerdame) {
                        localStorage.setItem('token', response.data.token);
                    }
                    alert("Inicio de Sesion Exitoso");
                    console.log("Inicio de Sesion Exitoso");
                } else {
                    console.log("Inicio de Sesion Fallido");
                    document.getElementById("error-message").textContent = response.data.message || "Inicio de Sesion Fallido";
                }
            })
            .catch(function (error) {
                console.error('Error:', error);
                document.getElementById("error-message").textContent = "Error de conexión con el servidor, Intentalo denuevo mas tarde";
            });
        });
    }

    if (linkregistro) {
        linkregistro.addEventListener("click", function(event){
            event.preventDefault();
            forminicio.style.display = "none";
            contraseñaolvidada.style.display = "none";
            formregistro.style.display = "block";
        });
    }

    if (contraseñaolvlink) {
        contraseñaolvlink.addEventListener("click", function(event){
            event.preventDefault();
            forminicio.style.display = "none";
            formregistro.style.display = "none";
            contraseñaolvidada.style.display = "block";
        });
    }

    if (botonvolverreg) {         
        botonvolverreg.addEventListener("click", function(event){
            event.preventDefault();
            forminicio.style.display = "block";
            formregistro.style.display = "none";
        });
    }

    if (botonvolvercon) {
        botonvolvercon.addEventListener("click", function(event){
            event.preventDefault();
            forminicio.style.display = "block";
            contraseñaolvidada.style.display = "none";
        });
    }

    formregistro.addEventListener("submit", function(event) {
        event.preventDefault();

        const usuario = document.getElementById("usuario-registro").value;
        const correo = document.getElementById("correo-registro").value;
        const contraseña = document.getElementById("contraseña-registro").value;
        const confirmarContraseña = document.getElementById("confirmar-contraseña").value;

        if (contraseña !== confirmarContraseña) {
            alert("Las contraseñas no coinciden");
            console.log("Las contraseñas no coinciden");
            return;
        }

        axios.post('http://127.0.0.1:5000/register', {
            usuario: usuario,
            correo: correo,
            contraseña: contraseña
        })
        .then(function (response) {
            if (response.data.register) {
                alert("Se ha registrado exitosamente");
                console.log("Registro Exitoso");
            } else {
                console.log("Registro Fallido");
            }
        })
        .catch(function (error) {
            console.error('Error:', error);
        });
    });

    contraseñaolvidada.addEventListener("submit", function(event) {
        event.preventDefault();

        const correo = document.getElementById("correo-contraseña-olvidada").value;

        axios.post('http://127.0.0.1:5000/recuperar_contraseña', {
            correo: correo
        })
        .then(function (response) {
            if (response.data.recuperar) {
                console.log("Correo de recuperación enviado");
            } else {
                console.log("Correo no encontrado");
            }
        })
        .catch(function (error) {
            console.error('Error:', error);
        });
    });
});


document.addEventListener("DOMContentLoaded", function() {
    const modal = new bootstrap.Modal(document.getElementById('terminos'));
    const link = document.getElementById('terminos-link');
    
    link.addEventListener('click', function(event) {
        event.preventDefault();
        modal.show();
    });
});


document.addEventListener("DOMContentLoaded", function() {
    const modal = new bootstrap.Modal(document.getElementById('privacidad'));
    const link = document.getElementById('privacidad-link');
    
    link.addEventListener('click', function(event) {
        event.preventDefault();
        modal.show();
    });
});