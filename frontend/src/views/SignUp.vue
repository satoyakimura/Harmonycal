<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';


const router = useRouter()

const valid = ref(false)

const user_id = ref('')
const userIdRules = [
                      v => !!v || 'ユーザIDを入力してください',
                    //   v => 6 <= v.length || '6文字以上で入力してください',
                    ]

const showPassword = ref(false)
const password = ref('')
const passwordRules = [
                        v => !!v || 'パスワードを入力してください',
                        // v => 7 <= v.length || '8文字以上で入力してください',
                      ]

const registerAccount = async () => {
  await axios
    .post('/user/signup', {
      username: user_id.value,
      password: password.value,
    })
    .then((res) => {
      sessionStorage.setItem('user_id', res.data.id)
      sessionStorage.setItem('user_name', res.data.username)
      router.push('/')
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<template>
  <v-card max-width="600px" min-width="350px" style="width: 40%;">
    <v-card-title class="text-blue-grey-darken-2 font-weight-bold pa-5">
      新規登録
    </v-card-title>
    <v-divider />
    <v-card-text class="pa-5">
        <v-form v-model="valid">
            <v-text-field
              :rules="userIdRules"
              v-model="user_id"
              prepend-icon="mdi-account"
              label="ユーザ名"
              variant="outlined"
              required
              style="padding-right: 40px;"
            />
            <v-text-field
              @click:append="showPassword = !showPassword"
              v-bind:type="showPassword ? 'text' : 'password'"
              v-bind:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              v-model="password"
              :rules="passwordRules"
              prepend-icon="mdi-lock"
              label="パスワード"
              variant="outlined"
              required
            />
            <v-card-actions class="justify-center pa-3">
              <v-btn
                @click="registerAccount"
                :disabled="!valid"
                color="info"
                class="font-weight-bold text-h6"
                flat
              >
                登録
              </v-btn>
            </v-card-actions>
        </v-form>
    </v-card-text>
    <v-divider />
    <p class="text-center" style="padding-top: 20px;">
      すでにアカウントを<br>
      お持ちの方は<router-link to="/login">こちら</router-link>
    </p>
    <br>
  </v-card>
</template>
