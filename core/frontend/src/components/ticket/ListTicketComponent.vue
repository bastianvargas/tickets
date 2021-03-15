<template>
    <div>
        <table>
            <tr>
                <th>Id</th>
                <th>Titulo</th>
                <th>Descripcion</th>
                <th>Estado</th>
                <th>Creado</th>
            </tr>
            <tr v-for="t in tickets" :key="t.id">
                <td>{{ t.id }}</td>
                <td>{{ t.title }}</td>
                <td>{{ t.description }}</td>
                <td>{{ t.state_str_ }}</td>
                <td>{{ datesFormat(t.created_at) }}</td>
            </tr>
        </table>
        
    </div>
</template>

<script>
export default {
    name: "ListTicketComponent",
    data() {
        return{
            tickets: []
        }
    },
    created() {
        this.getTicket()
    },
    methods: {
        async getTicket() {
            let path = 'http://localhost:8000/api/ticket/'
            let data = await fetch(path)
            this.tickets = await data.json()
        },
        datesFormat(string_date) {
            let date = new Date(string_date)
            return date.toLocaleString("ES-es")
        }
    }
}
</script>