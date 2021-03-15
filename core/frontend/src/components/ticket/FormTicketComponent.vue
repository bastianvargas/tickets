<template>
    <div>
        <form action="">
            <label for="">Titulo</label>
            <input type="text" v-model="title">
            <br>
            <label for="">Descripcion</label>
            <input type="text" v-model="description"> 
            <label for="">Estado</label>
            <select name="" id="" v-model="state">
                <option value="">Seleccionar</option>
                <option v-for="s in states" :key="s.id" :value="s.id">{{ s.name }}</option>
            </select>
            <br>
            <button type="button" @click="save">Guardar</button>
        </form>
    </div>
</template>

<script>
export default {
    name: "FormTicketComponent",
    data() {
        return {
            title: null,
            description: null,
            state: "",
            states: []
        }
    },
    created() {
        this.getState();
    },
    methods: {
        async getState() {
            let path = 'http://localhost:8000/api/state/'
            let data = await fetch(path)
            this.states = await data.json()
        },
        async save() {
            let path = 'http://localhost:8000/api/ticket/'

            let data = {
                title: this.title,
                description: this.description,
                state: this.state
            }
            
            let result = await fetch(path, {
                headers: {
                    'Content-Type': "application/json",
                    'Accept': "application/json"
                },
                method: "post",
                body: JSON.stringify(data)
            })

            if (result.status == 200 || result.status == 201 ) {
                alert("se guardo correctamente")
            } else {
                alert("no se guardo")
            }

        }
    }
}
</script>