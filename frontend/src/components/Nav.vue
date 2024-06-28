<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()

const signOutAccount = () => {
  sessionStorage.removeItem('user_id')
  sessionStorage.removeItem('user_name')
  router.push('/login')
}
</script>
<template>
  <v-app-bar color="indigo">
    <v-toolbar-title class="font-weight-black" style="padding-left: 20px;">
      Sample Note
    </v-toolbar-title>
    <v-spacer />
    <v-btn @click="signOutAccount" icon="mdi-logout" />
  </v-app-bar>
</template>
