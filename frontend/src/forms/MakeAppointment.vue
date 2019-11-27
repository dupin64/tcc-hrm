<template>
    <el-form :model="appointment" ref="appointment" label-width="120px" label-position="top">
        <template v-if="userIsStaff">
            <el-form-item label="Patient" prop="patient" required>
                <el-select
                        v-model="appointment.patient"
                        filterable
                        remote
                        placeholder="Please enter the patient's name"
                        :remote-method="getPatients"
                        :loading="loading">
                    <el-option
                            v-for="item in patients"
                            :key="item.id"
                            :label="item.user__name"
                            :value="item.id">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item v-if="patient" label="Specialist" prop="specialist" required>
                <el-select
                        v-model="appointment.specialist"
                        filterable
                        remote
                        placeholder="Please enter the specialist's name"
                        :remote-method="getSpecialists"
                        :loading="loading">
                    <el-option
                            v-for="item in specialists"
                            :key="item.id"
                            :label="item.user__name"
                            :value="item.id">
                    </el-option>
                </el-select>
            </el-form-item>
        </template>
        <el-form-item label="Title" prop="title" required>
            <el-input v-model="appointment.title"></el-input>
        </el-form-item>
        <el-form-item label="Date and time" required>
            <el-date-picker type="datetime" placeholder="Pick a date and time" v-model="appointment.date"
                            style="width: 100%;"></el-date-picker>
        </el-form-item>
        <el-form-item label="Notes" prop="notes" required>
            <el-input type="textarea" v-model="appointment.notes"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="bookAppoinment">Confirm</el-button>
            <el-button @click="clearAppointment">Cancel</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
    import {mapGetters} from 'vuex';

    export default {
        data() {
            return {
                appointmentUrl: 'activity/appointment',
                patientsUrl: 'account/patient?keyword=',
                specialistsUrl: 'account/search?id=',
                appointment: {
                    title: '',
                    notes: '',
                    date: ''
                },
                patients: [],
                loading: false
            }
        },
        props: {
            specialist: Object,
            tempDate: String,
            patient: Object
        },
        computed: {
            ...mapGetters(['userIsStaff']),
        },
        watch: {
            tempDate(val) {
                if (val) {
                    this.appointment.date = val;
                }
            },
            patient: {
                handler(val) {
                    if (val) {
                        this.patients.push(val);
                        this.appointment.patient = val.id;
                    }
                },
                deep: true,
				immediate: true
            }
        },
        methods: {
            bookAppoinment: function () {
                let appointment = {...this.appointment};

                if (this.specialist && this.specialist.id) {
                    appointment.specialist = this.specialist.id;
                }

                if (this.appointment.patient) {
                    delete this.appointment.patient;
                }

                axios.post(this.appointmentUrl, appointment).then((response) => {
                    if (response.data.success) {
                        this.$message.success('The appointment has been booked');
                        this.clearAppointment();
                    } else {
                        this.$message.error('An error occurred. Please try again');
                    }
                }).catch(() => this.$message.error('An error occurred. Please try again'));
            },
            clearAppointment: function () {
                this.$refs['appointment'].resetFields();
            },
            getPatients(query) {
                this.loading = true;
                axios.get(`${this.patientsUrl}${query}`).then((response) => {
                    this.patients = response.data.result;
                    this.loading = false;
                }).catch(() => {
                    this.loading = false;
                    this.patients = [];
                });
            },
            getSpecialists(query) {
                this.loading = true;
                axios.get(`${this.specialistsUrl}${query}`).then((response) => {
                    this.specialists = response.data.result;
                    this.loading = false;
                }).catch(() => {
                    this.loading = false;
                    this.specialists = [];
                });
            }
        }
    }
</script>