const store = Vuex.createStore({
    state() {
        return {
            productos: [
                {id: 1, nombre: 'Filtro de aire SuperCar', sku: '', stock: 5, disponible: true, categoria: 'Filtros'},
                {id: 2, nombre: 'Filtro de aceite Aceitosin', sku: '', stock: 18, disponible: true, categoria: 'Filtros'},
                {id: 3, nombre: 'Neumáticos 18" SpeedHunter', sku: '', stock: 1, disponible: true, categoria: 'Neumáticos'},
                {id: 4, nombre: 'Llantas 17" Racing', sku: '', stock: 3, disponible: true, categoria: 'Llantas'},
                {id: 5, nombre: 'Bujías NGK', sku: '', stock: 15, disponible: true, categoria: 'Bujías'},
                {id: 6, nombre: 'Pastillas de freno Brembo', sku: '', stock: 8, disponible: true, categoria: 'Frenos'}
            ],
            pedidos: [
                {id: 1, detalles: 'Pedido 1'},
                {id: 2, detalles: 'Pedido 2'}
            ],
            nuevoPedido: '',
            nuevoProducto: {
                nombre: '',
                stock: '',
                disponible: true,
                categoria: ''
            },
            currentView: 'menu'
        };
    },
    mutations: {
        cambiarVista(state, vista) {
            state.currentView = vista;
        },
        agregarPedido(state, detalles) {
            state.pedidos.push({ id: Date.now(), detalles });
        },
        actualizarNuevoPedido(state, detalles) {
            state.nuevoPedido = detalles;
        },
        agregarProducto(state, producto) {
            state.productos.push({
                id: Date.now(),
                nombre: producto.nombre,
                sku: Math.floor(Math.random() * 1000000000).toString().padStart(9, '0'),
                stock: producto.stock,
                disponible: producto.disponible === 'true',
                categoria: producto.categoria
            });
        },
        actualizarNuevoProducto(state, producto) {
            state.nuevoProducto = producto;
        },
        generarSku(state) {
            state.productos.forEach(producto => {
                producto.sku = Math.floor(Math.random() * 1000000000).toString().padStart(9, '0');
            });
        }
    },
    actions: {
        cambiarVista({ commit }, vista) {
            commit('cambiarVista', vista);
        },
        agregarPedido({ commit, state }) {
            if (state.nuevoPedido.trim()) {
                commit('agregarPedido', state.nuevoPedido);
                commit('actualizarNuevoPedido', '');
            }
        },
        agregarProducto({ commit, state }) {
            if (state.nuevoProducto.nombre.trim() && state.nuevoProducto.categoria.trim()) {
                commit('agregarProducto', state.nuevoProducto);
                commit('actualizarNuevoProducto', { nombre: '', stock: '', disponible: 'true', categoria: '' });
            }
        },
        generarSku({ commit }) {
            commit('generarSku');
        }
    },
    getters: {
        productosMenosStock(state) {
            return state.productos.sort((a, b) => a.stock - b.stock).slice(0, 10);
        },
        ultimosPedidos(state) {
            return state.pedidos.slice(-10);
        }
    }
});

const app = Vue.createApp({
    data() {
        return {
            currentView: 'menu',
            nuevoPedido: '',
            nuevoProducto: {
                nombre: '',
                stock: '',
                disponible: '',
                categoria: ''
            }
        };
    },
    computed: {
        productos() {
            return this.$store.state.productos;
        },
        pedidos() {
            return this.$store.state.pedidos;
        },
        productosMenosStock() {
            return this.$store.getters.productosMenosStock;
        },
        ultimosPedidos() {
            return this.$store.getters.ultimosPedidos;
        }
    },
    methods: {
        menu() {
            this.currentView = 'menu';
        },
        inventario() {
            this.currentView = 'inventario';
        },
        mostrarProductos() {
            this.currentView = 'productos';
        },
        mostrarPedidos() {
            this.currentView = 'pedidos';
        },
        agregarPedido() {
            this.$store.dispatch('agregarPedido');
            this.nuevoPedido = '';
        },
        agregarProducto() {
            this.$store.dispatch('agregarProducto');
            this.nuevoProducto = { nombre: '', stock: '', disponible: '', categoria: '' };
        }
    },
    watch: {
        nuevoPedido(val) {
            this.$store.commit('actualizarNuevoPedido', val);
        },
        nuevoProducto: {
            deep: true,
            handler(val) {
                this.$store.commit('actualizarNuevoProducto', val);
            }
        }
    },
    mounted() {
        this.$store.dispatch('generarSku');
    }
});

app.use(store);
app.mount('#app');
