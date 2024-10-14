/* estructura del archivo data.json
{
  "razas": [
    {
      "nombre": "Humano",
      "descripcion": "Los más comunes, se adaptan y aprenden rápido pero no poseen habilidades raciales."
    },
    {
      "nombre": "Elfo",
      "descripcion": "Elegantes y ágiles, poseen habilidades naturales en la magia y arquería."
    },
    {
      "nombre": "Enano",
      "descripcion": "Resistentes y expertos en la minería y la forja, conocidos por su resistencia física."
    },
    {
      "nombre": "Orco",
      "descripcion": "Fuertes y feroces, expertos en el combate cuerpo a cuerpo."
    },
    {
      "nombre": "Mediano",
      "descripcion": "Ágiles y sigilosos, excelentes en el robo y la exploración."
    },
    {
      "nombre": "Gnomo",
      "descripcion": "Ingeniosos e inventivos, dominan la magia y la creación de artefactos."
    }
  ],
  "profesiones": {
    "Guerrero": {
      "descripcion": "Experto luchador, siempre en la línea del frente.",
      "habilidades": {
        "Ataque": "Aumenta el daño infligido.",
        "Ataque Rapido": "Permite realizar un ataque adicional.",
        "Defensa": "Aumenta la resistencia a los ataques.",
        "Curación": "Permite curar heridas."
      },
      "poderes": {
        "Golpe Feroz": "Usando todo su peso y fuerza, el guerrero inflige un golpe devastador.",
        "Rugido de Batalla": "El guerrero lanza un rugido que intimidará a sus enemigos.",
        "Grito de Guerra": "El guerrero lanza un grito que inspirará a sus aliados.",
        "Golpe Aguijón": "El guerrero golpea con tal fuerza que puede atravesar la armadura del enemigo."
      },
      "equipamiento": {
        "armas": {
          "Espada y Escudo": {
            "Espada y Escudo de Madera": "Hecho de madera, util para entrenar pero, poco efectivo en combate.",
            "Espada y Escudo de Latón": "Hecho de una aleación de cobre y zinc, resistente pero se desafila con facilidad.",
            "Espada y Escudo de Hierro": "Hecho de hierro, resistente, duradero pero cuidado con la oxidación.",
            "Espada y Escudo de Acero": "Hecho de acero, no se desafila, resistente y duradero."
          }
        },
        "armaduras": {
          "Pechera": {            
          "Pechera de cuero": "Hecho de cuero, ligero y flexible.",
          "Pechera de placas": "Hecho de placas de metal, resistente pero pesado.",
          "Pechera de mallas": "Hecho de anillas de metal, resistente y flexible.",
          "Pechera de escamas": "Hecho de escamas de metal, resistente y ligero."
          },
          "Casco": {
            "Casco de cuero": "Hecho de cuero, ligero y flexible.",
            "Casco de placas": "Hecho de placas de metal, resistente pero pesado.",
            "Casco de mallas": "Hecho de anillas de metal, resistente y flexible.",
            "Casco de escamas": "Hecho de escamas de metal, resistente y ligero."
          },
          "Pantalón": {
            "Pantalón de cuero": "Hecho de cuero, ligero y flexible.",
            "Pantalón de placas": "Hecho de placas de metal, resistente pero pesado.",
            "Pantalón de mallas": "Hecho de anillas de metal, resistente y flexible.",
            "Pantalón de escamas": "Hecho de escamas de metal, resistente y ligero."
          },
          "Botas": {
            "Botas de cuero": "Hecho de cuero, ligero y flexible.",
            "Botas de placas": "Hecho de placas de metal, resistente pero pesado.",
            "Botas de mallas": "Hecho de anillas de metal, resistente y flexible.",
            "Botas de escamas": "Hecho de escamas de metal, resistente y ligero."
          },
          "Guantes": {
            "Guantes de cuero": "Hecho de cuero, ligero y flexible.",
            "Guantes de placas": "Hecho de placas de metal, resistente pero pesado.",
            "Guantes de mallas": "Hecho de anillas de metal, resistente y flexible.",
            "Guantes de escamas": "Hecho de escamas de metal, resistente y ligero."
          },
          "Capa": {
            "Capa de cuero": "Hecho de cuero, ligero y flexible.",
            "Capa de placas": "Hecho de placas de metal, resistente pero pesado.",
            "Capa de mallas": "Hecho de anillas de metal, resistente y flexible.",
            "Capa de escamas": "Hecho de escamas de metal, resistente y ligero."

          }
        }
      }
    },
    "Mago": {
      "descripcion": "Maestro en el uso de la magia y la curación.",
      "habilidades": {
      "Magia": "Permite lanzar poderosos hechizos.",
      "Curación": "Permite sanar heridas y restaurar la salud."
      },
      "poderes": {
      "Rayo": "Lanza un rayo de energía mágica.",
      "Curación": "Realiza una curación instantánea."
      },
      "equipamiento": {
      "armas": {
        "Varita y Daga de Madera": "Hecho de madera, ideal para principiantes.",
        "Varita y Daga de Hueso": "Hecho de hueso, aumenta el poder mágico.",
        "Varita y Daga de Hierro": "Hecho de hierro, mayor precisión y daño.",
        "Varita y Daga de Acero": "Hecho de acero, máximo poder mágico.",
        "Bastón de Madera": "Hecho de madera, aumenta el alcance de los hechizos.",
        "Bastón de Hueso": "Hecho de hueso, mayor poder mágico.",
        "Bastón de Hierro": "Hecho de hierro, mayor precisión y daño.",
        "Bastón de Acero": "Hecho de acero, máximo poder mágico."
      },
      "armaduras": {
        "Pechera": {
        "Pechera de tela": "Hecha de tela, ligera pero ofrece poca protección."
        },
        "Pantalón": {
        "Pantalón de tela": "Hecho de tela, ligero y flexible."
        },
        "Botas": {
        "Botas de tela": "Hechas de tela, ligeras y flexibles."
        },
        "Casco": {
        "Casco de tela": "Hecho de tela, ligero y flexible."
        },
        "Capa": {
        "Capa de tela": "Hecha de tela, ligera y flexible."
        }
      }
      }
    },
    "Arquero": {
      "descripcion": "Experto en el uso del arco y habilidades de robo.",
      "habilidades": {
      "Ataque": "Permite disparar flechas con gran precisión.",
      "Defensa": "Aumenta la resistencia a los ataques.",
      "Robo": "Permite robar objetos y desactivar trampas."
      },
      "poderes": {
      "Curación": "Realiza una curación instantánea.",
      "Rayo": "Lanza una flecha cargada de energía eléctrica."
      },
      "equipamiento": {
      "armas": {
        "Arco": "Arma principal del arquero, ideal para ataques a distancia."
      },
      "armaduras": {
        "Pechera": {
        "Pechera de cuero": "Hecho de cuero, ligero y flexible."
        },
        "Pantalón": {
        "Pantalón de cuero": "Hecho de cuero, ligero y flexible."
        },
        "Botas": {
        "Botas de cuero": "Hechas de cuero, ligeras y flexibles."
        },
        "Casco": {
        "Casco de cuero": "Hecho de cuero, ligero y flexible."
        },
        "Capa": {
        "Capa de cuero": "Hecha de cuero, ligera y flexible."
        }
      }
      }
    },
    "Ladrón": {
      "descripcion": "Especializado en el robo y el sigilo.",
      "habilidades": {
      "Robo": "Permite abrir cerraduras y desactivar trampas.",
      "Ataque": "Permite realizar ataques rápidos y precisos.",
      "Defensa": "Aumenta la resistencia a los ataques."
      },
      "poderes": {
      "Robo": "Realiza un robo sigiloso y eficiente."
      },
      "equipamiento": {
      "armas": {
        "Daga": "Arma principal del ladrón, ideal para ataques rápidos y sigilosos."
      },
      "armaduras": {
        "Pechera": {
        "Pechera de cuero": "Hecho de cuero, ligero y flexible."
        },
        "Pantalón": {
        "Pantalón de cuero": "Hecho de cuero, ligero y flexible."
        },
        "Botas": {
        "Botas de cuero": "Hechas de cuero, ligeras y flexibles."
        },
        "Casco": {
        "Casco de cuero": "Hecho de cuero, ligero y flexible."
        },
        "Capa": {
        "Capa de cuero": "Hecha de cuero, ligera y flexible."
        }
      }
      }
    },
    "Paladín": {
      "descripcion": "Guerrero sagrado, experto en la defensa y la curación.",
      "habilidades": {
      "Ataque": "Permite realizar ataques poderosos.",
      "Defensa": "Aumenta la resistencia a los ataques.",
      "Curación": "Permite sanar heridas y restaurar la salud."
      },
      "poderes": {
      "Curación": "Realiza una curación instantánea.",
      "Escudo": "Crea un escudo protector que reduce el daño recibido."
      },
      "equipamiento": {
      "armas": {
        "Espada": "Arma principal del paladín, ideal para combate cuerpo a cuerpo.",
        "Escudo": "Ofrece protección adicional y aumenta la defensa."
      },
      "armaduras": {
        "Pechera": {
        "Pechera de cuero": "Hecho de cuero, ligero y flexible."
        },
        "Pantalón": {
        "Pantalón de cuero": "Hecho de cuero, ligero y flexible."
        },
        "Botas": {
        "Botas de cuero": "Hechas de cuero, ligeras y flexibles."
        },
        "Casco": {
        "Casco de cuero": "Hecho de cuero, ligero y flexible."
        },
        "Capa": {
        "Capa de cuero": "Hecha de cuero, ligera y flexible."
        }
      }
      }
    }

  }
}

  

*/

