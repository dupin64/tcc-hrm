import Vue from 'vue';
import Router from 'vue-router';

//components
import Appointments from '../components/Appointments.vue';
import Specialists from '../components/Specialists.vue';
import Specialist from '../components/Specialist.vue';
import Patients from '../components/Patients.vue';
import Patient from '../components/Patient.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'appointments',
            component: Appointments
        },
        {
            path: '/specialists',
            name: 'specialists',
            component: Specialists
        },
        {
            path: '/specialist/:id',
            name: 'specialist',
            component: Specialist
        },
        {
            path: '/patients',
            name: 'patients',
            component: Patients
        },
        {
            path: '/patient/:id',
            name: 'patient',
            component: Patient
        },
    ]
});
