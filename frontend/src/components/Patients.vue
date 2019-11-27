<template>
    <div class="container">
        <el-row :gutter="30">
            <el-col :span="24">
                <el-input placeholder="Search for a patient" v-model="keyword" class="patient-filter">
                    <el-button slot="append" icon="el-icon-search" @click="getPatients"></el-button>
                </el-input>
            </el-col>
        </el-row>
        <el-row :gutter="30" class="patients">
            <el-col :span="24">
                <el-divider content-position="left">Patients</el-divider>
                <el-col v-for="item in patients" :span="6">
                    <div class="patient-mini" @click="showPatient(item)">
                        <el-card>
                            <p>{{ item.user__name }}</p>
                        </el-card>
                    </div>
                </el-col>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                keyword: '',
                patients: [],
                patientsUrl: 'account/patient?keyword=',
            }
        },
        methods: {
            getPatients: function () {
                axios.get(`${this.patientsUrl}${this.keyword}`).then((response) => {
                    this.patients = response.data.result;
                });
            },
            showPatient: function (item) {
                this.$router.push({name: 'patient', params: {id: item.id}});
            }
        },
        mounted() {
            this.getPatients();
        }
    }
</script>

<style>
    .patient-filter .el-input-group__prepend {
        background-color: #fff;
    }
    .patients {
        padding-top: 1em;
    }
    .patient-mini {
        cursor: pointer;
    }
</style>