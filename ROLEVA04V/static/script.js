const store = Vuex.createStore({
    state() {
        return {
            nombrejuego: 'Juanito en una galaxia muy muy lejana', 
            subtitulobanner: 'Regístrate ahora y conviértete en una leyenda de la más grande galaxia jamás creada',
            mensaje: 'Antes de convertirte en una leyenda debes decidir qué camino recorrerás. ¿Serás un Sith Lord? ¿Un Jedi? ¿Piloto de aviones para la república? ¿Crearás droides? ¿Serás un cazarrecompensas? Tú eliges a qué te dedicas y qué te llevará a la gloria.',
            botones: [
                { texto: 'Regístrate y Juega!', clase: 'btn btn-warning btn-lg my-2', accion: 'registrar' },
                {texto: 'Conoce más', clase: 'btn btn-primary btn-lg my-2', accion: 'conocer'},
            ],
            metricas: ['+1.000.000 Jugadores Registrados', '+50 Roles diferentes' , 'Servidores Dedicados', 'Actualizaciones Semanales y Eventos Especiales Mensuales'],
            caracteristicas: ['Personalizacion de personajes completa', 'Miles de planetas por explorar', 'Juego solo o con tus amigos'],
            requisitos: ['Windows 10', 'Procesador Intel Core i5', '8GB de RAM', 'DirectX 12', '80GB de espacio en disco'],
            botoncalltoaction: [{ texto: 'Regístrate y Juega!', clase: 'btn btn-warning btn-lg my-2', accion: 'registrar' }],
            contadorClicks: parseInt(localStorage.getItem('contadorClicks')) || 0
        }
    },
    getters: {
        nombrejuego: state => state.nombrejuego,
        subtitulobanner: state => state.subtitulobanner,
        mensaje: state => state.mensaje,
        botones: state => state.botones,
        metricas: state => state.metricas,
        caracteristicas: state => state.caracteristicas,
        requisitos: state => state.requisitos,
        botoncalltoaction: state => state.botoncalltoaction,
        contadorClicks: state => state.contadorClicks
    },
    mutations: {
        incrementarContadorClicks(state) {
            state.contadorClicks++;
            localStorage.setItem('contadorClicks',state.contadorClicks)
            console.log(`Contador de clics: ${state.contadorClicks}`);
        }
    }, 
    actions: {
        registrarClick({ commit }, tipo) {
            axios.post('http://localhost:3000/api/registrarClick', { tipo })
            console.log(`Clic en el botón: ${tipo}`);
            commit('incrementarContadorClicks');
        }
    }
});

const app = Vue.createApp({
    data() {
        return {
            titulo : this.$store.getters.nombrejuego,
            subtitulo : this.$store.getters.subtitulobanner,
            mensaje : this.$store.getters.mensaje,
        }
    },
    computed: {
        nombrejuego() {
            return this.$store.getters.nombrejuego
    },
    subtitulobanner() {
        return this.$store.getters.subtitulobanner
    },
    mensaje() {
        return this.$store.getters.mensaje
    },
    botones() {
        return this.$store.getters.botones
    },
    botonoconocemas() {
        return this.$store.getters.botonoconocemas
    },
    metricas() {
        return this.$store.getters.metricas
    },
    caracteristicas() {
        return this.$store.getters.caracteristicas
    },
    requisitos() {
        return this.$store.getters.requisitos
    },
    botoncalltoaction() {
        return this.$store.getters.botoncalltoaction
    }
    },
    methods: {
        registrarClick(tipo){
            this.$store.dispatch('registrarClick', tipo);

    },
    mostrarModal(){
        const modal = new bootstrap.Modal(document.getElementById('modalConoceMas'));
        modal.show()
    }
    },
});

app.use(store);
app.mount('#app');