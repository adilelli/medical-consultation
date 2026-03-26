<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center px-4">
    <div class="w-full max-w-md">
      <!-- Card Container -->
      <div class="bg-white rounded-lg shadow-xl overflow-hidden">
        <!-- Header Section -->
        <div class="bg-blue-600 px-6 py-8">
          <h1 class="text-3xl font-bold text-white text-center">Medical Consultation</h1>
          <p class="text-blue-100 text-center mt-2">Sign in to your account</p>
        </div>

        <!-- Form Section -->
        <form @submit.prevent="login" class="p-8 space-y-6">
          <!-- Email Field -->
          <div>
            <label for="email" class="block text-sm font-semibold text-gray-700 mb-2">
              Email Address
            </label>
            <input
              id="email"
              v-model="email"
              type="email"
              placeholder="you@example.com"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
            />
          </div>

          <!-- Password Field -->
          <div>
            <label for="password" class="block text-sm font-semibold text-gray-700 mb-2">
              Password
            </label>
            <input
              id="password"
              v-model="password"
              type="password"
              placeholder="Enter your password"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
            />
          </div>

          <!-- Error Message -->
          <div
            v-if="error"
            class="p-4 bg-red-50 border border-red-200 rounded-lg"
          >
            <p class="text-sm text-red-700 font-medium">{{ error }}</p>
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            class="w-full bg-blue-600 hover:from-blue-700 hover:to-indigo-700 text-white font-semibold py-3 rounded-lg transition duration-200 shadow-md hover:shadow-lg"
          >
            Sign In
          </button>
        </form>

        <!-- Footer -->
        <div class="px-8 py-4 bg-gray-50 border-t border-gray-200 text-center">
          <p class="text-sm text-gray-600">
            Don't have an account?
            <NuxtLink to="/signup" class="font-semibold text-blue-600 hover:text-blue-700">
              Sign up
            </NuxtLink>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
// import { t } from 'vue-router/dist/index-BzEKChPW.js';
import { auth } from '~/services/auth';
import { useRouter } from 'vue-router';

const router = useRouter();
const toast = useToast();
const email = ref('');
const password = ref('');
const error = ref('');

const login = async () => {
  try {
    await auth.login(email.value, password.value);
    toast.success('Login successful');
    router.push('/');
  } catch (err) {
    toast.error('Login failed');
  }
};
</script>