<template>
    <div class="container">
        <el-row :gutter="30">
            <el-col :span="24">
                <el-input placeholder="Search for a specialist" v-model="keyword" class="specialist-filter">
                    <el-button slot="append" icon="el-icon-search" @click="getSpecialists"></el-button>
                </el-input>
            </el-col>
        </el-row>
        <el-row :gutter="30" class="specialists">
            <el-col :span="24">
                <el-divider content-position="left">Specialists</el-divider>
                <el-col v-for="item in specialists" :span="6">
                    <div class="specialist-mini" @click="showSpecialist(item)">
                        <el-card>
                            <p>{{ item.user__name }}</p>
                            <p><el-tag size="mini">{{ item.title }}</el-tag></p>
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
                specialists: [],
                specialistsUrl: 'account/search?keyword=',
            }
        },
        methods: {
            getSpecialists: function () {
                axios.get(`${this.specialistsUrl}${this.keyword}`).then((response) => {
                    this.specialists = response.data.result;
                });
            },
            showSpecialist: function (item) {
                this.$router.push({name: 'specialist', params: {id: item.id}});
            }
        },
        mounted() {
            this.getSpecialists();
        }
    }
</script>

<style>
    .specialist-filter .el-input-group__prepend {
        background-color: #fff;
    }
    .specialists {
        padding-top: 1em;
    }
    .specialist-mini {
        cursor: pointer;
    }
</style>