/*
ja basado en el archivo data.json, se debe cargar las razas y profesiones en los selects correspondientes
*/
$(document).ready(function() {
    $.getJSON('/data', function(data)
    {
        // Cargar razas
        var razas = data.razas;
        var raza_select = $('#raza');
        $.each(razas, function(index, raza) {
            raza_select.append('<option value="' + raza.nombre + '">' + raza.nombre + '</option>');
            
        });

        // Cargar profesiones
        var profesiones = data.profesiones;
        var profesion_select = $('#profesion');
        $.each(profesiones, function(profesion, value) {
            profesion_select.append('<option value="' + profesion + '">' + profesion + '</option>');
        });

        // cargar habilidades
        $('#profesion').change(function() {
            var profesion = $(this).val();
            var habilidades = profesiones[profesion].habilidades;
            var habilidades_select = $('#habilidades');
            habilidades_select.empty();
            $.each(habilidades, function(habilidad, descripcion) {
                habilidades_select.append('<option value="' + habilidad + '">' + habilidad + '</option>');
            });
        });
        // cargar poderes
        $('#profesion').change(function() {
            var profesion = $(this).val();
            var poderes = profesiones[profesion].poderes;
            var poderes_select = $('#poderes');
            poderes_select.empty();
            $.each(poderes, function(poder, descripcion) {
                poderes_select.append('<option value="' + poder + '">' + poder + '</option>');
            });
        });
        // cargar armas
        $('#profesion').change(function() {
            var profesion = $(this).val();
            var armas = profesiones[profesion].equipamiento.armas;
            var armas_select = $('#armas');
            armas_select.empty();
            $.each(armas, function(arma, descripcion) {
                armas_select.append('<option value="' + arma + '">' + arma + '</option>');
            });
        });
        // cargar pecheras
        $('#profesion').change(function() {
            var profesion = $(this).val();
            var pecheras = profesiones[profesion].equipamiento.armaduras.Pechera;
            var pecheras_select = $('#armaduras');
            pecheras_select.empty();
            $.each(pecheras, function(pechera, descripcion) {
                pecheras_select.append('<option value="' + pechera + '">' + pechera + '</option>');
            });
        });

        // cargar cascos
        $('#profesion').change(function() {
            var profesion = $(this).val();
            var cascos = profesiones[profesion].equipamiento.armaduras.Casco;
            var cascos_select = $('#armaduras');
            cascos_select.empty();
            $.each(cascos, function(casco, descripcion) {
                cascos_select.append('<option value="' + casco + '">' + casco + '</option>');
            });
        });

        // cargar pantalones
        $('#profesion').change(function() {
            var profesion = $(this).val();
            var pantalones = profesiones[profesion].equipamiento.armaduras.Pantalón;
            var pantalones_select = $('#armaduras');
            pantalones_select.empty();
            $.each(pantalones, function(pantalon, descripcion) {
                pantalones_select.append('<option value="' + pantalon + '">' + pantalon + '</option>');
            });
        });

        // cargar botas
        $('#profesion').change(function() {
            var profesion = $(this).val();
            var botas = profesiones[profesion].equipamiento.armaduras.Botas;
            var botas_select = $('#armaduras');
            botas_select.empty();
            $.each(botas, function(bota, descripcion) {
                botas_select.append('<option value="' + bota + '">' + bota + '</option>');
            });
        });

        // cargar guantes
        $('#profesion').change(function() {
            var profesion = $(this).val();
            var guantes = profesiones[profesion].equipamiento.armaduras.Guantes;
            var guantes_select = $('#armaduras');
            guantes_select.empty();
            $.each(guantes, function(guante, descripcion) {
                guantes_select.append('<option value="' + guante + '">' + guante + '</option>');
            });
        });

        // cargar capas
        $('#profesion').change(function() {
            var profesion = $(this).val();
            var capas = profesiones[profesion].equipamiento.armaduras.Capa;
            var capas_select = $('#armaduras');
            capas_select.empty();
            $.each(capas, function(capa, descripcion) {
                capas_select.append('<option value="' + capa + '">' + capa + '</option>');
            });
        });



    });
}
);