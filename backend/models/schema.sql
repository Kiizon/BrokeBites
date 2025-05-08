
CREATE TABLE postal_codes (
  code       TEXT    PRIMARY KEY,
  queried_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS flyers (
  id         TEXT    PRIMARY KEY,
  store      TEXT    NOT NULL,
  flyer_date DATE    NOT NULL
);

CREATE TABLE IF NOT EXISTS postal_code_flyers (
  postal_code TEXT  NOT NULL REFERENCES postal_codes(code),
  flyer_id    TEXT  NOT NULL REFERENCES flyers(id),
  PRIMARY KEY (postal_code, flyer_id)
);

CREATE TABLE sale_items (
  id          SERIAL PRIMARY KEY,
  flyer_id    TEXT   NOT NULL REFERENCES flyers(id),
  name        TEXT   NOT NULL,
  sale_price  NUMERIC
);
