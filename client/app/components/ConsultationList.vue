<template>
  <div class="space-y-4">
    <div>
      <input 
        v-model="searchTerm" 
        placeholder="Search by name" 
        @input="debouncedSearch"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
      />
    </div>
    <div v-if="loading" class="text-center py-8">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
      <p class="mt-2 text-gray-600">Loading consultations...</p>
    </div>
    <div v-else-if="consultations.length === 0" class="text-center py-8">
      <p class="text-gray-500">No consultations found.</p>
    </div>
    <div v-else class="grid gap-4">
      <div
        v-for="consult in consultations"
        :key="consult.id"
        class="bg-white rounded-lg shadow-md p-6 border-l-4 border-blue-500 hover:shadow-lg transition duration-200"
      >
        <h3 class="text-lg font-semibold text-gray-800">{{ consult.patient.name }}</h3>
        <p class="text-sm text-gray-500 mt-1">Doctor: {{ consult.doctor.name }}</p>
        <p class="text-gray-700 mt-3">{{ consult.description }}</p>
        <div v-if="consult.diagnosis" class="mt-3 pt-3 border-t border-gray-200">
          <span class="inline-block bg-blue-100 text-blue-800 text-xs px-3 py-1 rounded-full font-medium">
            {{ consult.diagnosis.code }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { consultations as consultationsApi } from '~/services/consultations';
import { useDebounceFn } from '@vueuse/core';
import type { ConsultationResponse } from '~/types';

const consultations = ref<ConsultationResponse[]>([]);
const allConsultations = ref<ConsultationResponse[]>([]);
const loading = ref(false);
const searchTerm = ref('');

onMounted(async () => {
    allConsultations.value = await consultationsApi.getAll();
    consultations.value = allConsultations.value;
});

const fetchConsultations = async (search?: string) => {
  loading.value = true;
  try {
    consultations.value = await consultationsApi.getAll(search);
  } catch (err) {
    console.error('Failed to fetch consultations', err);
  } finally {
    loading.value = false;
  }
};

const debouncedSearch = useDebounceFn(() => {
    if(searchTerm.value === ''){
        consultations.value = allConsultations.value;
        return;
    }
    fetchConsultations(searchTerm.value);
}, 300);

</script>