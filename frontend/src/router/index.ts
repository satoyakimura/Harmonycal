import { createRouter, createWebHistory } from 'vue-router'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import HomeView from '../views/HomeView.vue'
import ScheduleMonth from '../views/ScheduleMonth.vue'
// import ScheduleWeek from '../views/ScheduleWeek.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUp
    },
    {
      path: '/login',
      name: 'login',
      component: LogIn
    },
    {
      path: '/schedule/month',
      name : 'schedulemonth',
      component: ScheduleMonth
    },
    // {
    //   Path: '/schedule/week',
    //   name : 'scheduleweek',
    //   component: ScheduleWeek
    // },
  ]
})

export default router
