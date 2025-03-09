CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE datarecord (
    id TEXT PRIMARY KEY,
    data JSONB NOT NULL,
    collection TEXT DEFAULT 'default',
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER REFERENCES "user"(id)
);
