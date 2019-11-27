<template>
    <div class="container">
        <el-row :gutter="30">
            <el-col :span="24">
                <el-table
                        :data="appointments"
                        style="width: 100%">
                    <el-table-column type="expand">
                        <template slot-scope="props">
                            <p>Notes</p>
                            <p>{{ props.row.notes }}</p>
                        </template>
                    </el-table-column>
                    <el-table-column
                            label="Date"
                            prop="date">
                    </el-table-column>
                    <el-table-column
                            label="title"
                            prop="title">
                    </el-table-column>
                    <el-table-column
                            :label="userType === 'specialist' ? 'Patient' : 'Specialist'"
                            :prop="userType === 'specialist' ? 'patient__user__name' : 'specialist__user__name'">
                    </el-table-column>
                    <el-table-column
                            label="Status">
                        <template slot-scope="scope">
                            <p>{{ scope.row.status | capitalize }}</p>
                        </template>
                    </el-table-column>
                    <el-table-column
                            label="Actions">
                        <template slot-scope="scope">
                            <el-button v-if="userType === 'specialist' && scope.row.status !== 'confirmed'"
                                       size="mini"
                                       @click="confirmAppointment(scope.$index, scope.row.id)">Confim
                            </el-button>
                            <el-button
                                    size="mini"
                                    type="danger"
                                    @click="cancelAppointment(scope.$index, scope.row.id)">Cancel
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';

    export default {
        data() {
            return {
                appointmentsUrl: 'activity/appointment',
                approveAppointmentsUrl: 'activity/approve_appointment?id=',
                cancelAppointmentsUrl: 'activity/cancel_appointment?id=',
                appointments: [],
            }
        },
        computed: {
            ...mapGetters(['userType']),
        },
        filters: {
            capitalize: function (value) {
                if (!value) return '';
                value = value.toString();
                return value.charAt(0).toUpperCase() + value.slice(1);
            }
        },
        methods: {
            confirmAppointment: function (index, id) {
                this.$confirm(`Would you like to confirm this appointment?`).then(() => {
                    axios.get(`${this.approveAppointmentsUrl}${id}`).then((response) => {
                        if (response.data.success) {
                            this.appointments[index].status = 'confirmed';
                            this.$message.success('This appointment has been confirmed successfully');
                        }
                    })
                }).catch(() => {
                });
            },
            cancelAppointment: function (index, id) {
                this.$confirm(`Would you like to cancel this appointment?`).then(() => {
                    axios.get(`${this.cancelAppointmentsUrl}${id}`).then((response) => {
                        if (response.data.success) {
                            this.appointments[index].status = 'cancelled';
                            this.$message.success('This appointment has been cancelled successfully');
                        }
                    })
                }).catch(() => {
                });
            },
            getAppointments: function () {
                axios.get(this.appointmentsUrl).then((response) => {
                    this.appointments = response.data.result;
                })
            }
        },
        mounted() {
            this.getAppointments();
        }
    }
</script>