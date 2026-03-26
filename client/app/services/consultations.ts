import { apiFetch } from './api';
import type { ConsultationResponse, ConsultationCreate } from '~/types';

export const consultations = {
  getAll: (search?: string | null) => {
    const params = search ? `?search=${encodeURIComponent(search)}` : '';
    return apiFetch<ConsultationResponse[]>(`/consultations/${params}`);
  },

  create: (data: ConsultationCreate) =>
    apiFetch<ConsultationResponse>('/consultations/', {
      method: 'POST',
      body: JSON.stringify(data),
    }),
};