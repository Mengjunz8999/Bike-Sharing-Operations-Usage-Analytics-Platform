import { useState, useMemo } from 'react'
import { mockBikes, mockUsers } from './data/mockData'
import { Bike, User } from './types'
import BikeCard from './components/BikeCard'
import UserCard from './components/UserCard'
import StatsBar from './components/StatsBar'

type Tab = 'bikes' | 'users'
type BikeFilter = 'all' | 'classic' | 'electric'
type StatusFilter = 'all' | 'available' | 'rented' | 'maintenance'

export default function App() {
  const [tab, setTab] = useState<Tab>('bikes')
  const [bikeTypeFilter, setBikeTypeFilter] = useState<BikeFilter>('all')
  const [statusFilter, setStatusFilter] = useState<StatusFilter>('all')
  const [userTypeFilter, setUserTypeFilter] = useState<'all' | 'casual' | 'member'>('all')
  const [search, setSearch] = useState('')

  const stats = useMemo(() => ({
    totalBikes: mockBikes.length,
    availableBikes: mockBikes.filter((b) => b.status === 'available').length,
    totalUsers: mockUsers.length,
    memberUsers: mockUsers.filter((u) => u.user_type === 'member').length,
  }), [])

  const filteredBikes = useMemo(() =>
    mockBikes.filter((b: Bike) => {
      if (bikeTypeFilter !== 'all' && b.bike_type !== bikeTypeFilter) return false
      if (statusFilter !== 'all' && b.status !== statusFilter) return false
      if (search && !b.bike_id.toLowerCase().includes(search.toLowerCase())) return false
      return true
    }),
    [bikeTypeFilter, statusFilter, search]
  )

  const filteredUsers = useMemo(() =>
    mockUsers.filter((u: User) => {
      if (userTypeFilter !== 'all' && u.user_type !== userTypeFilter) return false
      if (search && !u.name.toLowerCase().includes(search.toLowerCase()) && !u.email.toLowerCase().includes(search.toLowerCase())) return false
      return true
    }),
    [userTypeFilter, search]
  )

  return (
    <div className="min-h-screen">
      {/* Header */}
      <header className="border-b border-white/5 backdrop-blur sticky top-0 z-10 bg-ink/80">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <span className="text-2xl">🚴</span>
            <h1 className="font-display text-3xl tracking-widest text-paper">
              BIKE<span className="text-lime">FLEET</span>
            </h1>
          </div>
          <p className="text-xs font-mono text-mist hidden sm:block">
            Factory Pattern — Admin Panel
          </p>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 py-8">
        {/* Stats */}
        <StatsBar stats={stats} />

        {/* Tab switcher */}
        <div className="flex gap-2 mb-6">
          {(['bikes', 'users'] as Tab[]).map((t) => (
            <button
              key={t}
              onClick={() => { setTab(t); setSearch('') }}
              className={`px-5 py-2 rounded-xl text-sm font-body font-medium transition-all duration-150 capitalize
                ${tab === t ? 'tab-active' : 'tab-inactive'}`}
            >
              {t === 'bikes' ? `🚲 Bikes (${mockBikes.length})` : `👤 Users (${mockUsers.length})`}
            </button>
          ))}
        </div>

        {/* Filters */}
        <div className="flex flex-wrap gap-3 mb-6">
          {/* Search */}
          <input
            type="text"
            placeholder={tab === 'bikes' ? 'Search bike ID…' : 'Search name or email…'}
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="bg-slate border border-white/10 rounded-xl px-4 py-2 text-sm text-paper placeholder:text-mist/50 font-body focus:outline-none focus:border-lime/40 w-56"
          />

          {tab === 'bikes' ? (
            <>
              {/* Bike type */}
              {(['all', 'classic', 'electric'] as BikeFilter[]).map((f) => (
                <button
                  key={f}
                  onClick={() => setBikeTypeFilter(f)}
                  className={`btn-ghost text-sm capitalize ${bikeTypeFilter === f ? 'border-lime/40 text-lime' : ''}`}
                >
                  {f}
                </button>
              ))}
              {/* Status */}
              {(['all', 'available', 'rented', 'maintenance'] as StatusFilter[]).map((f) => (
                <button
                  key={f}
                  onClick={() => setStatusFilter(f)}
                  className={`btn-ghost text-sm capitalize ${statusFilter === f ? 'border-lime/40 text-lime' : ''}`}
                >
                  {f}
                </button>
              ))}
            </>
          ) : (
            <>
              {(['all', 'casual', 'member'] as const).map((f) => (
                <button
                  key={f}
                  onClick={() => setUserTypeFilter(f)}
                  className={`btn-ghost text-sm capitalize ${userTypeFilter === f ? 'border-lime/40 text-lime' : ''}`}
                >
                  {f}
                </button>
              ))}
            </>
          )}
        </div>

        {/* Grid */}
        {tab === 'bikes' ? (
          filteredBikes.length > 0 ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
              {filteredBikes.map((bike, i) => (
                <div key={bike.bike_id} style={{ animationDelay: `${i * 60}ms` }}>
                  <BikeCard bike={bike} />
                </div>
              ))}
            </div>
          ) : (
            <EmptyState message="No bikes match your filters." />
          )
        ) : (
          filteredUsers.length > 0 ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
              {filteredUsers.map((user, i) => (
                <div key={user.user_id} style={{ animationDelay: `${i * 60}ms` }}>
                  <UserCard user={user} />
                </div>
              ))}
            </div>
          ) : (
            <EmptyState message="No users match your filters." />
          )
        )}
      </main>
    </div>
  )
}

function EmptyState({ message }: { message: string }) {
  return (
    <div className="flex flex-col items-center justify-center py-24 text-mist">
      <span className="text-4xl mb-4">🔍</span>
      <p className="font-body text-sm">{message}</p>
    </div>
  )
}
