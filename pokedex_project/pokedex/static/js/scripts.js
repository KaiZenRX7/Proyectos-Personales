// Inicializa Particles.js
particlesJS('particles-js', {
    particles: {
        number: {
            value: 40,
            density: {
                enable: true,
                value_area: 800
            }
        },
        color: {
            value: "#ffffff" // Color blanco como base para el efecto.
        },
        shape: {
            type: "image", // Usamos una imagen como partícula
            image: {
                src: pokeballImageUrl, // URL de la Pokébola
                width: 20,
                height: 20
            }
        },
        opacity: {
            value: 0.8,
            random: false,
            anim: {
                enable: false,
                speed: 1,
                opacity_min: 0.1,
                sync: false
            }
        },
        size: {
            value: 15, // Tamaño inicial de las Pokébolas
            random: true,
            anim: {
                enable: true,
                speed: 40,
                size_min: 10,
                sync: false
            }
        },
        line_linked: {
            enable: false // Desactiva líneas para que no afecten la estética
        },
        move: {
            enable: true,
            speed: 5,
            direction: "none",
            random: false,
            straight: false,
            out_mode: "out",
            bounce: false,
            attract: {
                enable: false,
                rotateX: 600,
                rotateY: 1200
            }
        }
    },
    interactivity: {
        detect_on: "canvas",
        events: {
            onhover: {
                enable: true,
                mode: "grab" // Cambiar a "repulse" si prefieres un efecto diferente
            },
            onclick: {
                enable: true,
                mode: "push"
            },
            resize: true
        },
        modes: {
            grab: {
                distance: 200,
                line_linked: {
                    opacity: 0.5
                }
            },
            bubble: {
                distance: 400,
                size: 50,
                duration: 2,
                opacity: 8,
                speed: 3
            },
            repulse: {
                distance: 200,
                duration: 0.4
            },
            push: {
                particles_nb: 4
            },
            remove: {
                particles_nb: 2
            }
        }
    },
    retina_detect: true
});


function confirmLogout() {
    Swal.fire({
        title: '¿Estás seguro?',
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, cerrar sesión',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            document.getElementById('logout-form').submit();
        }
    });
}


function capturarPokemon(button) {
    const pokemonId = button.getAttribute('data-pokemon-id');
    const pokemonName = button.getAttribute('data-pokemon-name');

    // Solicitar la lista de entrenadores
    fetch('/pokedex/api/entrenadores/')
        .then(response => response.json())
        .then(data => {
            if (data.entrenadores && Array.isArray(data.entrenadores)) {
                let entrenadoresDisponibles = data.entrenadores.filter(entrenador => entrenador.pokemons.length < 6);
                if (entrenadoresDisponibles.length === 0) {
                    Swal.fire({
                        title: 'Error',
                        text: 'Todos los entrenadores ya tienen 6 Pokémon.',
                        icon: 'error',
                        confirmButtonText: 'Aceptar'
                    });
                } else {
                    let entrenadoresHtml = '';
                    entrenadoresDisponibles.forEach(entrenador => {
                        entrenadoresHtml += `
                            <div>
                                <input type="checkbox" name="entrenadores" value="${entrenador.id}" id="entrenador-${entrenador.id}">
                                <label for="entrenador-${entrenador.id}">${entrenador.nombre}</label>
                            </div>
                        `;
                    });

                    // Obtener el token CSRF
                    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

                    // Mostrar el formulario dentro del SweetAlert
                    Swal.fire({
                        title: `¿Capturar a ${pokemonName}?`,
                        html: `
                            <p>Selecciona uno o más entrenadores para capturar a ${pokemonName}:</p>
                            <form id="capturar-form">
                                <input type="hidden" name="pokemon_id" value="${pokemonId}">
                                <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                                ${entrenadoresHtml}
                            </form>
                        `,
                        showCancelButton: true,
                        confirmButtonText: 'Capturar',
                        cancelButtonText: 'Cancelar',
                        focusConfirm: false,
                        preConfirm: () => {
                            const selectedEntrenadores = [];
                            document.querySelectorAll('#capturar-form input[name="entrenadores"]:checked')
                                .forEach(checkbox => selectedEntrenadores.push(checkbox.value));

                            if (selectedEntrenadores.length === 0) {
                                Swal.showValidationMessage('Selecciona al menos un entrenador.');
                                return false;
                            }

                            return selectedEntrenadores;
                        }
                    }).then(result => {
                        if (result.isConfirmed) {
                            const form = document.getElementById('capturar-form');
                            const formData = new FormData(form);

                            // Añadir los IDs de entrenadores seleccionados al FormData
                            result.value.forEach(entrenadorId => {
                                formData.append('entrenadores', entrenadorId);
                            });

                            // Mostrar un loader mientras se procesa la captura
                            Swal.fire({
                                title: 'Capturando...',
                                html: '<img src="/static/images/pokeballcaptura.png" alt="Cargando..." style="width:300px;height:200px;">',
                                showConfirmButton: false,
                                allowOutsideClick: false,
                                timer: 3000,
                                didOpen: () => {
                                    Swal.showLoading();
                                }
                            }).then(() => {
                                // Enviar el formulario al servidor
                                fetch('/pokedex/pokemons/', {
                                    method: 'POST',
                                    body: formData,
                                    headers: {
                                        'X-CSRFToken': csrfToken
                                    }
                                })
                                    .then(response => response.json())
                                    .then(data => {
                                        if (data.success) {
                                            // Mostrar mensaje de éxito
                                            Swal.fire({
                                                title: '¡Capturado!',
                                                text: `Has capturado a ${pokemonName} y se ha unido al(los) entrenador(es) seleccionado(s).`,
                                                icon: 'success'
                                            }).then(() => {
                                                window.location.reload();
                                            });
                                        } else {
                                            // Mostrar mensaje de error
                                            Swal.fire({
                                                title: 'Error',
                                                text: data.error || 'Hubo un problema al capturar el Pokémon.',
                                                icon: 'error'
                                            });
                                        }
                                    })
                                    .catch(error => {
                                        // Manejar errores de la solicitud
                                        Swal.fire({
                                            title: 'Error',
                                            text: `No se pudo enviar la solicitud: ${error.message}`,
                                            icon: 'error'
                                        });
                                    });
                            });
                        }
                    });
                }
            } else {
                // Si no se pudieron cargar los entrenadores
                Swal.fire('Error', 'No se pudo cargar la lista de entrenadores.', 'error');
            }
        })
        .catch(error => {
            // Manejar errores al cargar la lista de entrenadores
            Swal.fire('Error', `No se pudo cargar la lista de entrenadores: ${error.message}`, 'error');
        });
}



