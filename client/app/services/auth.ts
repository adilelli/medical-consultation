// services/auth.ts
import { apiFetch } from './api';

export const auth = {
  login: (email: string, password: string) =>
    apiFetch<{ message: string }>('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    }),
  logout: () =>
    apiFetch('/auth/logout', { method: 'POST' }),
};