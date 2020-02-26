/*Create Frontal Lobe Database database */

CREATE TABLE expression_values (
    sample_id            integer,
    gene_symbol          varchar,
    sub_structure        varchar
);

CREATE TABLE maps_to (
    gene                 varchar,
    gene_id              integer
);

CREATE TABLE differentially_expressed_genes (
    gene_symbol          varchar,
    gene_id              integer
);

CREATE TABLE associated (
    gene_id              integer,
    go_id                varchar
);

CREATE TABLE go_terms (
    go_id                varchar,
    term                 varchar,
);

/* Copy data. */

