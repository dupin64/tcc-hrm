<template>
    <div class="container" v-loading="!specialist">
        <el-row :gutter="30" v-if="specialist">
            <el-col :span="12">
                <el-card>
                    <div class="header">
                        <p>Name: {{ specialist.name }}</p>
                        <p>Title: {{ specialist.title }}</p>
                    </div>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card>
                    <el-tabs v-model="activeTab">
                        <el-tab-pane label="Schedule" name="schedule">
                            <calendar @initAppointment="initAppointment" :schedule="specialist.schedule"></calendar>
                        </el-tab-pane>
                        <el-tab-pane v-if="formHeader" label="Booking" name="booking" class="booking">
                            <h3> {{ formHeader }} </h3>
                            <make-appointment :specialist="specialist" :temp-date="tempDate"></make-appointment>
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
    import Calendar from '../utils/FullCalendar.vue'

    export default {
        data() {
            return {
                specialist: null,
                activeTab: 'schedule',
                specialistUrl: 'account/specialist?id=',
                tempDate: ''
            }
        },
        computed: {
            ...mapGetters(['userType']),
            formHeader() {
                return this.userType === 'specialist' ? 'Refer a patient' : this.userType === 'patient' ? 'Make an appointment' : '';
            }
        },
        components: {MakeAppointment, Calendar},
        methods: {
            getSpecialist: function (id) {
                axios.get(`${this.specialistUrl}${id}`).then((response) => {
                    this.specialist = response.data.result;
                });
            },
            initAppointment: function(date) {
                this.tempDate = date;
                this.activeTab = 'booking';
            }
        },
        mounted() {
            if (this.$route.params.id) {
                this.getSpecialist(this.$route.params.id);
            }
        }
    }
</script>

<style>
    .booking h3 {
        text-align: center;
    }
</style>