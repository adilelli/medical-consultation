import { apiFetch } from './api';
import type { UserResponse, UserCreate, UserRole } from '~/types';

export const users = {
  getAll: (role?: UserRole | null) => {
    console.log('Fetching users with role:', role);
    const params = role !== undefined && role !== null ? `?role=${role}` : '';
    console.log('Constructed API endpoint:', `/users/${params}`);
    return apiFetch<UserResponse[]>(`/users/${params}`);
  },

  create: (data: UserCreate) =>
    apiFetch<UserResponse>('/users/', {
      method: 'POST',
      body: JSON.stringify(data),
    }),
};