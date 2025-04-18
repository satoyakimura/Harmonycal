<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()

const signOutAccount = async () => {
  try {
    const response = await fetch('http://localhost:8888/logout', { 
      method: 'POST',
      credentials: 'include'  // Cookieを送信するために必要
    });

    if (response.ok) {
      console.log("Logged out successfully");
      router.push('/login');  // ログアウト後にログインページへ
    } else {
      console.error("Logout failed");
    }
  } catch (error) {
    console.error("Error logging out:", error);
  }
};
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
