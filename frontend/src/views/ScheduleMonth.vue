<template>
    <div class="calendar-container">
        <FullCalendar
            :options="calendarOptions"
            class="fullcalendar"
        />

        <div v-if="selectedEvent" class="event-edit-form">
            <h3>予定の編集</h3>
            <label for="edit-title">タイトル:</label>
            <input type="text" id="edit-title" v-model="editedEvent.title"><br>

            <label for="edit-start">開始日時:</label>
            <input type="datetime-local" id="edit-start" v-model="editedEvent.start"><br>

            <label for="edit-end">終了日時:</label>
            <input type="datetime-local" id="edit-end" v-model="editedEvent.end"><br>

            <label for="edit-description">詳細:</label>
            <textarea id="edit-description" v-model="editedEvent.description"></textarea><br>

            <button @click="updateSchedule">保存</button>
            <button @click="closeEditForm">キャンセル</button>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import FullCalendar from '@fullcalendar/vue3';
import dayGridPlugin from '@fullcalendar/daygrid';
import jaLocale from '@fullcalendar/core/locales/ja';

const events = ref([]); // イベントデータを保持するリアクティブ変数

const fetchSchedules = async () => {
    try {
        const response = await fetch('http://localhost:8888/schedule/month', {
            method: 'GET',
            credentials: 'include' // クッキーを送る
        });

        if (!response.ok) {
            throw new Error('Failed to fetch schedules');
        }

        const data = await response.json();

        // 取得したデータを FullCalendar 用の形式に変換
        events.value = data.map(schedule => ({
            title: schedule.title,
            start: new Date(schedule.start_date).toISOString(),
            end: new Date(schedule.end_date).toISOString(),
            description: schedule.description
        }));
    } catch (error) {
        console.error('Error fetching schedules:', error);
    }
};

// Vue の onMounted でデータ取得を実行
onMounted(fetchSchedules);

// calendarOptions を computed にして events を動的に反映
const calendarOptions = computed(() => ({
    plugins: [dayGridPlugin],
    initialView: 'dayGridMonth',
    height: 'calc(100vh - 20px)', // ナビゲーションバー分を差し引く
    locale: jaLocale,
    headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,dayGridWeek'
    },
    events: events.value // 直接 events を適用
}));
</script>

<style>
.calendar-container {
    padding-top: 80px;
    width: 100vw;
    overflow-x: auto;

}
.fullcalendar {
    width: 100%;
}
</style>
