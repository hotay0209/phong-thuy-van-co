-- PostgreSQL schema equivalent to SQLAlchemy MVP model
CREATE TABLE IF NOT EXISTS house_analyses (
  id BIGSERIAL PRIMARY KEY,
  house_name VARCHAR(160) NOT NULL DEFAULT 'Nhà ở',
  address VARCHAR(300),
  construction_year INTEGER NOT NULL,
  facing_degrees DOUBLE PRECISION NOT NULL CHECK (facing_degrees >= 0 AND facing_degrees < 360),
  facing_mountain VARCHAR(8) NOT NULL,
  sitting_mountain VARCHAR(8) NOT NULL,
  period_number INTEGER NOT NULL CHECK (period_number BETWEEN 1 AND 9),
  result_json TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS ix_house_analyses_id ON house_analyses(id);
