export interface UserSimple {
  id: number;
  name: string;
}

export interface DiagnosisSimple {
  id: number;
  code: string;
}

export enum UserRole {
  Patient = 1,
  Doctor = 2,
}

export interface UserResponse {
  id: number;
  email: string;
  name: string;
  role: UserRole;
  created_date: string;
}

export interface UserCreate {
  email: string;
  name: string;
  role: UserRole;
}

export interface ConsultationCreate {
  doctor_id: number;
  patient_id: number;
  diagnosis_id: number;
  description: string;
}

export interface ConsultationResponse {
  id: number;
  doctor: UserSimple;
  patient: UserSimple;
  description: string;
  created_date: string;
  diagnosis: DiagnosisSimple;
}

// Diagnosis
export interface DiagnosisResponse {
  id: number;
  code: string;
  description: string;
}