<template>
    <div>
        <h2>Nuevo Ticket</h2>
        <form-ticket-component />
    </div>
</template>
<script>
import FormTicketComponent from '../../components/ticket/FormTicketComponent.vue'
export default {
    components: {FormTicketComponent},
    name: "CreateTicket"
}
</script>