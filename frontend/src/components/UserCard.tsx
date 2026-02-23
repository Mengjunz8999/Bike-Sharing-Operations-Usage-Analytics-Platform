import { User, MemberUser } from '../types'

interface Props {
  user: User
}

const tierConfig = {
  silver: { label: 'Silver', color: 'bg-slate-400/20 text-slate-300 border border-slate-400/30' },
  gold: { label: 'Gold', color: 'bg-yellow-400/15 text-yellow-300 border border-yellow-400/30' },
  platinum: { label: 'Platinum', color: 'bg-cyan-400/15 text-cyan-300 border border-cyan-400/30' },
}

function initials(name: string) {
  return name
    .split(' ')
    .map((n) => n[0])
    .join('')
    .toUpperCase()
    .slice(0, 2)
}

export default function UserCard({ user }: Props) {
  const isMember = user.user_type === 'member'
  const member = isMember ? (user as MemberUser) : null

  return (
    <div className="card animate-slide-up cursor-default">
      <div className="flex items-start gap-4">
        {/* Avatar */}
        <div className="flex-shrink-0 w-12 h-12 rounded-xl bg-lime/10 border border-lime/20 flex items-center justify-center">
          <span className="font-display text-lime text-lg leading-none">{initials(user.name)}</span>
        </div>

        {/* Info */}
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 flex-wrap">
            <h3 className="font-body font-semibold text-paper truncate">{user.name}</h3>
            {isMember && member ? (
              <span className={`badge ${tierConfig[member.membership_tier].color}`}>
                {tierConfig[member.membership_tier].label}
              </span>
            ) : (
              <span className="badge bg-white/5 text-mist border border-white/10">Casual</span>
            )}
          </div>
          <p className="text-sm text-mist mt-0.5 truncate">{user.email}</p>
          <p className="font-mono text-xs text-white/30 mt-1">{user.user_id}</p>
        </div>
      </div>

      {isMember && member && (
        <div className="mt-4 pt-4 border-t border-white/5 text-xs text-mist font-mono">
          Member since {new Date(member.membership_start).toLocaleDateString('en-GB', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
          })}
        </div>
      )}
    </div>
  )
}
