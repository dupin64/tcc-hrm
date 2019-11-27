<template>
    <el-row :gutter="30">
        <navigation></navigation>
        <router-view></router-view>
    </el-row>
</template>

<script>
    import Navigation from './components/Navigation.vue';
    export default {
        name: 'App',
        data() {
            return {}
        },
        components: {Navigation}
    }
</script>

<style>
    body {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c3e50;
    }

    .container {
        padding: 2em;
    }

    .el-select, .el-input {
        width: 100%;
    }

    @media (max-width: 768px) {
        .login-page, .register-page {
            width: 100%;
        }
    }
</style>