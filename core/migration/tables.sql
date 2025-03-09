CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TYPE TIMESTAMPTZ
);

CREATE TABLE datarecord (
    id TEXT PRIMARY KEY,
    data JSONB NOT NULL,
    collection TEXT DEFAULT 'default',
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER REFERENCES "user"(id)
);

CREATE TABLE apikey (
    id SERIAL PRIMARY KEY,
    key TEXT NOT NULL UNIQUE,
    subscription_type TEXT NOT NULL,
    user_id INTEGER REFERENCES "user"(id) ON DELETE CASCADE
);
