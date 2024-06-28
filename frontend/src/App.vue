<script setup>
import Nav from './components/Nav.vue'
</script>

<template>
  <v-app class="bg-grey-lighten-3">
    <Nav />
    <v-row align-content="center">
      <v-col align="center">
        <router-view />
      </v-col>
    </v-row>
  </v-app>
</template>
