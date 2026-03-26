<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50" @click="$emit('close')">
    <div class="bg-white rounded-lg shadow-xl max-w-2xl w-full mx-4" @click.stop>
      <div class="flex justify-between items-center border-b border-gray-200 p-6">
        <h2 class="text-2xl font-bold text-gray-800">New Consultation</h2>
        <button 
          @click="$emit('close')"
          type="button"
          class="text-gray-500 hover:text-gray-700 text-2xl leading-none"
        >
          ×
        </button>
      </div>

      <form @submit.prevent="createConsultation" class="p-6 space-y-4">
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Doctor</label>
          <select 
            v-model="form.doctor_id"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            required
          >
            <option value="">Select Doctor</option>
            <option v-for="doctor in doctors" :key="doctor.id" :value="doctor.id">
              {{ doctor.name }}
            </option>
          </select>
        </div>

        <!-- Patient Selection -->
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Patient</label>
          <select 
            v-model="form.patient_id"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            required
          >
            <option value="">Select Patient</option>
            <option v-for="patient in patients" :key="patient.id" :value="patient.id">
              {{ patient.name }}
            </option>
          </select>
        </div>

        <div class="relative">
          <label class="block text-sm font-semibold text-gray-700 mb-2">Diagnosis</label>
          <input
            v-model="diagnosisSearch"
            placeholder="Search diagnosis by code or description"
            @input="debouncedDiagnosisSearch"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
          <div v-if="diagnosisResults.length" class="absolute top-full left-0 right-0 bg-white border border-gray-300 border-t-0 rounded-b-lg shadow-lg z-10">
            <div
              v-for="diag in diagnosisResults"
              :key="diag.id"
              @click="selectDiagnosis(diag)"
              class="px-4 py-3 hover:bg-blue-50 cursor-pointer border-b border-gray-200 last:border-b-0 transition"
            >
              <span class="font-semibold text-gray-800">{{ diag.code }}</span>
              <span class="text-gray-600"> – {{ diag.description }}</span>
            </div>
          </div>
        </div>

        <!-- Selected Diagnosis Display -->
        <div v-if="form.diagnosis_id" class="px-3 py-2 bg-blue-50 border border-blue-200 rounded-lg">
          <span class="text-sm text-gray-600">Selected: </span>
          <span class="text-sm font-semibold text-blue-700">{{ diagnosisSearch }}</span>
        </div>

        <!-- Consultation Notes -->
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Consultation Notes</label>
          <textarea 
            v-model="form.description" 
            placeholder="Enter consultation notes and observations"
            rows="4"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
            required
          />
        </div>

        <!-- Action Buttons -->
        <div class="flex gap-3 justify-end pt-4 border-t border-gray-200">
          <button
            type="button"
            @click="$emit('close')"
            class="px-6 py-2 border border-gray-300 rounded-lg text-gray-700 font-semibold hover:bg-gray-50 transition duration-200"
          >
            Cancel
          </button>
          <button 
            type="submit"
            class="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg shadow-md transition duration-200"
          >
            Create Consultation
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onBeforeMount } from 'vue';
import { consultations as consultationsApi } from '~/services/consultations';
import { diagnoses as diagnosesApi } from '~/services/disgnoses';
import { get, useDebounceFn } from '@vueuse/core';
import { users, users as usersApi } from '~/services/users';
import { UserRole } from '~/types';

const toast = useToast()

const form = ref({
  doctor_id: null,
  patient_id: null,
  description: '',
  diagnosis_id: null,
});

const doctors = ref([]);
const patients = ref([]);

onBeforeMount(async ()=>{
    const doctorsList = await usersApi.getAll(UserRole.Doctor);
    doctors.value = doctorsList
    const patientsList = await usersApi.getAll(UserRole.Patient);
    patients.value = patientsList
})

const diagnosisSearch = ref('');
const diagnosisResults = ref([]);

const debouncedDiagnosisSearch = useDebounceFn(async () => {
  if (!diagnosisSearch.value) {
    diagnosisResults.value = [];
    return;
  }
  const results = await diagnosesApi.searchDiagnoses(diagnosisSearch.value);
  diagnosisResults.value = results;
}, 300);

const selectDiagnosis = (diag) => {
  form.value.diagnosis_id = diag.id;
  diagnosisSearch.value = `${diag.code} – ${diag.description}`;
  diagnosisResults.value = [];
};

const createConsultation = async () => {
  try {
    await consultationsApi.create({
      doctor_id: form.value.doctor_id,
      patient_id: form.value.patient_id,
      description: form.value.description,
      diagnosis_id: form.value.diagnosis_id,
    });
    toast.success({ title: 'Success!', message: 'Consultation created successfully.' })
  } catch (err) {
    console.error('Creation failed', err);
    toast.error({ title: 'Error!', message: 'Failed to create consultation. Please try again.' });
  }
};
</script>