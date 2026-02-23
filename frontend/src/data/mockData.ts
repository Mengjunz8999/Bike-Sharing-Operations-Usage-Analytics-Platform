import { Bike, User } from './types'

export const mockBikes: Bike[] = [
  {
    bike_id: 'BK001',
    bike_type: 'classic',
    gear_count: 7,
    status: 'available',
  },
  {
    bike_id: 'BK002',
    bike_type: 'electric',
    battery_level: 87,
    max_range_km: 60,
    status: 'rented',
  },
  {
    bike_id: 'BK003',
    bike_type: 'electric',
    battery_level: 42,
    max_range_km: 50,
    status: 'available',
  },
  {
    bike_id: 'BK004',
    bike_type: 'classic',
    gear_count: 3,
    status: 'maintenance',
  },
  {
    bike_id: 'BK005',
    bike_type: 'electric',
    battery_level: 100,
    max_range_km: 80,
    status: 'available',
  },
  {
    bike_id: 'BK006',
    bike_type: 'classic',
    gear_count: 21,
    status: 'rented',
  },
]

export const mockUsers: User[] = [
  {
    user_id: 'USR001',
    name: 'Alice Chen',
    email: 'alice@example.com',
    user_type: 'member',
    membership_start: '2024-03-01',
    membership_tier: 'gold',
  },
  {
    user_id: 'USR002',
    name: 'Bob Müller',
    email: 'bob@example.com',
    user_type: 'casual',
  },
  {
    user_id: 'USR003',
    name: 'Carla Rossi',
    email: 'carla@example.com',
    user_type: 'member',
    membership_start: '2023-11-15',
    membership_tier: 'platinum',
  },
  {
    user_id: 'USR004',
    name: 'David Park',
    email: 'david@example.com',
    user_type: 'casual',
  },
  {
    user_id: 'USR005',
    name: 'Eva Santos',
    email: 'eva@example.com',
    user_type: 'member',
    membership_start: '2025-01-10',
    membership_tier: 'silver',
  },
]
