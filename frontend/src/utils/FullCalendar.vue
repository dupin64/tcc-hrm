<template>
    <div class='full-calendar'>
        <div class='header'>
            <el-button size="mini" @click="toggleWeekends">Toggle weekends</el-button>
            Click a date/time to book an appointment
        </div>
        <FullCalendar
                class='body'
                ref="fullCalendar"
                defaultView="dayGridMonth"
                :header="headerConfig"
                :plugins="calendarPlugins"
                :weekends="calendarWeekends"
                :events="events"
                @dateClick="handleDateClick"
        />
    </div>
</template>

<script>
    import FullCalendar from '@fullcalendar/vue'
    import dayGridPlugin from '@fullcalendar/daygrid'
    import timeGridPlugin from '@fullcalendar/timegrid'
    import interactionPlugin from '@fullcalendar/interaction'

    export default {
        components: {
            FullCalendar
        },
        data: function () {
            return {
                calendarPlugins: [
                    dayGridPlugin,
                    timeGridPlugin,
                    interactionPlugin
                ],
                calendarWeekends: true,
                headerConfig: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
                }
            }
        },
        props: {
            schedule: Array
        },
        computed: {
            events() {
                let schedule = [...this.schedule];
                return schedule.map((item) => { return {
                    title: item.status === 'confirmed' ? 'Confirmed' : 'Pending', start: item.date,
                    color: item.status === 'confirmed' ? 'orange' : 'green'}
                });
            }
        },
        methods: {
            toggleWeekends() {
                this.calendarWeekends = !this.calendarWeekends;
            },
            handleDateClick(arg) {
                this.$confirm(`Would you like to make an appointment on ${arg.dateStr}?`).then(() => {
                    this.$emit('initAppointment', arg.dateStr);
				}).catch(() => {});
            }
        }
    }
</script>

<style lang='scss'>
    @import '~@fullcalendar/core/main.css';
    @import '~@fullcalendar/daygrid/main.css';
    @import '~@fullcalendar/timegrid/main.css';

    .demo-app {
        font-family: Arial, Helvetica Neue, Helvetica, sans-serif;
        font-size: 14px;
    }

    .header {
        margin: 0 0 3em;
    }

    .body {
        margin: 0 auto;
        max-width: 900px;
    }
</style>