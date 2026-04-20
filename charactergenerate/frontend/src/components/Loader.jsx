export function Loader({ small = false }) {
  return <span className={`loader${small ? ' loader-small' : ''}`} aria-label="Loading" />
}
