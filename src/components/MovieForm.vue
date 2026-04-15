<template>
<div class="container mt-4">
        <h2>Add a Movie</h2>

        <div v-if="message" class="alert alert-success">
            {{ message }}
        </div>

        <div v-if="errors.length" class="alert alert-danger">
            <ul>
                <li v-for="(error, index) in errors" :key="index">
                    {{ error }}
                </li>
            </ul>
        </div>

        <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
            <div class="form-group mb-3">
                <label for="title" class="form-label">Movie Title</label>
                <input
                    type="text"
                    id="title"
                    name="title"
                    class="form-control"
                    v-model="title"
                />
            </div>

            <div class="form-group mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea
                    id="description"
                    name="description"
                    class="form-control"
                    rows="4"
                    v-model="description"
                ></textarea>
            </div>

            <div class="form-group mb-3">
                <label for="poster" class="form-label">Movie Poster</label>
                <input
                    type="file"
                    id="poster"
                    name="poster"
                    class="form-control"
                    @change="handleFileUpload"
                    accept="image/*"
                />
            </div>

            <button type="submit" class="btn btn-primary">Save Movie</button>
        </form>

  </div>

</template>

<script setup>
//importing reactive variable function from Vue
import {ref} from 'vue'

//creating reactive variables 
const title = ref('');
const description = ref('');
const poster = ref(null);
const message = ref('');
const errors = ref([]);

// handle file input
function handleFileUpload(event) {
    poster.value = event.target.files[0];
    }

//required function (based on your instructions)
function saveMovie() {
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);

    fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data
    })
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
    // display a success message
        console.log(data);

        if (data.errors) {
            errors.value = data.errors;
            message.value = '';
        } else {
            message.value = data.message;
            errors.value = [];


            //reset form
            title.value='';
            description.value = '';
            poster.value = null;

            movieForm.reset();
        }
    })
    .catch(function (error) {
        console.log(error);
        errors.value = ["An error occurred while submitting the form."];
        message.value = '';
    });
}
</script>


