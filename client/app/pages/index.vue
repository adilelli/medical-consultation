<template>
  <div class="max-w-7xl mx-auto px-6 py-8">
    <div class="flex justify-between items-center mb-8">
      <h1 class="text-3xl font-bold text-gray-800">Consultations</h1>
      <button 
        @click="showCreateModal = true"
        class="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-6 rounded-lg shadow-md transition duration-200"
      >
        New Consultation
      </button>
    </div>

    <ConsultationList/>

    <CreateConsultationModal
      v-if="showCreateModal"
      @close="showCreateModal = false"
      @created="handleConsultationCreated"
    />
  </div>
</template>

<script setup>
import ConsultationList from '~/components/ConsultationList.vue'
import CreateConsultationModal from '~/components/CreateConsultationModal.vue'
import { ref } from 'vue'

const showCreateModal = ref(false)

const handleConsultationCreated = () => {
  showCreateModal.value = false
}
</script>