import { DashboardStats } from '../data/types'

interface Props {
  stats: DashboardStats
}

interface StatItemProps {
  label: string
  value: number
  accent?: boolean
}

function StatItem({ label, value, accent }: StatItemProps) {
  return (
    <div className="flex flex-col">
      <span className={`font-display text-4xl leading-none ${accent ? 'text-lime' : 'text-paper'}`}>
        {value}
      </span>
      <span className="text-xs text-mist mt-1 font-body">{label}</span>
    </div>
  )
}

export default function StatsBar({ stats }: Props) {
  return (
    <div className="bg-slate border border-white/5 rounded-2xl p-6 mb-8 animate-fade-in">
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-6">
        <StatItem label="Total Bikes" value={stats.totalBikes} />
        <StatItem label="Available" value={stats.availableBikes} accent />
        <StatItem label="Total Users" value={stats.totalUsers} />
        <StatItem label="Members" value={stats.memberUsers} accent />
      </div>
    </div>
  )
}
