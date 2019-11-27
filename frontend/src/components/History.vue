<template>
    <div class="container">
        <el-row :gutter="30">
            <el-col :span="24">
                <el-table
                        :data="history"
                        style="width: 100%">
                    <el-table-column type="expand">
                        <template slot-scope="props">
                            <p>Notes</p>
                            <p>{{ props.row.notes }}</p>
                        </template>
                    </el-table-column>
                    <el-table-column
                            label="Date"
                            prop="date_created">
                    </el-table-column>
                    <el-table-column
                            label="title"
                            prop="title">
                    </el-table-column>
                    <el-table-column
                            label="Specialist"
                            prop="specialist__user__name">
                    </el-table-column>
                    <el-table-column
                      align="right">
                      <template slot="header" slot-scope="scope">
                        <el-button icon="el-icon-plus" size="mini" @click="initAdd"></el-button>
                      </template>
                      <template slot-scope="scope">
                        <el-button size="mini"
                                   @click="initEdit(scope.$index)">Edit
                        </el-button>
                        <el-button
                                size="mini"
                                type="danger"
                                @click="deleteHistory(scope.$index, scope.row.id)">Delete
                        </el-button>
                    </template>
                    </el-table-column>
                </el-table>
            </el-col>
            <history-form :is-active="showHistoryForm"
                          :action="historyFormAction"
                          :data="historyItem"
                          :patient="patient"
                          @closeHistoryModal="showHistoryForm=false"></history-form>
        </el-row>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import HistoryForm from '../forms/HistoryForm.vue';

    export default {
        data() {
            return {
                historyUrl: 'activity/history?id=',
                dataUrl: 'activity/history',
                history: [],
                historyItem: {},
                showHistoryForm: false,
                historyFormAction: ''
            }
        },
        props: {
            patient: [String | Number]
        },
        watch: {
            patient: {
                handler(val) {
                    if (val) {
                        this.getHistory();
                    }
                },
                deep: true,
				immediate: true
            }
        },
        computed: {
            ...mapGetters(['userType']),
        },
        components: {HistoryForm},
        methods: {
            getHistory: function () {
                axios.get(`${this.historyUrl}${this.patient}`).then((response) => {
                    this.history = response.data.result;
                })
            },
            initAdd: function() {
                this.showHistoryForm=true;
                this.historyFormAction='ADD';
            },
            initEdit: function(index) {
                this.historyFormAction = 'EDIT';
                this.historyItem = this.history[index];
                this.showHistoryForm=true;
            },
            deleteHistory: function(index, id) {
                this.$confirm('This will permanently delete the record. Continue?', 'Warning', {
                    confirmButtonText: 'OK',
                    cancelButtonText: 'Cancel',
                    type: 'warning'
                }).then(() => {
                    axios.delete(this.dataUrl, {data: {id}}).then(() => {
                        this.$message.success('The record has been deleted successfully');
                        this.history.splice(index, 1);
                    });
                }).catch(() => {
                    this.$message.error('An error occurred.');
                });
            }
        }
    }
</script>