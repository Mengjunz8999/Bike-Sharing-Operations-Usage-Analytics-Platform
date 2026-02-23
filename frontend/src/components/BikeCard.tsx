import { Bike, ClassicBike, ElectricBike } from '../types'

interface Props {
  bike: Bike
}

const statusConfig = {
  available: { label: 'Available', color: 'bg-lime/15 text-lime border border-lime/30' },
  rented: { label: 'Rented', color: 'bg-rust/15 text-rust border border-rust/30' },
  maintenance: { label: 'Maintenance', color: 'bg-yellow-400/15 text-yellow-300 border border-yellow-400/30' },
}

function BatteryBar({ level }: { level: number }) {
  const color = level > 50 ? 'bg-lime' : level > 20 ? 'bg-yellow-400' : 'bg-rust'
  return (
    <div className="mt-3">
      <div className="flex justify-between items-center mb-1">
        <span className="text-xs text-mist font-mono">Battery</span>
        <span className="text-xs font-mono font-medium text-paper">{level}%</span>
      </div>
      <div className="h-1.5 bg-white/10 rounded-full overflow-hidden">
        <div
          className={`h-full rounded-full transition-all duration-500 ${color}`}
          style={{ width: `${level}%` }}
        />
      </div>
    </div>
  )
}

export default function BikeCard({ bike }: Props) {
  const { label, color } = statusConfig[bike.status]

  return (
    <div className="card animate-slide-up group cursor-default">
      {/* Header */}
      <div className="flex items-start justify-between mb-4">
        <div>
          <p className="font-mono text-xs text-mist mb-0.5">{bike.bike_id}</p>
          <h3 className="font-display text-2xl tracking-wide">
            {bike.bike_type === 'electric' ? '⚡ Electric' : '🚲 Classic'}
          </h3>
        </div>
        <span className={`badge ${color}`}>{label}</span>
      </div>

      {/* Details */}
      {bike.bike_type === 'classic' ? (
        <div className="flex items-center gap-2 text-sm text-mist">
          <span className="font-mono">{(bike as ClassicBike).gear_count}</span>
          <span>gears</span>
        </div>
      ) : (
        <>
          <div className="flex items-center gap-2 text-sm text-mist">
            <span className="font-mono">{(bike as ElectricBike).max_range_km} km</span>
            <span>max range</span>
          </div>
          <BatteryBar level={(bike as ElectricBike).battery_level} />
        </>
      )}
    </div>
  )
}
