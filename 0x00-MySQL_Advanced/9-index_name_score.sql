-- the column name and score in ascending order.
CREATE INDEX idx_name_first_score ON names(name(1), score);
