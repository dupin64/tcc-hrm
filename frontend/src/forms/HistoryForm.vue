<template>
    <el-dialog :title="`${action} PATIENT HISTORY`"
               :visible.sync="modalVisible"
               @close="exit"
               top="0">
        <el-form :model="form" ref="form">
            <el-form-item label="Title" prop="title" required>
                <el-input v-model="form.title"></el-input>
            </el-form-item>
            <el-form-item label="Specialist" prop="specialist" required>
                <el-select
                        v-model="form.specialist"
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
            <el-form-item label="Notes" prop="notes" required>
                <el-input v-model="form.notes"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="saveHistory">Save</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
    export default {
        data() {
            return {
                modalVisible: false,
                dataUrl: 'activity/history',
                specialistsUrl: 'account/search?keyword=',
                form: {
                    patient: '',
                    specialist: '',
                    title: '',
                    notes: ''
                },
                specialists: []
            }
        },
        props: {
            isActive: Boolean,
            action: String,
            data: Object,
            patient: [String | Number]
        },
        watch: {
            isActive(value) {
                this.modalVisible = value;
            },
            data: {
                handler(val) {
                    if (val) {
                        this.form = val;
                    }
                },
                deep: true,
                immediate: true
            }
        },
        methods: {
            exit() {
                this.$emit("closeHistoryModal");
            },
            saveHistory() {
                let method = 'put';
                let action = 'updated';
                if (this.action === 'ADD') {
                    method = 'post';
                    action = 'created';
                }
                const data = {...this.form};
                data.patient = this.patient;
                axios({
                    method: method,
                    url: this.dataUrl,
                    data: data
                }).then(() => {
                    this.$message.success(`The record has been ${action} successfully`);
                    this.exit();
                }).catch(() => {
                    this.$message.error('An error occurred.');
                });
            },
            getSpecialists: function (query) {
                axios.get(`${this.specialistsUrl}${query}`).then((response) => {
                    this.specialists = response.data.result;
                });
            },
        }
    }
</script>