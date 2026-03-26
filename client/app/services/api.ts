export const API_BASE = import.meta.env.VITE_API_BASE;

export async function apiFetch<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
    console.log(API_BASE);
  const url = `${API_BASE}${endpoint}`;
  const response = await fetch(url, {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    credentials: 'include',
    ...options,
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`API Error ${response.status}: ${errorText}`);
  }

  return response.status === 204 ? (null as T) : await response.json();
}