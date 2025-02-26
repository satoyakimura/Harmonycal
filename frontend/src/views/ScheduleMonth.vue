<template>
    <v-container fluid class="calendar-container">
      <v-row class="justify-center">
        <v-col cols="12" md="10" lg="8">
          <v-card>
            <v-card-title>
              <v-btn @click="goToPreviousMonth" icon>
                <v-icon>mdi-chevron-left</v-icon>
              </v-btn>
              <span class="text-h4">{{ formattedMonth }}</span>
              <v-btn @click="goToNextMonth" icon>
                <v-icon>mdi-chevron-right</v-icon>
              </v-btn>
            </v-card-title>
            <v-divider></v-divider>
            <!-- 曜日の表示 -->
            <v-card-text>
              <v-row class="calendar-header">
                <v-col v-for="(day, index) in weekdays" :key="index" cols="1" class="text-center">
                  <span class="text-body-1">{{ day }}</span>
                </v-col>
              </v-row>
              <v-row class="calendar-body">
                <!-- 空白のセル -->
                <v-col
                  v-for="(day, index) in leadingEmptyDays"
                  :key="'empty-' + index"
                  cols="1"
                  class="calendar-cell"
                ></v-col>
  
                <!-- 日付のセル -->
                <v-col
                  v-for="(day, index) in daysInMonth"
                  :key="index"
                  cols="1"
                  class="calendar-cell"
                >
                  <v-card :class="{'bg-blue-grey': isToday(day)}" class="day-card">
                    <v-card-title class="text-center">{{ day.getDate() }}</v-card-title>
                    <v-list dense>
                      <v-list-item-group v-if="eventsForDay(day)">
                        <v-list-item v-for="(event, index) in eventsForDay(day)" :key="index">
                          <v-list-item-content>
                            <v-list-item-title>{{ event.title }}</v-list-item-title>
                            <v-list-item-subtitle>{{ event.description }}</v-list-item-subtitle>
                          </v-list-item-content>
                        </v-list-item>
                      </v-list-item-group>
                    </v-list>
                  </v-card>
                </v-col>
                <!-- 空白のセル（最後の週に余る場合）-->
                <v-col
                  v-for="(day, index) in trailingEmptyDays"
                  :key="'empty-end-' + index"
                  cols="1"
                  class="calendar-cell"
                ></v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  import { format, startOfMonth, endOfMonth, addMonths, subMonths, eachDayOfInterval, getDay } from 'date-fns';
  
  const router = useRouter();
  const currentMonth = ref(new Date());
  const allSchedules = ref([]);  // ユーザーの全スケジュール
  const formattedMonth = computed(() => format(currentMonth.value, 'yyyy年MM月'));
  const daysInMonth = ref([]);
  const weekdays = ['日', '月', '火', '水', '木', '金', '土'];  // 曜日
  
  // 月初の曜日と、空白の日数を計算（その月の最初の曜日に基づく）
  const leadingEmptyDays = computed(() => {
    const startOfMonthDate = startOfMonth(currentMonth.value);
    const startDayOfWeek = getDay(startOfMonthDate);  // 月の初日の曜日を取得
    return Array(startDayOfWeek).fill(null);  // 初日の曜日分だけ空白を追加
  });
  
  // 最後の週の余りの日数
  const trailingEmptyDays = computed(() => {
    const endOfMonthDate = endOfMonth(currentMonth.value);
    const endDayOfWeek = getDay(endOfMonthDate);  // 月末の曜日を取得
    const trailingDays = 6 - endDayOfWeek;  // 月末が土曜日なら0、金曜日なら1というように余りを計算
    return Array(trailingDays).fill(null);  // 余った日数分だけ空白を追加
  });
  
  // フィルタリングされた予定を表示するためのメソッド
  const eventsForDay = (day) => allSchedules.value.filter(event => {
    const eventStartDate = new Date(event.start_date);
    return eventStartDate.getDate() === day.getDate() && eventStartDate.getMonth() === day.getMonth();
  });
  
  // 今日かどうかを判定するメソッド
  const isToday = (day) => format(day, 'yyyy-MM-dd') === format(new Date(), 'yyyy-MM-dd');
  
  // 月初と月末の日付を取得して、その間の日付をリスト化
  const getDaysInMonth = () => {
    const start = startOfMonth(currentMonth.value);
    const end = endOfMonth(currentMonth.value);
    daysInMonth.value = eachDayOfInterval({ start, end });
  };
  
  const fetchAllSchedules = async () => {
    try {
      const response = await axios.get('/schedule/month');  // 全てのスケジュールを取得
      allSchedules.value = response.data;
    } catch (error) {
      console.error('Error fetching schedule:', error);
      router.push('/login');
    }
  };
  
  // 前月に移動するメソッド
  const goToPreviousMonth = () => {
    currentMonth.value = subMonths(currentMonth.value, 1);
    getDaysInMonth();
    fetchAllSchedules();  // 新しい月に合わせてデータを再取得
  };
  
  // 次月に移動するメソッド
  const goToNextMonth = () => {
    currentMonth.value = addMonths(currentMonth.value, 1);
    getDaysInMonth();
    fetchAllSchedules();  // 新しい月に合わせてデータを再取得
  };
  
  // コンポーネントがマウントされた際に呼び出される
  onMounted(() => {
    getDaysInMonth();
    fetchAllSchedules();  // 初期スケジュールデータを取得
  });
  </script>
  
  <style scoped>
  .calendar-container {
    height: 80vh;  /* 画面いっぱいにカレンダーを表示 */
    width: 100vh;
    display: flex;
    flex-direction: column;
  }
  
  .calendar-header {
    display: flex;
    justify-content: space-between;
  }
  
  .calendar-body {
    overflow-y: auto;
  }
  
  .calendar-cell {
    padding: 10px;
  }
  
  .day-card {
    width: 100%;  /* 横幅を100%に設定 */
    height: 100%;  /* 縦幅を100%に設定 */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  
  .v-card-title {
    font-size: 1.4rem;
    padding: 8px;
  }
  
  .v-list-item-title {
    font-size: 1rem;
  }
  
  .v-list-item-subtitle {
    font-size: 0.9rem;
  }
  
  .bg-blue-grey {
    background-color: #607d8b;
    color: white;
  }
  
  @media (max-width: 600px) {
    .calendar-cell {
      padding: 5px;
    }
  
    .v-card-title {
      font-size: 1.2rem;
    }
  
    .day-card {
      width: 100%;  /* 横幅を100%に設定 */
      height: 100%;  /* 縦幅を100%に設定 */
    }
  }
  </style>
  