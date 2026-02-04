CREATE TABLE naturezas_de_operacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    code TEXT,
    goevo_code TEXT,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE variaveis_de_ambiente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    value TEXT NOT NULL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE departamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE rpa_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    rpa_guid TEXT NOT NULL,
    rpa_status TEXT NOT NULL,

    rpa_params TEXT,

    rpa_error TEXT,

    rpa_init DATETIME,
    rpa_end DATETIME,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_rpa_guid ON rpa_log(rpa_guid);
CREATE INDEX idx_rpa_status ON rpa_log(rpa_status);

CREATE INDEX idx_env_name ON variaveis_de_ambiente(name);

CREATE INDEX idx_nat_cod ON naturezas_de_operacao(code);
