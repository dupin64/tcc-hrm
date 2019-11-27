import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        userType: window.userType
    },
    getters: {
        userType: state => {
            return state.userType;
        },
        userIsStaff: state => {
            return ['receptionist', 'specialist'].includes(state.userType);
        }
    },
    mutations: {},
    actions: {}
});