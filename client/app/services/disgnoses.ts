import { apiFetch } from './api';
import type { DiagnosisResponse } from '~/types';

export const diagnoses = {
  searchDiagnoses: (search?: string | null) => {
    const params = search ? `?search=${encodeURIComponent(search)}` : '';
    return apiFetch<DiagnosisResponse[]>(`/diagnoses/${params}`);
  },
};