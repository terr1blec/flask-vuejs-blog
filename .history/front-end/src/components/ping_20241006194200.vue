<template>
    <div>
        <p>{{ msg }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Ping',
    data() {
        return {
            msg: ''
        }
    },
    method: {
        getMessage() {
            axios.get('http://localhost:5000/ping')
                .then(response => {
                    this.msg = response.data;
                })
                .catch(error => {
                    console.error(error);
                });
        }
    },
    created() {
        this.getMessage();
    }
}
</script>