function confirmUpdate() {
    const form = document.getElementById('update-form');
    const formData = new FormData(form);
    let changes = '';

    formData.forEach((value, key) => {
        const originalValue = form.querySelector(`[name="${key}"]`).defaultValue;
        if (value !== originalValue) {
            changes += `${key}: ${originalValue} -> ${value}\n`;
        }
    });

    if (changes) {
        Swal.fire({
            title: 'Confirmar Actualización',
            text: `Estás a punto de cambiar los siguientes atributos:\n${changes}`,
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, actualizar',
            cancelButtonText: 'Cancelar'            
        }).then((result) => {
            if (result.isConfirmed) {
                // Enviar el formulario usando fetch para manejar la respuesta
                fetch(form.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                })
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        return response.json().then(data => {
                            throw new Error(JSON.stringify(data.errors));
                        });
                    }
                })
                .then(data => {
                    if (data.success) {
                        Swal.fire({
                            title: '¡Actualizado!',
                            text: 'El Pokémon ha sido actualizado correctamente.',
                            icon: 'success',
                            confirmButtonColor: '#3085d6'
                        }).then(() => {
                            window.location.href = data.redirect_url;
                        });
                    } else {
                        Swal.fire({
                            title: 'Error',
                            text: 'Hubo un problema al actualizar el Pokémon.',
                            icon: 'error'
                        });
                    }
                })
                .catch(error => {
                    const errors = JSON.parse(error.message);
                    for (const [field, messages] of Object.entries(errors)) {
                        const input = form.querySelector(`[name="${field}"]`);
                        if (input) {
                            const errorDiv = document.createElement('div');
                            errorDiv.className = 'invalid-feedback d-block';
                            errorDiv.innerHTML = messages.map(msg => msg.message).join('<br>');
                            input.parentNode.appendChild(errorDiv);
                        }
                    }
                });
            }
        });
    } else {
        Swal.fire({
            title: 'Sin Cambios',
            text: 'No has realizado ningún cambio.',
            icon: 'info',
            confirmButtonColor: '#3085d6'
        });
    }
}

// Añadir el evento de clic al botón de actualización
document.addEventListener("DOMContentLoaded", function () {
    const updateButton = document.getElementById("update-button");
    if (updateButton) {
        updateButton.addEventListener("click", confirmUpdate);
    }
});