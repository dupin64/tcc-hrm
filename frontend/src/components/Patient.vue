<template>
    <div class="container" v-loading="!patient">
        <el-row :gutter="30" v-if="patient">
            <el-col :span="12">
                <el-card>
                    <div class="header">
                        <p>Name: {{ patient.user__name }}</p>
                    </div>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card>
                    <el-tabs v-model="activeTab">
                        <el-tab-pane label="History" name="history">
                            <history :patient="patient.id"></history>
                        </el-tab-pane>
                        <el-tab-pane v-if="formHeader" :label="userType === 'specialist' ? 'Refer' : 'Book appointment'" name="booking" class="booking">
                            <h3> {{ formHeader }} </h3>
                            <make-appointment :patient="patient"></make-appointment>
                        </el-tab-pane>
                    </el-tabs>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import MakeAppointment from '../forms/MakeAppointment.vue';
    import History from './History.vue';

    export default {
        data() {
            return {
                patient: null,
                activeTab: 'history',
                patientUrl: 'account/patient?id=',
                tempDate: ''
            }
        },
        computed: {
            ...mapGetters(['userType']),
            formHeader() {
                return this.userType === 'specialist' ? 'Refer a patient' : this.userType === 'receptionist' ? 'Book appointment for patient' : '';
            }
        },
        components: {MakeAppointment, History},
        methods: {
            getPatient: function (id) {
                axios.get(`${this.patientUrl}${id}`).then((response) => {
                    this.patient = response.data.result[0] || {};
                });
            }
        },
        mounted() {
            if (this.$route.params.id) {
                this.getPatient(this.$route.params.id);
            }
        }
    }
</script>

<style>
    .booking h3 {
        text-align: center;
    }
</style>