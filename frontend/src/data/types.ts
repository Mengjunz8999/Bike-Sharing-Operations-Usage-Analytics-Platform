// ── Bikes ──────────────────────────────────────────────────────────────────

export type BikeType = 'classic' | 'electric'

export interface BaseBike {
  bike_id: string
  bike_type: BikeType
  status: 'available' | 'rented' | 'maintenance'
}

export interface ClassicBike extends BaseBike {
  bike_type: 'classic'
  gear_count: number
}

export interface ElectricBike extends BaseBike {
  bike_type: 'electric'
  battery_level: number   // 0–100
  max_range_km: number
}

export type Bike = ClassicBike | ElectricBike

// ── Users ──────────────────────────────────────────────────────────────────

export type UserType = 'casual' | 'member'

export interface BaseUser {
  user_id: string
  name: string
  email: string
  user_type: UserType
}

export interface CasualUser extends BaseUser {
  user_type: 'casual'
}

export interface MemberUser extends BaseUser {
  user_type: 'member'
  membership_start: string   // ISO date string
  membership_tier: 'silver' | 'gold' | 'platinum'
}

export type User = CasualUser | MemberUser

// ── Stats ─────────────────────────────────────────────────────────────────

export interface DashboardStats {
  totalBikes: number
  availableBikes: number
  totalUsers: number
  memberUsers: number
}
