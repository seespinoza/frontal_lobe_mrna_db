/*Create Frontal Lobe Database database */

CREATE TABLE expression_values (
    sample_id            integer,     --Unique RNA-seq sample ID from Allen Brain Atlas
    gene_symbol          varchar,     --Gene Symbol
    sub_structure        varchar,     --Frontal lobe substructure where sample was taken.
    raw_counts           integer      --Raw RNA-seq counts for a certain sample gene.
);

CREATE TABLE maps_to (
    gene                 varchar,     --Gene Symbol
    gene_id              integer,     --Gene ID
    sample_id            integer      --Unique RNA-seq sample ID from Allen Brain Atlas  
);

CREATE TABLE differentially_expressed_genes (
    gene_symbol          varchar,     --Gene Symbol
    gene_id              integer      --Gene ID
);

CREATE TABLE associated (
    gene_id              integer,     --Gene ID
    go_id                varchar      --Unique GO ID for the term associated with the gene
);

CREATE TABLE go_terms (
    go_id                varchar,     --Unique GO ID
    term                 varchar      --Name of GO term
);

/* Copy data. */

