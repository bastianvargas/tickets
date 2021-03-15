<template>
    <div>
        <h2>listado de ticket</h2>
        <list-ticket-component />
    </div>
</template>

<script>
import ListTicketComponent from '../../components/ticket/ListTicketComponent.vue'
export default {
    components: {ListTicketComponent},
    name : "ListTicket"
}
</script>